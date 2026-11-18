# Repository Guidelines

At the start of every chat about this repository, read `AGENTS.md` and the current Don task context file, `DON_CURRENT_TASK.md` at the repository root. Treat the latter as additional, Don-specific context for planning and handoffs; keep it updated when the assigned checkpoint work changes.

## Project Structure & Module Organization

This repository analyzes EIU democracy scores alongside HDI/IHDI measures. Source CSV snapshots and `build_data.py` live at the root; generated tables and audits belong in `data/` and are ignored or maintained there as documented.

Exploratory notebooks and figures are in `Checkpoint 4 - EDA/`; acquisition material is in `Checkpoint 3 - Data Acquisition/`; documentation is in `Checkpoint 5 - Data Documentation/`. Read `README.md` and `DATASHEET.md` before changing sources or interpretations.

## Interactive Checkpoint Workflow

At each checkpoint, inspect the assignment materials, repository state, and `intake_NOCOMMIT/` for deliverables and feedback. Use those notes for planning, but never commit files from that directory. Fairly divide work among Don, Sai, and Daniel, record ownership, review one another’s work, and ensure each member makes a meaningful commit when required.

### Preserve Existing Work

Before removing, replacing, or substantially rewriting existing user-authored content—including notebook cells, prose, figures, or code—ask the user for explicit approval. Prefer additive changes and preserve exploratory notes unless the user specifically authorizes their removal. If a replacement is necessary, first identify the exact affected content and offer to retain it alongside the new work.

For narrative checkpoints, connect claims to reproducible evidence, uncertainty, limitations, polished figures, and checks of alternative explanations. Keep decisions interactive when research questions, analyses, or ownership are ambiguous.

Plan with slack: data-science tasks routinely take longer than their initial estimates because analysis, debugging, interpretation, and figure revisions interact. Set an internal finish target at least half a day before the official deadline, reserve time for integration and review, and treat stretch analyses as optional until the required deliverables are complete.

## Build, Test, and Development Commands

Most work happens in notebooks, Markdown, and figures; do not run the data-building script for every checkpoint. Run it from the repository root with Python 3.9+ when source data, cleaning logic, or generated tables change:

```sh
python3 build_data.py
```

This verifies hashes and schemas, validates values, performs joins, and regenerates tables and audits. Do not run it merely to refresh unchanged outputs. The older acquisition script is historical support only.

There is no automated test suite. When relevant, use a successful rebuild and `data/audit.md` review as the smoke test. Otherwise, rerun affected notebooks, verify figures and README references, and trace reported numbers to code.

## Coding Style & Naming Conventions

Use Python 4-space indentation, `snake_case`, descriptive columns, explicit validation, and deterministic sorting. Do not hand-edit generated outputs. Place derived figures under `Checkpoint 4 - EDA/figures/`.

Add concise “why” comments for non-obvious code, analytical checks, or implementation choices. Explain the reason for the step rather than restating what the code already says.

## Commit & Pull Request Guidelines

Use short checkpoint-scoped commit subjects (for example, `updating draft of datadoc`). Pull requests should explain research impact, list changed files, note provenance or licensing changes, identify reviewers, and include visual previews when useful.

## Data and Configuration Safety

Document source-version, schema, access-date, and licensing changes in the datasheet and manifest. Treat EIU-derived values as restricted. Never commit secrets, notebook checkpoints, or `intake_NOCOMMIT/` files; inspect that directory only for requirements and feedback.
