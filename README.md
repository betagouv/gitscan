# GitScan

![GitScan workflow status](https://github.com/revolunet/gitscan/actions/workflows/scan.yaml/badge.svg?branch=main)

Automated GitHub public repository scanner. Collects metadata, documentation, dependencies, and commit history from public repositories. Optionally generates AI-powered structured overviews.

Edit [orgas.txt](./orgas.txt) and activate github pages to get your own for free.

## Overview

This GitScan monitors many **French GitHub organizations** public repos.

You can change that in [./orgas.txt](./orgas.txt)

## What It Extracts

For each repository:

- **README.md** and **CHANGELOG.md**
- **Dependencies**: `package.json`, `requirements.txt`, `pyproject.toml`
- **Docker configs**: `compose.yml`, `docker-compose.yml`
- **Commit history**: Last 90 days
- **File tree**: Compressed directory structure
- **GitHub metadata**: Languages, topics, issues count, etc.
- **AI Overview** (optional): Structured JSON with description, features, tech stack, and more
- **AI Changelog** (optional): human-friendly changelog from commits

## Data Structure

```
repos/
├── {org-name}/
│   ├── repos.json          # All org repositories metadata
│   ├── repos.txt           # Clone URLs list
│   └── {repo-name}/        # Per-repository data
│       ├── README.md
│       ├── github.json
│       ├── commits.txt
│       ├── tree.txt
│       ├── package.json
│       └── overview.json   # AI-generated structured overview
└── ...
```

## Usage

See the GitHub workflows

## AI Overview Schema

See [./schemas/repository.schema.json](./schemas/repository.schema.json)

The `overview.json` files follow a [JSON Schema](./schemas/repository.schema.json) with fields including:

| Field          | Description                                           |
| -------------- | ----------------------------------------------------- |
| `description`  | Concise project description (in French)               |
| `language`     | Primary programming language                          |
| `features`     | User-facing features and capabilities                 |
| `audience`     | Target users (public, professionals, admin agents...) |
| `dependencies` | Main frameworks, libraries, and services              |
| `components`   | Technical architecture components                     |
| `auth`         | Authentication methods and providers                  |
| `tests`        | Testing setup and frameworks                          |
| `workflows`    | CI/CD workflows                                       |
| `status`       | Maintenance status (active, archived, deprecated...)  |
| `license`      | SPDX license identifier                               |
| `metrics`      | Stars, forks, contributors, open issues               |
| `tags`         | Keywords for categorization                           |

## GitHub Actions

The workflow runs daily at midnight UTC and can be triggered manually.

**Features:**

- Automatic scheduling with smart prioritization (new/outdated repos first)
- Parallel scanning (up to 3 repositories at a time)
- Auto-commits results back to the repository

**Manual trigger:** Go to Actions → "Scan repos" → Run workflow

## License

MIT
