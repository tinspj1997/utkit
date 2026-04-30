# Package Development Guide

This section covers the workflow for developing and publishing utkit using uv.

## Upgrade the package in a project

To pull the latest published version of utkit into a project:

```bash
uv add utkit --upgrade
```

This updates utkit to the newest available version on PyPI and syncs the lockfile.

## Bump the version

Use `uv version` to increment the package version. For a minor release (e.g. 0.3.0 → 0.4.0):

```bash
uv version --bump minor
```

Other bump options:

| Command | Example result |
|---------|----------------|
| `uv version --bump patch` | 0.4.0 → 0.4.1 |
| `uv version --bump minor` | 0.4.0 → 0.5.0 |
| `uv version --bump major` | 0.4.0 → 1.0.0 |

This updates the version field in `pyproject.toml` automatically.

## Build the package

Compile the distribution artifacts (wheel + sdist):

```bash
uv build
```

Output is placed in the `dist/` folder:

```
dist/
  utkit-0.4.0-py3-none-any.whl
  utkit-0.4.0.tar.gz
```

## Full release workflow

```bash
# 1. Bump version
uv version --bump minor

# 2. Build distribution
uv build

# 3. Publish to PyPI
uv publish
```
