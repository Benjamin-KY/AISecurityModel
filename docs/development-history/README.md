# Development history

This directory holds the build-out journal of `AISecurityModel` v2.0
(October–November 2025). All seven files here were previously at the
repository root, where they created the impression of an unmaintained
planning dump. They are preserved verbatim — not rewritten — as
historical record.

**Anything these files claim is superseded by the current `README.md` and
`CHANGELOG.md` at the repository root.** Where they say "production-ready"
or "100% complete", treat that as the v2.0 release-narrative pose and
read the current README for the honest maturity assessment.

## File map

| File | Authored | What it is |
|---|---|---|
| `IMPLEMENTATION_PLAN.md` | 2025-10-27 | The initial sprint plan for finishing the 15-notebook curriculum. Useful as a record of the original scope intent. |
| `NOTEBOOK_RECOMMENDATIONS.md` | 2025-10-27 | A 429-line analysis of which notebook stubs needed substance and what each should cover. The honest version of where things stood mid-build. |
| `NOTEBOOKS_STATUS.md` | 2025-10-27 → 2025-11-05 | A running status board of which of the 15 notebooks were complete, in-progress, or template-only at various points in the v2.0 sprint. |
| `REMAINING_WORK_TODO.md` | 2025-11-04 | The final TODO list at the end of the v2.0 push, including known gaps (troubleshooting sections, exercise variations, learning-outcomes cells) that did not land before tag. Phase 3 of the overhaul addresses these. |
| `CLEANUP_STATUS.md` | 2025-11-05 | Tracking doc for the file-renames and content-consolidation done during the v2.0 finalisation. |
| `SPACE_SETUP.md` | 2025-11-04 | One-shot operational notes for setting up the Hugging Face Space. Superseded by `README_SPACE.md` at the repo root for ongoing use. |
| `TEST_REPORT.md` | 2025-11-05 | Claimed "100% passed" was JSON-syntax validation of notebook files, *not* notebook execution. Phase 2 of the overhaul is adding real CI (`nbval-lax`, `nbqa`, `nbformat` validation). |

## Why keep them?

Two reasons:

1. **Honesty about the build path.** The v2.0 sprint genuinely produced
   real artefacts (15 notebooks, a working Space, a 37 KB educator guide,
   real fine-tuning scripts). The planning documents are the audit trail
   of that work and would mislead readers if deleted with no replacement.
2. **Reusable shape.** The structure of `NOTEBOOK_RECOMMENDATIONS.md` and
   `REMAINING_WORK_TODO.md` is a reasonable template for tracking future
   curriculum-expansion sprints — instructors forking this course for
   their own institutions may find them useful as a planning shape.

## What replaced them at the root

- `README.md` — honest current-state course overview and per-notebook
  maturity table.
- `CHANGELOG.md` — release-by-release narrative starting at v2.1.0.
- `SECURITY.md` — threat model and responsible-disclosure policy.
- `CONTRIBUTING.md` — pedagogical contract and Code of Conduct.
- `CITATION.cff` — machine-readable citation metadata.

For the overhaul roadmap (Phases 1–5), see the maintainer's session
notes; the public surface tracks progress via `CHANGELOG.md` and
release notes.
