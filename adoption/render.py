"""Render adopters.yaml into docs/ADOPTERS.md and docs/adopters.csv, with live star counts.

Usage: python3 adoption/render.py   (requires an authenticated gh CLI and PyYAML)
"""
import collections, csv, json, os, subprocess
import yaml

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
data = yaml.safe_load(open(os.path.join(HERE, 'adopters.yaml')))
adopters = data['adopters']
ORDER = ['GCF', 'agent-lsp', 'mcp-assert', 'GCP emulators', 'claudewatch', 'knowing']
LINKS = {'GCF': 'https://github.com/blackwell-systems/gcf', 'agent-lsp': 'https://github.com/blackwell-systems/agent-lsp',
         'mcp-assert': 'https://github.com/blackwell-systems/mcp-assert', 'GCP emulators': 'https://github.com/blackwell-systems/gcp-emulator',
         'claudewatch': 'https://github.com/blackwell-systems/claudewatch', 'knowing': 'https://github.com/blackwell-systems/knowing'}

meta = {}
repos = sorted({a['repo'] for a in adopters})
for i in range(0, len(repos), 40):
    parts = [f'r{j}: repository(owner: {json.dumps(r.split("/")[0])}, name: {json.dumps(r.split("/")[1])}) {{ nameWithOwner stargazerCount owner {{ __typename }} }}' for j, r in enumerate(repos[i:i + 40])]
    out = subprocess.run(['gh', 'api', 'graphql', '-f', 'query=query { ' + ' '.join(parts) + ' }'], capture_output=True, text=True).stdout
    d = (json.loads(out).get('data') or {}) if out else {}
    for j, r in enumerate(repos[i:i + 40]):
        if d.get(f'r{j}'):
            meta[r] = d[f'r{j}']

def stars(a): return (meta.get(a['repo']) or {}).get('stargazerCount', 0)
def otype(a): return ((meta.get(a['repo']) or {}).get('owner') or {}).get('__typename', '')

unique = {a['repo'].lower() for a in adopters}
owners = {a['repo'].split('/')[0].lower() for a in adopters}
extra = data.get('without_public_repo', [])
per = collections.Counter(a['project'] for a in adopters)

with open(os.path.join(ROOT, 'docs', 'adopters.csv'), 'w', newline='') as f:
    w = csv.writer(f, lineterminator='\n')
    w.writerow(['project', 'repository', 'owner_type', 'stars', 'category', 'how_used', 'evidence', 'verified'])
    for a in sorted(adopters, key=lambda a: (ORDER.index(a['project']), a['repo'].lower())):
        w.writerow([a['project'], a['repo'], otype(a), stars(a), a['category'], a['how'], a['evidence'], data['verified']])

md = ['# Adopters', '',
      f"Third-party repositories that use Blackwell Systems projects, each verified by opening the file listed under Evidence. Last verified {data['verified']}.", '',
      f"**{len(unique)} repositories across {len(owners)} organizations and developers**, plus {len(extra)} adopters without a public repository "
      f"({', '.join(e['name'] for e in extra)}).", '',
      '| Project | Repositories |', '|---|---|']
md += [f"| [{p}]({LINKS[p]}) | {per[p]} |" for p in ORDER if per[p]]
md += ['', 'Counted: direct use in code, dependency manifests, MCP and editor configs, CI, containers, packaging, and vendored skills. '
       'Not counted: our own repositories, forks, copies of an adopting project, packages that arrive only indirectly through another dependency '
       '(lockfile-only), catalogs and awesome lists, documentation-only mentions, and unrelated projects that share a name. '
       'The full method and scripts are in [`adoption/`](../adoption/).', '']
for p in ORDER:
    rows = [a for a in adopters if a['project'] == p]
    if not rows:
        continue
    named = [a for a in rows if not a.get('individual')]
    people = [a for a in rows if a.get('individual')]
    md += [f'## {p}', '', '| Repository | Stars | How it is used | Evidence |', '|---|---|---|---|']
    md += [f"| [{a['repo']}](https://github.com/{a['repo']}) | {stars(a):,} | {a['how']} | `{a['evidence']}` |" for a in sorted(named, key=lambda a: (-stars(a), a['repo'].lower()))]
    if people:
        md += [f"| Individual developers ({len(people)}) | | Personal setups: dotfiles, homelab and Nix configurations | |"]
    md.append('')
if extra:
    md += ['## Adopters without a public repository', '', '| Project | Adopter | How it is used |', '|---|---|---|']
    md += [f"| {e['project']} | {('[' + e['name'] + '](' + e['url'] + ')') if e['url'] else e['name']} ({e['organization']}) | {e['how']} |" for e in extra]
    md.append('')
md += ['Using one of these projects? Open an issue or pull request on the project\'s repository and it will be added here.', '']
open(os.path.join(ROOT, 'docs', 'ADOPTERS.md'), 'w').write('\n'.join(md))
print(f"{len(unique)} repos, {len(owners)} owners, {len(extra)} without a public repo; wrote docs/ADOPTERS.md and docs/adopters.csv")
