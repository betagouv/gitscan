# Agent Skills

A collection of skills for AI coding agents. Skills are packaged instructions and scripts that extend agent capabilities.

Skills follow the [Agent Skills](https://agentskills.io/) format.

## Available Skills

### rgaa-html-css

RGAA HTML/CSS accessibility compliance skill. Contains ~98 rules across 13 categories covering page structure, forms, images, keyboard accessibility, and more.

**Use when:**
- Writing or reviewing HTML templates and components
- Generating frontend markup that must comply with RGAA
- Auditing existing pages for accessibility issues
- Fixing accessibility bugs in HTML/CSS

**Categories covered:**
- Page Structure and Landmarks (Critical)
- Images, SVG, and Icons (Critical)
- Forms (Critical)
- Keyboard Accessibility (Critical)
- Links and Buttons (High)
- Tables (High)
- CSS Usage and Content Robustness (High)
- HTML Validity and Semantics (High)
- Language (High)
- Page Title (High)
- Lists (Medium)
- Iframes (Medium)
- Additional Conformity Rules (Medium)

## Installation

All skills:
```bash
npx skills add SocialGouv/skills
```

RGAA HTML/CSS only:
```bash
npx skills add SocialGouv/skills/skills/rgaa-html-css
```

## Usage

Skills are automatically available once installed. The agent will use them when relevant tasks are detected.

**Examples:**
```
Review this page for RGAA compliance
```
```
Fix the accessibility issues in this form
```
```
Generate an accessible navigation component
```

## Skill Structure

Each skill contains:
- `SKILL.md` - Instructions for the agent
- `rules/` - Individual rule files with code examples
- `reference/` - Supporting documentation (optional)

## Development

See [packages/skills-build/](packages/skills-build/) for the build system that compiles individual rule files into `AGENTS.md`.

### Setup

```bash
pnpm install
```

This installs dependencies and automatically configures the pre-commit hook that rebuilds `AGENTS.md` when rule files change.

### Build & Validate

```bash
pnpm build-agents --all          # Build all skills
pnpm build-agents --skill=rgaa-html-css  # Build rgaa skill only
pnpm validate --all              # Validate all rule files
```

## License

MIT
