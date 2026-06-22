# Project Memory

Claude Code reads this file automatically at the start of every run. It is the
loop's memory and rulebook. Keep it accurate — everything here shapes the loop.

## Project Overview

A small Python project. The loop's job: find failing pytest runs from the last
24 hours, draft a fix for each, have the verifier subagent check it, and open a
**draft** Pull Request for human review. Nothing merges without a human.

## Stack & Commands

- **Python:** 3.11+
- **Run tests:** `pytest -x --tb=short`
- **Install dev deps:** `pip install -e ".[dev]"`

## Project Layout

```
hello.py        # the module under test
test_hello.py   # pytest checks
```

## Loop Rules

1. Never push to `main`. Always work on a `loop/fix-<slug>` branch.
2. Open PRs as **drafts**, labeled `loop-proposed`. Never merge your own PR.
3. Fix the narrowest surface that resolves the failure. Touch at most 3 files.
4. Never modify dependency versions in `pyproject.toml`.
5. Never delete a test or add `pytest.mark.skip` / `# noqa` without a comment.
6. Run the test suite before opening a PR. If it still fails, open the PR anyway
   with the failure noted in the body, labeled `loop-needs-human`.
7. Cap each run at 3 fixes to limit cost and blast radius.

## Known Failure Patterns

<!-- Add patterns as the loop encounters them. Each entry prevents re-discovery. -->

## Run Log

<!-- The loop appends one line per run. Do not edit by hand. -->
<!-- FORMAT: YYYY-MM-DD | N triaged | N PRs | N skipped | note -->
