# Branching & Collaboration Guidelines

1. **Branching strategy**
   - Keep main (or master if that is the default you already use) protected and reserved for deploy-ready code.
   - Work on named feature/bugfix branches off of main, e.g., eature/add-hello-logging or ix/validate-inputs.
   - Merge feature branches back into main only through pull requests once the work is verified.

2. **Small, frequent commits**
   - Make each commit focus on one logical change to keep diffs readable.
   - Push often and break large tasks into multiple branches instead of one giant commit.
   - Use descriptive commit messages so reviewers and history stay easy to navigate.

3. **Branch protection rules**
   - Enable protection on main to block direct pushes from everyone but automated processes.
   - Require the CI workflow (the CI job under .github/workflows/ci.yml) to pass before any merge.
   - Restrict who can dismiss reviews and require the branch to be up to date before merging.

4. **Code reviews before merging**
   - All pull requests targeting main must have at least one approving review.
   - Reviewers should rely on the lightweight CI feedback plus a quick manual inspection for logic/style.
   - Address any requested changes with new commits so reviewers can confirm fixes in CI outputs.

Following these guardrails keeps the repo stable while staying lean and easy to understand. We can expand this doc later as the workflow evolves.
