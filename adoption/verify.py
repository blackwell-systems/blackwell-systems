"""First-pass sort of raw.tsv into candidates for human review.

Repositories already in adopters.yaml are skipped. Every other hit is classified: own repos,
forks, copies of another project, lockfile-only (indirect) appearances, listings and
documentation-only mentions are excluded; the rest are opened and checked for
project-specific evidence. The result, candidates.json, is a review queue: confirm each
"candidate" by hand before adding it to adopters.yaml.

Usage: python3 adoption/verify.py   (requires an authenticated gh CLI and PyYAML)
"""
import base64, collections, csv, json, os, re, subprocess, sys
import yaml

HERE = os.path.dirname(os.path.abspath(__file__))
OWN = {'blackwell-systems', 'bide-ai'}
LOCK = re.compile(r'(^|/)(package-lock\.json|pnpm-lock\.yaml|yarn\.lock|bun\.lockb?|go\.sum|go\.work\.sum|poetry\.lock|uv\.lock|cargo\.lock|packages\.lock\.json|npm-shrinkwrap\.json)$|_cacache|node_modules/', re.I)
COPY = re.compile(r'open-sse/services/compression/engines/headroom|chrome-devtools-mcp/|extensions/chrome-devtools-mcp', re.I)
LISTING = re.compile(r'awesome|mcp-servers|directory|registry|changefeed|stars|catalog|curated|lists?\b|digest|vault|knowledge|research|textbook|skills-hub|plugin-repository|discovery|file-history|trend|study', re.I)
DOCS = re.compile(r'\.(md|mdx|rst|txt|html|adoc)$', re.I)
EVIDENCE = {
    'gcf': re.compile(r'@blackwell-systems/gcf|blackwell-systems/gcf|gcf-go|gcf-python|BlackwellSystems\.Gcf|gcf-proxy|from gcf import (encode_generic|decode|encode)', re.I),
    'agent-lsp': re.compile(r'blackwell-systems/agent-lsp|tap/agent-lsp|"command"\s*:\s*"agent-lsp"|command\s*=\s*"agent-lsp"|agent-lsp\.com|pname\s*=\s*"agent-lsp"|lsp-safe-edit', re.I),
    'mcp-assert': re.compile(r'blackwell-systems/mcp-assert|blackwellsystems/mcp-assert|mcp-assert-action|pytest-mcp-assert|vitest-mcp-assert|jest-mcp-assert|mcp-assert (audit|run|scan|init|generate)', re.I),
    'emulators': re.compile(r'blackwell-systems/gcp-(secret-manager|kms|iam|eventarc)-emulator|blackwell-systems/gcp-emulator', re.I),
    'knowing': re.compile(r'blackwell-systems/knowing|@blackwell-systems/knowing|"command"\s*:\s*"knowing"', re.I),
    'claudewatch': re.compile(r'blackwell-systems/claudewatch|"command"\s*:\s*"[^"]*claudewatch', re.I),
}

def gh(args):
    r = subprocess.run(['gh', 'api'] + args, capture_output=True, text=True)
    return r.stdout if r.returncode == 0 else None

known = {a['repo'].lower() for a in yaml.safe_load(open(os.path.join(HERE, 'adopters.yaml')))['adopters']}
hits = collections.defaultdict(set)
for project, repo, path, _ in csv.reader(open(os.path.join(HERE, 'raw.tsv')), delimiter='\t'):
    if repo.split('/')[0].lower() in OWN or repo.lower() in known:
        continue
    hits[(project, repo)].add(path)

forks = {}
repos = sorted({r for _, r in hits})
for i in range(0, len(repos), 40):
    parts = [f'r{j}: repository(owner: {json.dumps(r.split("/")[0])}, name: {json.dumps(r.split("/")[1])}) {{ isFork }}' for j, r in enumerate(repos[i:i + 40])]
    out = gh(['graphql', '-f', 'query=query { ' + ' '.join(parts) + ' }'])
    data = (json.loads(out).get('data') or {}) if out else {}
    for j, r in enumerate(repos[i:i + 40]):
        forks[r] = (data.get(f'r{j}') or {}).get('isFork')

result = {}
for (project, repo), paths in sorted(hits.items()):
    evidence = None
    direct = [p for p in paths if not LOCK.search(p) and not COPY.search(p)]
    if forks.get(repo):
        status = 'excluded: fork'
    elif not direct:
        status = 'excluded: copy of another project' if any(COPY.search(p) for p in paths) else 'excluded: lockfile only (indirect)'
    elif LISTING.search(repo.split('/')[1]) and all(DOCS.search(p) or p.endswith('.json') for p in direct):
        status = 'excluded: listing'
    elif all(DOCS.search(p) for p in direct):
        status = 'excluded: mention only'
    else:
        status = 'excluded: no project-specific evidence'
        for p in sorted(direct, key=len)[:3]:
            c = gh([f'repos/{repo}/contents/{p}', '--jq', '.content'])
            if not c:
                continue
            text = base64.b64decode(c).decode('utf-8', 'ignore')
            m = EVIDENCE[project].search(text)
            if m:
                status, evidence = 'candidate', {'path': p, 'snippet': re.sub(r'\s+', ' ', text[max(0, m.start() - 80):m.start() + 120])}
                break
    result[f'{project}|{repo}'] = {'project': project, 'repo': repo, 'status': status, 'paths': sorted(paths)[:5], **({'evidence': evidence} if status == 'candidate' else {})}

json.dump(result, open(os.path.join(HERE, 'candidates.json'), 'w'), indent=1)
counts = collections.Counter(v['status'] for v in result.values())
print(dict(counts))
for v in result.values():
    if v['status'] == 'candidate':
        print(f"review: {v['project']:11} {v['repo']:50} {v['evidence']['path']}", file=sys.stderr)
