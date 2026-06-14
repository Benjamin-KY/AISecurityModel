# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

(No unreleased changes — `v2.1.0` is the most recent tagged release.)

## [2.1.0] — 2026-06-14

**Hygiene + relaunch.** No notebook content or `app.py` logic is changed in
this release. The course substance shipped in `v2.0` (15 notebooks, working
Gradio Space, real fine-tuning scripts, OWASP-mapped vulnerability taxonomy,
37 KB educator guide, ~6.5 MB training dataset) remains as-is. The goal here
is to make the repository honestly representable and properly licensed
before any further content work.

### Added

- `LICENSE` (Apache-2.0, for code) and `LICENSE-DOCS` (CC BY-SA 4.0, for
  course content). The repository had previously *claimed* dual-licensing
  in `README.md` but shipped neither file, leaving the project implicitly
  all-rights-reserved.
- `SECURITY.md` — threat model, out-of-scope clarifications (the vulnerable
  adapter being vulnerable is *not* a security bug), responsible-disclosure
  channel via GitHub Security Advisories, and explicit guidance for learners
  who find real vulnerabilities in production systems.
- `CONTRIBUTING.md` — pedagogical contract (vulnerable-then-educate framing
  is required), dual-licensing terms for PRs, Code of Conduct adapted from
  Contributor Covenant v2.1 with course-specific responsible-use clauses,
  per-release ship discipline, and a sibling-course reading order.
- `CITATION.cff` — CFF v1.2.0 citation metadata so the course can be cited
  in academic work without learners hand-rolling a BibTeX entry.
- `requirements-notebooks.txt` — full notebook-time dependency list derived
  from a per-notebook `import` audit. Previously the only requirements file
  was a 5-line Space-only manifest, which left notebooks 5–15 with
  silently-missing dependencies (`pandas`, `matplotlib`, `seaborn`,
  `streamlit`, `bitsandbytes`, `pytesseract`, `cryptography`, and others).
- `docs/development-history/` directory + index — historical record of the
  v2.0 build-out (formerly seven separate root-level planning documents).

### Changed

- `README.md` — full rewrite of the framing prose:
  - Dropped the "Production-Ready" / "Status: Complete" claims that
    overstated the maturity of an experimental educational tool.
  - Added a "Maturity & realistic scope" section with an honest per-notebook
    status (gold-standard / solid / pedagogically rough / scheduled for
    refactor) drawn from a cell-level audit on 2026-06-14.
  - Added a "Companion course" section that positions this repository as
    the **model and prompt layer** companion to
    [`harmless-harnesses`](https://github.com/Benjamin-KY/Harmless-Harnesses),
    which teaches the **structural-harness layer**.
  - Updated the License section to reference the actual `LICENSE` and
    `LICENSE-DOCS` files (was previously prose-only).
  - Updated the Citation block to point to `CITATION.cff`.
  - Updated the footer to `Version 2.1.0`, current date, and the honest
    "experimental educational tool" maturity label.
- `requirements.txt` — slimmed to a Space-only minimal manifest, with a
  one-line note pointing notebook users to `requirements-notebooks.txt`.
- `README_SPACE.md` — `license: mit` corrected to `license: apache-2.0`
  to match the actual repository license and remove a year-long
  contradiction between the Space metadata and the project README.

### Moved (kept in git history; no content rewritten)

Seven historical planning documents previously at the repository root were
relocated to `docs/development-history/`:

- `CLEANUP_STATUS.md`
- `IMPLEMENTATION_PLAN.md`
- `NOTEBOOKS_STATUS.md`
- `NOTEBOOK_RECOMMENDATIONS.md`
- `REMAINING_WORK_TODO.md`
- `SPACE_SETUP.md`
- `TEST_REPORT.md`

These remain valuable as the build-out journal of v2.0 but were creating
the impression of an unmaintained AI-generated planning dump at the root
of the repository. The `docs/development-history/README.md` indexes them
and notes that any claims they make about completeness are superseded by
the current `README.md` and this changelog.

### Known issues (carried forward, scheduled)

- **Notebooks 13, 14, 15** ship with 6–9 monolithic code cells of
  130–173 lines each. The code itself is real and runnable, but the
  pedagogical structure is poor (learners cannot step through
  incrementally). Phase 3 of the multi-session overhaul will refactor
  these to match notebook 7's cell-level granularity.
- **No real CI.** The previous `TEST_REPORT.md` claim of "100% passed"
  reflected JSON-syntax validation of notebook files, not execution.
  Phase 2 will add `nbval-lax` CI for at least notebooks 1, 2, and 7
  on CPU, with `nbqa` lint and `nbformat` validation.
- **Open PR #1** (Colab T4 bfloat16 fix) has scope-creep beyond the
  documented fix and is pending a focused re-do in a follow-up release.
- **Content currency.** Course content is 2025-vintage. Phase 4 will
  add notebooks for 2026 surfaces (agent / MCP tool misuse, RAG-layer
  injection, the harness-paradigm capstone) and refresh existing
  notebooks for post-Skeleton-Key defences and constitutional
  classifiers.

## [2.0.0] — 2025-11-05

Initial 15-notebook curriculum, Gradio Space, fine-tuning scripts, and
training data. See `docs/development-history/` for the build-out journal.
No prior changelog was maintained; this entry is a placeholder for
historical continuity.

[Unreleased]: https://github.com/Benjamin-KY/AISecurityModel/compare/v2.1.0...HEAD
[2.1.0]: https://github.com/Benjamin-KY/AISecurityModel/compare/v2.0.0...v2.1.0
[2.0.0]: https://github.com/Benjamin-KY/AISecurityModel/releases/tag/v2.0.0
