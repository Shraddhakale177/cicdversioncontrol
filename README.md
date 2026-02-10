# Simple Python CI/CD Sample

This repo demonstrates a minimal Python application with a fully automated CI workflow. Key goals:

- Keep the app extremely focused so the pipeline logic stays easy to follow.
- Enforce a branching strategy and review guardrails before merging to main.

## What is included

1. src/app.py: a tiny CLI that prints a greeting.
2. 	ests/test_app.py: a single pytest check so CI can verify functionality.
3. .github/workflows/ci.yml: the pipeline that installs dependencies and runs the test suite.
4. docs/branching.md: explains how to work with branches, protect main, and require reviews.

Run the app with python -m src.app YourName, and run the tests locally via pytest.
