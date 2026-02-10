# Simple Python CI/CD Sample

This repo demonstrates a minimal Python application with a fully automated CI workflow. Key goals:

- Keep the app extremely focused so the pipeline logic stays easy to follow.
- Enforce a branching strategy and review guardrails before merging to main.

## What is included

1. `src/app.py`: a tiny CLI that prints a greeting.
2. `tests/test_app.py`: the pytest check that keeps the pipeline honest.
3. `.github/workflows/ci.yml`: installs dependencies and runs the suite on every push/PR.
4. `docs/branching.md`: explains how to work with feature branches and guard `main`.

Run the app with `python -m src.app YourName` (defaults to `developer`) and run the focused test with `pytest tests/test_app.py` before pushing.
