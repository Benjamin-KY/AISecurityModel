# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

(No unreleased changes — `v2.4.1` is the most recent tagged release.)

## [2.4.1] — 2026-06-15

**Audit-discipline patch:** four leftover "15-notebook" / "6-notebook"
refs caught during the HuggingFace Space redeploy investigation. No
content or pedagogical changes. CI-clean.

### Fixed

- `requirements.txt` comment — "15-notebook course" → "18-notebook course".
- `requirements-notebooks.txt` comment — same.
- `README.md` project-structure tree comment — "15-notebook curriculum"
  → "18-notebook curriculum" (lines 9 and 461 were already corrected in
  v2.4.0; this catches the third occurrence on line 332 in the directory
  tree, which the v2.4.0 sweep missed).
- `.github/workflows/notebooks-ci.yml` lint-job comment — dropped the
  stale "15-notebook curriculum predates this CI" anchor (factually
  correct as historical narrative, but actively confusing to a 2026
  reader; replaced with "the notebook curriculum predates this CI"
  with no version anchor).

### Why a release for four comment-line fixes

Audit-discipline (`memory: audit discipline`): "When user says 'check
EVERYTHING' run a stale-ref grep across the whole tree — not just visible
README sections." These four refs would have remained visible to anyone
reading the Space requirements manifest, the Colab install instructions,
the directory layout, or the CI yml — three of the four primary surfaces
a new contributor touches in their first hour with the repo. Tagged as a
patch so the corrected versions are referenceable.

## [2.4.0] — 2026-06-15

**Phase 5 complete: strategic positioning, cross-repo coherence, and a
full educator-facing refresh.** No new notebooks and no notebook
restructuring this release; the substance is in docs, in the
HuggingFace Space description, in the educator guide expansion, and
in repo-wide Privacy-Act-reform consistency.

### Added

- `docs/POSITIONING.md` — strategic anchor doc explaining where this
  repository fits in the three-repo Kereopa-Yorke constellation
  (AISecurityModel = model-and-prompt layer with a bridge into the
  architectural layer; [`harmless-harnesses`](https://github.com/Benjamin-KY/Harmless-Harnesses)
  = architectural / harness layer; [`sa-sovereign-llm-harness`](https://github.com/Benjamin-KY/sa-sovereign-llm-harness)
  = research codebase + SA-GOV-BENCH evaluation methodology). Includes
  the explicit "what this repository IS / what it is NOT" contract, a
  two-layer ASCII architecture diagram, four reading paths, the IDSov
  boundary statement (verbatim positioning from
  `harmless-harnesses` F0 §6 and F2 §6, themselves verbatim from
  `sa-sovereign-llm-harness/docs/the-harness-paradigm.md` with author
  approval), and the two-paper research plan (paper #1 SA-GOV-BENCH
  empirical → NeurIPS 2027; paper #2 structural critique of the harness
  paradigm → FAccT 2027).
- `docs/READING_ORDER.md` — operational companion to `POSITIONING.md`
  with six audience-specific paths: Path A (self-paced learner, full
  curriculum, 50-70 h over 8-12 weeks), Path B (working engineer, fastest
  viable, ~16 h over 2 weeks), Path C (instructor with a 14-week
  combined-syllabus skeleton spanning both this repo and
  `harmless-harnesses`), Path D (researcher), Path E (regulator, with
  five concrete vendor-challenge prompts), Path F (executive 90-min
  briefing). Includes a prerequisite cheat sheet, a time-budget table,
  and a cross-repo hand-off table documenting six specific transitions
  between the three repositories.

### Changed

- `docs/EDUCATOR_GUIDE.md` — major expansion from v1.0 (921 lines,
  6-notebook coverage) to v2.0 (1162 lines, 18-notebook coverage).
  Added: new **Format 5 — 5-day intensive** spanning all 18 notebooks;
  full v1.0-style pedagogical treatment for the 2026 Architectural
  Capstone Track (nb16 Agent/MCP, nb17 RAG-layer prompt injection,
  nb18 Harness-Paradigm capstone) including key concepts, teaching
  tips, common issues, discussion prompts, and assessment ideas;
  condensed reference table for nb7-15 (since those notebooks already
  ship with prerequisites + try-it-yourself cells from the Phase 3
  refactor); Architectural / Harness Layer learning outcomes (4 new);
  Privacy Act references updated to post-2024-reform penalty figures
  throughout. Date stamp: 2026-06-15. Self-references updated to
  AISecurityModel v2.4.0+.
- `README_SPACE.md` — rewritten to match new positioning. Now declares
  the Space as the *attacks lab* half of the picture (with the
  architectural layer in the sibling course); 6-notebook references
  updated to 18 notebooks with three-track breakdown; Privacy Act
  references updated to post-2024-reform tiered penalties; the "this
  Space is part of a three-repo constellation" section added with
  per-repo role table and recommended reading path; IDSov boundary
  disclaimer added; "necessary, not sufficient" added to the disclaimer
  list (defending only at the prompt boundary does not eliminate harm —
  see nb16-18 and `harmless-harnesses`); citation year and author block
  corrected.
- `README.md` — line 9 corrected from "15 Jupyter notebooks" to
  **"18 Jupyter notebooks across three tracks"** with the foundational
  / advanced / 2026-architectural-capstone breakdown inline; Course
  Formats section updated: "University Course" now refers to all 18
  notebooks (with weighting guidance), "Corporate Training" extended
  from 3 days to **5 days** to cover nb16-18 + hand-off to
  `harmless-harnesses`; cross-link block added to `docs/POSITIONING.md`
  and `docs/READING_ORDER.md`.
- `app.py` — Gradio Space "Get Started" panel: notebook count corrected
  from 6 to 18 with three-track breakdown; educator-guide reference no
  longer cites the obsolete "70+ pages" figure (now "comprehensive
  guide, 5 course formats from 2 h workshop to 5-day intensive");
  citation block updated from `@software{aisecurityedu2025, ...
  author = {Benjamin-KY}, year = {2025}}` to
  `@software{aisecurityedu2026, ... author = {Kereopa-Yorke, Benjamin},
  year = {2026}}`; footer "Privacy Act 1988 Compliant" → "Privacy Act
  1988 context — post-2024 reform aware"; cross-link to
  `docs/POSITIONING.md` and the sibling course added.
- `scripts/merge_and_upload.py` — model-card boilerplate line corrected
  from "6 progressive Jupyter notebooks (beginner to advanced)" to
  "18 progressive Jupyter notebooks (foundational, advanced, 2026
  architectural capstone)".
- `notebooks/06_Defence_Real_World_Application.ipynb` — capstone
  banner reworded from *"CONGRATULATIONS! COURSE COMPLETE! You've
  completed all 6 notebooks"* to *"FOUNDATIONAL TRACK COMPLETE!
  You've completed the foundational track (notebooks 1-6)"*, which is
  the structurally accurate phrasing now that nb07-18 exist; one
  additional Privacy Act 1988 penalty-figure reference updated to
  post-2024-reform language (any remaining occurrences from v2.3.0
  were swept in this pass).
- `notebooks/11_Industry_Specific_Security.ipynb` — three Privacy Act
  1988 penalty-figure references updated to post-2024-reform tiered
  penalty language; these were missed in the v2.3.0 Phase 4 sweep
  (which restricted itself to nb06 to keep the release scope tight).
- `notebooks/15_Incident_Response_Forensics.ipynb` — Privacy Act 1988
  penalty-figure references updated to post-2024-reform tiered penalty
  language; course-journey hand-off prose updated to reference the
  18-notebook structure and the bridge into `harmless-harnesses`.
- `CITATION.cff` — version `2.3.0` → `2.4.0`; date `2026-06-14` →
  `2026-06-15`; abstract rewritten end-to-end to describe the
  18-notebook three-track structure, the post-Dec-2024 Privacy Act
  reform, the Voluntary AI Safety Standard, the new
  `POSITIONING.md` / `READING_ORDER.md` strategic docs, and the
  educator guide's five course formats.

### Strategic context

This release closes the gap identified in the original Phase 1
positioning audit: the repo previously read as a standalone
"AI security course" with no signal that it sits inside a wider
research and curriculum constellation. After v2.4.0:

- A learner landing on the README gets pointed to the right next
  repository for their goal (architectural layer →
  `harmless-harnesses`; research evidence →
  `sa-sovereign-llm-harness`).
- An instructor adopting this course gets a 14-week combined-syllabus
  skeleton spanning both this repo and `harmless-harnesses`, with a
  clear hand-off point.
- A regulator gets five concrete vendor-challenge prompts grounded in
  the post-Dec-2024 Australian regulatory landscape.
- An executive can get the 90-min briefing path that ends with a clear
  build/buy/govern decision.

The release deliberately does **not** rename the repository (still
`AISecurityModel`) — that remains a deferred user decision and would
break inbound HuggingFace and academic citations if done unilaterally.

### Not in this release (carried forward)

- No notebook structural changes, no new attack/defence content, no
  CI/CD changes, no model retraining. Phase 5 is documentation and
  positioning only; the substance shipped in v2.1.x (test
  infrastructure), v2.2.x (notebook pedagogical refactor), and v2.3.0
  (2026 modernisation + capstone track).
- `data/training_data.jsonl` and `data/vulnerability_taxonomy.json`
  still contain pre-reform Privacy Act figures embedded in the
  training data itself. These were intentionally not touched in this
  release: retraining the vulnerable model is out of scope for a
  documentation release, and altering the taxonomy mid-cycle would
  invalidate cross-references in already-shipped notebooks. A future
  v3.x training-data refresh will sweep these.
- The repo rename remains deferred to user. Plan explicitly says "do
  not initiate without explicit user request."

## [2.3.0] — 2026-06-14

**Phase 4 complete: 2026 modernisation.**
Three new architectural-defence notebooks (16, 17, 18) form a capstone track
on top of the existing 15-notebook model-and-prompt-layer course. Existing
notebooks 4, 5, 6 receive surgical 2026 updates (not full refactors). One
factually-incorrect figure in nb06 (Privacy Act penalty ceiling) is corrected
in place; the rest of v2.3.0 is additive.

### Added

- `notebooks/16_Agent_MCP_Security.ipynb` — agent and tool-misuse security:
  tool-calling agents, MCP servers, indirect prompt injection via tool
  outputs, confused-deputy / over-privileged-tool patterns, cross-tool
  data exfiltration, tool-allowlist defences.
- `notebooks/17_RAG_Injection_Security.ipynb` — RAG-layer prompt injection:
  document poisoning in retrieval indices, retrieved-context attacks
  (where the model never sees an attacker prompt directly), source
  provenance and trust scoring, citation enforcement as a defence
  primitive, why output-filtering defences from notebook 6 don't help here.
- `notebooks/18_Harness_Paradigm_Capstone.ipynb` — capstone synthesis:
  reframes notebooks 1-17 as the *model-and-prompt* layer; introduces
  the **harness paradigm** of architectural defences around (not inside)
  the model; builds a 4-component `GovernanceHarness` (source registry,
  router, verifier, decision logger); runs two ablation studies showing
  which component fails what (authority-ablation: blog-rant slips
  through when `min_trust` is dropped; enforcement-ablation: a
  `ForgingHarness` that emits fabricated citations is caught by the
  verifier when enforcement is on, slips through when it's off);
  explicit hand-off to [`harmless-harnesses`](https://github.com/Benjamin-KY/Harmless-Harnesses)
  for the full course on harness design; Indigenous-data-sovereignty
  positioning of the paradigm work.
- `notebooks/04_Advanced_Jailbreaks_Skeleton_Key.ipynb` — appended
  *"2026 Update: Successor Attack Families"* covering many-shot
  jailbreaking (Anthropic Apr 2024 → matured 2025), Crescendo
  (Microsoft Research Apr 2024 → mainstream 2025), and the
  architectural-bypass families (indirect prompt injection via tool
  outputs → notebook 16; RAG poisoning → notebook 17).
- `notebooks/05_XAI_Interpretability_Inside_Model.ipynb` — appended
  *"2026 Update: Interpretability-Driven Defences in Production"*
  covering Anthropic's Constitutional Classifiers (Feb 2025), feature
  steering / activation patching as a defence layer, and
  interpretability-as-a-service vendors (Goodfire / Transluce / Decode
  Research, 2025-2026).
- `notebooks/06_Defence_Real_World_Application.ipynb` — appended
  *"2026 Update: Australian AI Regulatory Landscape"* documenting the
  **Privacy and Other Legislation Amendment Act 2024** (assented 10 Dec
  2024), the **Voluntary AI Safety Standard** (Sept 2024) and its
  10 guardrails, the anticipated mandatory-guardrails regime for
  high-risk AI settings, and the still-in-force 8 AI Ethics Principles.

### Changed

- `notebooks/06_Defence_Real_World_Application.ipynb` — corrected the
  Privacy Act 1988 penalty ceiling figure in 7 locations (text,
  data-structures, assessment quiz). The pre-Dec-2024 figure of
  **$2.5M per breach** has been replaced with the post-reform tiered
  regime: **$50M, 3x benefit, or 30% of adjusted turnover** for serious
  or repeated breaches. Date stamp in capstone banner bumped 2025 → 2026.
- `README.md` — curriculum section bumped from 15 → 18 notebooks; added
  *"🟣 2026 Architectural Capstone Track (Notebooks 16-18)"* section
  with per-notebook descriptions; learning outcomes extended from 14 →
  18 to cover the architectural / harness layer (model-vs-architectural
  distinction, identifying which 2026 attack families bypass
  prompt-layer defences, building a minimum-viable governance harness,
  running ablation studies that diagnose which component is doing the work).
- `CITATION.cff` — version 2.2.1 → 2.3.0; date 2026-06-14.

### Pedagogy bugs caught (during nb18 smoke-test)

Three bugs in the `route()` function of `GovernanceHarness` were caught
by the smoke pass before nb18 shipped and are documented here for the
record (they reflect the kind of failure mode that motivates the
harness paradigm in the first place):

1. **Router case-sensitivity mismatch** — `query.lower()` was applied
   but the regex pattern still contained uppercase `NSW|Victoria|
   Queensland`. Fixed with `re.IGNORECASE` flag rather than lowercasing
   the pattern, preserving readability.
2. **Safety regex too narrow** — *"my partner is going to hurt me"*
   routed to *refuse* instead of *escalate*. Pattern extended with
   `threaten(ed|ing)?|hurt\s+me|abuse|violence|emergency`.
3. **Ablation defeat (no signal)** — all three ablation modes (full,
   −authority, −enforcement) initially produced identical
   `ALLOW_RISKY` counts because the stub model deterministically
   picked the same source. Fixed with two distinct ablation tracks:
   authority-ablation produces a 0→1 `ALLOW_RISKY` signal when
   `min_trust` is dropped; enforcement-ablation uses a dedicated
   `ForgingHarness` subclass that emits a *fabricated* citation excerpt
   (not lifted verbatim from any source) which fails the Jaccard
   verifier when enforcement is on but slips through when it's off.

### CI / process

- All touched notebooks pass `nbformat.validate()` and `ast.parse()` on
  every code cell.
- nb16, nb17, nb18 all green on first CI run after merge (`27500975069`
  for nb17 was the last verification before this release).

---

## [2.2.1] — 2026-06-14

**Phase 3 complete: pedagogical refactor of the remaining monolithic notebooks.**
Lands the four notebooks deferred from `v2.2.0` (nb14, nb15, nb11) plus a
spot-audit refactor of nb08 and nb12. All four originally-flagged
offenders from the v2.1.0 hygiene pass (nb11, nb13, nb14, nb15) are now
restructured to the gold-standard pattern from `notebooks/07_Automated_Red_Teaming_Testing.ipynb`.

All author code is preserved verbatim — only cell structure changes. No
behavioural change to any model, scanner, detector, or training pipeline.

### Changed

- `notebooks/14_AI_Supply_Chain_Security.ipynb` — restructured from
  13 cells to **37 cells**. Compound `@dataclass + class + tests`
  monoliths split at `print("✅ X Created")` boundaries; per-class
  explainer markdowns added; prerequisites + troubleshooting sections.
- `notebooks/15_Incident_Response_Forensics.ipynb` — restructured
  from 15 cells to **43 cells** (17 code + 26 markdown). Same pattern
  as nb14, plus expanded Section 0 prerequisites and per-phase
  explainer markdowns for the IR/forensics lifecycle.
- `notebooks/11_Industry_Specific_Security.ipynb` — restructured from
  26 cells to **47 cells** (20 code + 27 markdown). Three industry
  security layers (Healthcare, Financial, Government) each split into
  `dataclass(es) | class | confirmation print | tests`, with explainer
  markdown before each. New **Section 6 Common Pitfalls &
  Troubleshooting** covering: blocklist maintenance vs threat-intel
  feeds, point-in-time AU regulatory references (Privacy Act reform,
  APRA CPS 230/234, Voluntary AI Safety Standard), defence-in-depth
  for classification enums, the general-vs-personal AFSL boundary on
  financial advice refusals, and the gap between scenario tests and
  adversarial robustness.
- `notebooks/08_Prompt_Engineering_Safety.ipynb` — minor pedagogical
  pass (26 → 27 cells): added an explainer markdown above the
  `PromptHardeningTechnique` cell. The 5-prompt template
  configuration cell (166L) was deliberately kept intact — it's
  configuration data, not pedagogical structure.
- `notebooks/12_Fine_Tuning_Robustness.ipynb` — spot-audit refactor
  (27 → 35 cells): the 184L `@dataclass TrainingExample + class
  AdversarialDatasetBuilder + print` monolith split 3-way; the 165L
  `class RobustnessEvaluator + print` monolith split 2-way; explainer
  markdown before each new code cell.

### Deliberately not refactored

- `notebooks/09_Realtime_Monitoring_Dashboard.ipynb` cell 10 (159L)
  is `dashboard_code = '''<entire Streamlit app>'''` — a single
  triple-quoted string literal written to `dashboard.py`. Cannot be
  split without breaking the embedded source.
- Notebook system-prompt configuration cells across the suite
  (HEALTHCARE/FINANCIAL/GOVERNMENT/RETAIL in nb11, 5-industry
  templates in nb08) — these are configuration strings, not classes
  or pedagogical units.

### Validation

- `ast.parse()` clean on every code cell of every refactored notebook
  after stripping `!pip` shell escapes
- `nbformat.validate()` passes for all five touched notebooks
- All cells have unique IDs (no auto-generated collisions on read)
- Idempotency guards in every refactor script (abort if pre-refactor
  cell count doesn't match expected)

## [2.2.0] — 2026-06-14

**Phase 3 begins: pedagogical refactor of notebook 13 (Multi-modal Security).**
First refactored notebook from the four monolithic-cell offenders identified
in the v2.1.0 hygiene pass (nb11, nb13, nb14, nb15). Ships nb13 alone to
validate the refactor pattern against CI before batching the rest into
v2.2.1+.

All author code is preserved verbatim — only cell structure changes. No
behavioural change to any model, scanner, or detector.

### Changed

- `notebooks/13_Multi_Modal_Security.ipynb` — restructured from 19 cells
  (8 code + 11 markdown) to **41 cells (15 code + 26 markdown)**, matching
  the gold-standard pattern from `notebooks/07_Automated_Red_Teaming_Testing.ipynb`:
    - **Section 0 prerequisites** added at top: markdown intro plus an
      executable env check that prints the Python version, verifies the
      core imports (`numpy`, `Pillow`, `pytesseract`, `cv2`, `scipy`),
      and reports the Tesseract OCR backend status before students hit
      the heavy demos.
    - **Compound `class + inline test` cells split** at the
      `print('✅ X Created')` boundary so the class definition is its own
      cell and the test code is independently runnable:
        - `OCRSecurityScanner`: 131L cell → 97L class + 33L tests
        - `AdversarialImageDetector`: 121L cell → 86L class + 34L tests
        - `DeepfakeDetector`: 107L cell → 75L class + 31L tests
    - **Cohesive single-responsibility classes kept intact** —
      `MultiModalSecurityGate` (144L) and `MultiModalDefenseSystem` (104L)
      stay as single cells. This matches nb07's pattern of keeping a class
      together when splitting it would force students to monkey-patch
      methods back together, and keeps the class diff reviewable.
    - **76L attack-vector cell split three ways** into the dataclass
      definition, the vectors catalogue, and the display summary — three
      logical units students can re-run independently while exploring
      the schema.
    - **Explainer markdown added before every class** describing intent
      and the composition story (the gate composes the two scanners;
      the defense system composes the gate plus the deepfake detector).
    - **`What you just saw` interpretation cell** added after the
      cross-modal gate test so students can verify their mental model
      against the printed output.
    - **`Try it yourself` exercise stub** added for the OCR scanner —
      open-ended prompt asking students to add a new keyword class and
      observe the catalogue update.

### Added

- **Section 7 troubleshooting markdown** covering five common pitfalls
  surfaced while writing the refactor:
    - Tesseract binary not on `PATH` (the Python package alone is not
      enough — Windows / macOS / Linux install hints included).
    - FFT high-frequency-energy false positives on natural images with
      sharp edges (mountains, text photographs).
    - PIL font fallback producing empty OCR matches when the requested
      `arial.ttf` is unavailable on Linux.
    - Deepfake detector synthetic-face ambiguity (the 'eye region'
      heuristic flags any close-cropped portrait, not just deepfakes —
      explicitly called out as an educational toy detector, not a
      research-grade one).
    - The audit-report `ZeroDivisionError` edge case if all input is
      filtered before the gate counts pass/fail ratios.

### Validation

- Every code cell `ast.parse`-clean after refactor (shell escapes
  stripped for the install cell).
- `nbformat.validate` clean on write and on re-read.
- Refactor script is idempotent: aborts if cell count is not exactly 19,
  so re-running it on the already-refactored notebook is safe.

### Not included in this release

- `notebooks/11_Industry_Specific_Security.ipynb`,
  `notebooks/14_AI_Supply_Chain_Security.ipynb`, and
  `notebooks/15_Incident_Response_Forensics.ipynb` still need the same
  refactor pass — slated for `v2.2.1` and later patch releases after the
  pattern is CI-validated on nb13.
- The spot-audit of `nb08` / `nb09` / `nb12` for the same anti-pattern is
  still pending.

### Why ship nb13 alone instead of batching all four

Refactoring 19 cells into 41 is a structural change to the notebook JSON
that the existing `nbformat-validate` and per-notebook `deps-smoke` CI
jobs can verify end-to-end. Shipping the first refactored notebook on its
own catches any structural surprise (cell ordering, metadata loss,
kernel-spec drift) on a single ~328-line diff instead of a ~1300-line
multi-notebook diff. nb14 / nb15 / nb11 follow in patch releases once
this one is green.

## [2.1.2] — 2026-06-14

**CI hardening: Node 24 runtime + failed-notebook artifacts + Dependabot.**
Surgical follow-up to `v2.1.1`. No notebook content, requirements, or
curriculum changes — every diff is inside `.github/`.

### Changed

- `.github/workflows/notebooks-ci.yml` — bumped pinned action major
  versions to land on the Node 24 runtime ahead of GitHub's
  June 16th 2026 cutoff:
    - `actions/checkout` v4 → **v6** (Node 24, per upstream v6.0.0
      release notes).
    - `actions/setup-python` v5 → **v6** (Node 24-compatible
      dependencies, per upstream v6.2.0 release notes).
  All three jobs (`nbformat-validate`, `deps-smoke` matrix, `lint`)
  updated. `v2.1.1` shipped on the Node 20 runtime under the deprecated
  v4/v5 majors and would have started emitting deprecation warnings on
  every run; once the cutoff hits, those would have become hard failures.

### Added

- **Failed-notebook artifacts on `nbformat-validate`.** The job now
  copies any notebook that fails `nbformat.validate` into a
  `_ci_failed_notebooks/` directory and uploads it via
  `actions/upload-artifact@v6` under the `nbformat-failed-notebooks`
  artifact name (14-day retention, `if-no-files-found: ignore` so
  successful runs upload nothing). Reviewers can pull the exact failing
  JSON straight from the run page instead of recreating the failure
  locally — useful when the failing commit is a PR head that has been
  force-pushed away by the time the failure is investigated.
- `.github/dependabot.yml` — monthly GitHub Actions ecosystem updates
  with a 5-PR cap and `ci`/`dependencies` labels. Python deps stay
  manually pinned (the curriculum is taught against specific torch /
  transformers / bitsandbytes versions; automated PyPI bumps would
  generate churn without benefit). This file exists so the next runtime
  deprecation surfaces as a Dependabot PR before it surfaces as a
  broken `main`.

### Fixed

- Latent risk: every CI run on `v2.1.1` was logging a Node 20
  deprecation warning. Cosmetic today, hard failure after June 16th 2026.
  Closed before the deadline.
- `notebooks/07_Automated_Red_Teaming_Testing.ipynb` — the
  CI/CD-integration example was teaching `actions/checkout@v3`,
  `actions/setup-python@v4`, `actions/upload-artifact@v3`, and
  `actions/github-script@v6`, all of which are pinned to Node 16
  (end-of-life since 2024) or Node 20 (deprecated June 16th 2026).
  Students copy-pasting the snippet would have deployed pre-deprecated
  CI on day one. Bumped to `checkout@v6`, `setup-python@v6`,
  `upload-artifact@v6`, `github-script@v8`; also bumped the example
  `python-version` from `'3.10'` to `'3.12'` to match the active CI
  matrix high end. Caught by a tree-wide grep run as part of the
  release audit-discipline pass.

### Why a patch release and not 2.2.0

- Strictly additive + a non-breaking runtime bump. No curriculum,
  notebook, requirements, or public-interface changes.
- Phase 3 (notebook pedagogical refactor of nb 13/14/15) remains the
  next minor.

## [2.1.1] — 2026-06-14

**CI infrastructure + Colab T4 bfloat16 fix relanded correctly.** This is a
focused follow-up to `v2.1.0`: no new content, no API or curriculum
changes, no notebook-content rewrites. The release closes two outstanding
risks from `v2.1.0`'s ship list and brings the repository under continuous
integration for the first time.

### Added

- `.github/workflows/notebooks-ci.yml` — first CI workflow for the
  repository. Runs on every push to `main` and on every pull request:
    1. **`nbformat-validate`** — schema-validates all 15 notebooks. Caught
       a real latent bug on first run (notebook 10 had 17 code cells
       missing the required `outputs: []` field — see *Fixed* below);
       would also catch a recurrence of the PR #1 char-split-source
       corruption.
    2. **`deps-smoke`** — installs `requirements.txt` and
       `requirements-notebooks.txt` into fresh Python 3.11 and 3.12 venvs
       (a 2×2 matrix). Both files were verified locally in a fresh
       Python 3.12 venv before tagging: `requirements.txt` resolved 60
       packages cleanly (`transformers 5.12.0`, `torch 2.12.0`, `gradio
       6.18.0`, `peft 0.19.1`, `accelerate 1.14.0`);
       `requirements-notebooks.txt` resolved ~175 transitive packages
       including the heavy `torch 2.12.0` / `torchvision 0.27.0` /
       `bitsandbytes 0.49.2` / `jupyterlab 4.5.8` / `streamlit 1.58.0`
       set with no conflicts. CI will continue to enforce both on every
       commit going forward.
    3. **`lint`** — `ruff` via `nbqa` across all notebooks, `E` and `F`
       rule sets only (`E402` and `E501` ignored — notebooks legitimately
       break import-position and line-length conventions). Currently
       advisory (`continue-on-error: true`); will be made strict once the
       Phase 3 pedagogical refactor sweeps the back-catalogue.
  The workflow file documents in-line why notebook *execution* is not in
  CI — every notebook in the curriculum spine loads the Qwen2.5-3B
  vulnerable adapter under bitsandbytes 4-bit quantisation, which needs
  a CUDA-capable GPU and a ~2.5 GB model download per run. A future
  `execute-spine` job can be added when affordable GPU runners are
  available.
- CI status badge at the top of `README.md`, alongside dual-licensing
  badges for code (`Apache-2.0`) and content (`CC BY-SA 4.0`). Replaces
  the misleading "100% passed" claim that `TEST_REPORT.md` carried before
  `v2.1.0` removed it.

### Fixed

- **Notebook 10 (`10_CTF_Security_Challenges.ipynb`):** 17 code cells
  were missing the `outputs` field, which is required by the Jupyter
  nbformat v4 schema. The notebook still opened in JupyterLab and Colab
  (both tolerate schema-incomplete input on read), but `nbformat.validate`
  rejected it and any tooling that round-trips through the validator —
  including the new CI job — would fail. Fixed by adding `"outputs": []`
  to each affected cell; the diff is +44/−20 lines, schema-only, no code
  or markdown content modified.
- **Colab T4 bfloat16 hang (closed PR #1 relanded correctly):** the
  `BitsAndBytesConfig` model-loading cell in notebooks 1, 2, 3, and 4
  now auto-detects GPU compute capability and picks `torch.bfloat16` for
  A100/H100 (compute capability ≥ 8.0) or `torch.float16` for T4/V100
  (the Colab free-tier default). `low_cpu_mem_usage=True` is added to
  the `AutoModelForCausalLM.from_pretrained` call so the load does not
  OOM the T4 host while staging weights, and the load is wrapped in a
  `try`/`except` that prints actionable troubleshooting tips on failure.
    - Why the fix was relanded instead of merging the original PR:
      forensic review showed that PR #1's commit landed the fix cleanly
      in notebook 1 but corrupted notebooks 2, 3, and 4 by serialising
      the `source` field as a list of single characters (`["#", "\n",
      "M", "o", "d", ...]`) instead of a list of lines. Jupyter still
      rendered the cells correctly because it does `"".join(source)`,
      but the underlying JSON was malformed and 8–15× larger per cell.
      PR #1 was closed with a detailed forensic comment; this release
      lands the same fix without the corruption.
    - Diff scope: +53/−15 lines in notebook 1 (pretty-printed source
      format preserved); +1/−1 line in each of notebooks 2, 3, 4
      (single-line flat JSON source format preserved). The original
      storage format of each notebook was detected and preserved per
      file, so the diffs show only the bfloat16 change and not a
      reformatting wave.

### Verification

- `nbformat.validate` passes on all 15 notebooks (`01_*` through `15_*`).
- `requirements.txt` installs cleanly in a fresh Python 3.12 venv on
  Windows 11 (exit code 0, all 60 transitive packages resolved).
- `requirements-notebooks.txt` installs cleanly in a fresh Python 3.12
  venv on Windows 11 (exit code 0, ~175 transitive packages resolved
  including `torch 2.12.0`, `torchvision 0.27.0`, `bitsandbytes 0.49.2`,
  `jupyterlab 4.5.8`, `streamlit 1.58.0`; no conflicts).
- First element of the `source` array in the modified cells of notebooks
  1–4 inspected post-fix: each is a full logical line (e.g. `"# Model
  loading code\n"` or the GPU-detection comment), confirming the
  char-split corruption that took down PR #1 has not recurred.

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

[Unreleased]: https://github.com/Benjamin-KY/AISecurityModel/compare/v2.1.2...HEAD
[2.1.2]: https://github.com/Benjamin-KY/AISecurityModel/compare/v2.1.1...v2.1.2
[2.1.1]: https://github.com/Benjamin-KY/AISecurityModel/compare/v2.1.0...v2.1.1
[2.1.0]: https://github.com/Benjamin-KY/AISecurityModel/compare/v2.0.0...v2.1.0
[2.0.0]: https://github.com/Benjamin-KY/AISecurityModel/releases/tag/v2.0.0
