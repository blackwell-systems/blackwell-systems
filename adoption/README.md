# Adoption count

How the "used by" figures on this profile are produced, so anyone can check or reproduce them. The published list is [docs/ADOPTERS.md](../docs/ADOPTERS.md) (also as [CSV](../docs/adopters.csv)).

## Steps

1. **Search.** `adoption/search.sh` runs every query in `queries.tsv` against GitHub code search: package manifests (npm, Go, PyPI, NuGet, Cargo), MCP and editor configurations, CI workflows, Dockerfiles, Nix and Gentoo packaging, and vendored agent-lsp skills. Raw hits go to `raw.tsv`.
2. **First-pass sort.** `adoption/verify.py` drops repositories already listed, then excludes our own repositories, forks, copies of an adopting project, lockfile-only appearances (a package that arrives indirectly through another dependency), catalogs and awesome lists, and documentation-only mentions. It opens the remaining files and keeps those with project-specific evidence as candidates in `candidates.json`.
3. **Human review.** Each candidate is checked by hand, because names collide (other tools called agent-lsp or ClaudeWatch, Google Cloud Functions also abbreviated GCF). Confirmed adopters are added to `adopters.yaml` with the file that proves it.
4. **Render.** `adoption/render.py` turns `adopters.yaml` into the published list with current star counts.

The search can also be cross-checked against GitHub's dependency graph ("Used by" on each package repository).

## Rules

- Count a repository once, however many of our projects it uses.
- Count direct use only. A package that appears only in a lockfile came in through something else and is reach, not adoption.
- Copies and forks of an adopting project count once, as the original.
- Personal setups (dotfiles, homelab, personal Nix configs) count, and are shown as a group rather than named.
- An adopter with no public repository is listed separately and not counted as a repository.

## Requirements

An authenticated [GitHub CLI](https://cli.github.com/) (`gh auth login`), Python 3, and PyYAML (`pip install pyyaml`).
