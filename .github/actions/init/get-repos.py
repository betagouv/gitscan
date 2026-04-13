import os
import json
import sys
from urllib.parse import urlparse
from datetime import datetime, timezone, timedelta
import re

STALE_DAYS = 30


# get list of repos to analyze based on orgas.txt
# prioritizes repos that have been updated on GitHub since last local analysis

repos_folder = os.path.abspath("./repos")


def load_pushed_at_map(orgas):
    """Load pushed_at timestamps from repos.json files, keyed by clone_url."""
    pushed_at_map = {}
    for orga in orgas:
        repos_json_path = os.path.join(repos_folder, orga, "repos.json")
        if not os.path.isfile(repos_json_path):
            continue
        try:
            with open(repos_json_path) as f:
                repos_data = json.load(f)
            for repo in repos_data:
                clone_url = repo.get("clone_url")
                pushed_at = repo.get("pushed_at") or repo.get("updated_at")
                if clone_url and pushed_at:
                    dt = datetime.fromisoformat(pushed_at.replace("Z", "+00:00"))
                    pushed_at_map[clone_url] = dt.timestamp()
        except Exception as e:
            print(f"error loading {repos_json_path}: {e}", file=sys.stderr)
    return pushed_at_map


def get_scanned_pushed_at(local_path):
    """Return the pushed_at timestamp stored in the local github.json, or None."""
    github_json = os.path.join(local_path, "github.json")
    if not os.path.isfile(github_json):
        return None
    try:
        with open(github_json) as f:
            data = json.load(f)
        pushed_at = data.get("pushed_at")
        if pushed_at:
            dt = datetime.fromisoformat(pushed_at.replace("Z", "+00:00"))
            return dt.timestamp()
    except Exception:
        pass
    return None


urls = []

orgas = [
    orga.strip() for orga in open(os.path.join("./orgas.txt")).readlines() if len(orga)
]

# Build mapping of clone_url -> pushed_at timestamp from GitHub API data
pushed_at_map = load_pushed_at_map(orgas)


def get_repo_path(url):
    parsed = urlparse(url)
    path = parsed.path.strip("/")
    path = re.sub(".git$", "", path)
    segments = [s for s in path.split("/") if s]
    path = f"{segments[-2]}/{segments[-1]}"
    return path


def get_repo_local_path(url):
    return f"{repos_folder}/{get_repo_path(url)}"


exclude_repos = set(
    r.strip() for r in os.environ.get("EXCLUDE_REPOS", "").split(",") if r.strip()
)

for orga in orgas:
    repos_file = os.path.join(repos_folder, orga, "repos.txt")
    if os.path.isfile(repos_file):
        urls.extend(line.strip() for line in open(repos_file) if line.strip())

# Filter out excluded repos
if exclude_repos:
    before = len(urls)
    urls = [u for u in urls if get_repo_path(u) not in exclude_repos]
    excluded = before - len(urls)
    if excluded:
        print(f"Excluded {excluded} repos: {', '.join(exclude_repos)}", file=sys.stderr)

# Filter out repos that are already scanned and have not been pushed to in STALE_DAYS days
stale_cutoff = (datetime.now(timezone.utc) - timedelta(days=STALE_DAYS)).timestamp()
before = len(urls)
urls = [
    u for u in urls
    if pushed_at_map.get(u, 0) >= stale_cutoff          # active recently, OR
    or not os.path.exists(get_repo_local_path(u))        # not yet scanned
]
stale_count = before - len(urls)
if stale_count:
    print(f"Skipped {stale_count} repos with no activity in the last {STALE_DAYS} days", file=sys.stderr)


# Sort URLs:
#   0 — unscanned (no local github.json): sorted by pushed_at desc
#   1 — outdated (github pushed_at > scanned pushed_at): sorted by pushed_at desc
#   2 — up-to-date: sorted by pushed_at desc (backfill, most active first)
def get_sort_key(url):
    local_path = get_repo_local_path(url)
    github_pushed_at = pushed_at_map.get(url, 0)
    if not os.path.exists(local_path):
        return (0, -github_pushed_at)
    scanned_pushed_at = get_scanned_pushed_at(local_path)
    if scanned_pushed_at is None or github_pushed_at > scanned_pushed_at:
        return (1, -github_pushed_at)
    return (2, -github_pushed_at)


# Cache sort keys to avoid redundant filesystem reads
sort_key_cache = {url: get_sort_key(url) for url in urls}

sorted_urls = sorted(urls, key=lambda u: sort_key_cache[u])

# Take only the first N URLs (from input)
matrix_count = int(sys.argv[1])
matrix_urls = sorted_urls[:matrix_count]

# Log summary
new_count = sum(1 for u in urls if sort_key_cache[u][0] == 0)
updated_count = sum(1 for u in urls if sort_key_cache[u][0] == 1)
unchanged_count = sum(1 for u in urls if sort_key_cache[u][0] == 2)
print(
    f"Repos: {len(urls)} total, {new_count} unscanned, {updated_count} outdated, {unchanged_count} up-to-date",
    file=sys.stderr,
)
selected_priority = sum(1 for u in matrix_urls if sort_key_cache[u][0] <= 1)
selected_backfill = sum(1 for u in matrix_urls if sort_key_cache[u][0] == 2)
print(
    f"Selected: {len(matrix_urls)} repos ({selected_priority} unscanned/outdated, {selected_backfill} backfill)",
    file=sys.stderr,
)

# Output the matrix JSON to GITHUB_OUTPUT
urls_json = json.dumps(
    [{"url": url, "full_name": get_repo_path(url)} for url in matrix_urls]
)

print(urls_json)
