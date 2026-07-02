# CI/CD pipeline demo — for qtop challenge #433

This repo demonstrates the CI/CD structure proposed for [qtop challenge #433](https://github.com/qtop/qtop/issues/433).

## Structure

- `Makefile` — shared entry point for local and CI runs
- `requirements-ci.txt` — pinned CI dependencies
- `.github/workflows/ci.yml` — GitHub Actions, actions pinned to full commit SHAs
- `.gitlab-ci.yml` — GitLab CI mirror, shares same Makefile targets
- `fortifications` — eval ban + control char detection (script in `tools/`)
- DCO sign-off enforced

## How it works

Both CI systems call the same `make ci` → `make test lint`, ensuring they never drift.
Artifacts are uploaded for review. Python 3.6 compat is covered via AlmaLinux 8 container.
