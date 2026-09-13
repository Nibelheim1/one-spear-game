# Publish to GitHub

This project is ready to publish as a static repository. `index.html` is the complete playable build.

Recommended repository name: `one-spear-game`

If GitHub CLI is authenticated on your machine, run from this directory:

```bash
bash scripts/publish_github.sh
```

The script creates a **private** repository by default. To create a public repository instead:

```bash
VISIBILITY=public bash scripts/publish_github.sh
```

Requirements: `git` and GitHub CLI (`gh`) with `gh auth status` succeeding.
