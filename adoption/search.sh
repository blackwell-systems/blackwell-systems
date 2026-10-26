#!/usr/bin/env bash
# Run every query in queries.tsv against GitHub code search and write raw hits to raw.tsv
# (project, repository, path, query). Requires an authenticated `gh` CLI. Code search allows
# about 10 requests a minute, so a full run takes several minutes.
set -euo pipefail
here="$(cd "$(dirname "$0")" && pwd)"
out="$here/raw.tsv"
: > "$out"
while IFS=$'\t' read -r project query; do
  [ -z "$project" ] && continue
  for page in $(seq 1 10); do
    res=$(gh api -X GET search/code -f q="$query" -f per_page=100 -f page="$page" \
      --jq '.items[] | "\(.repository.full_name)\t\(.path)"' 2>/dev/null || true)
    sleep 7
    [ -z "$res" ] && break
    printf '%s\n' "$res" | awk -v p="$project" -v q="$query" -F'\t' '{print p"\t"$1"\t"$2"\t"q}' >> "$out"
    [ "$(printf '%s\n' "$res" | wc -l)" -lt 100 ] && break
  done
done < "$here/queries.tsv"
echo "$(wc -l < "$out") hits written to raw.tsv"
