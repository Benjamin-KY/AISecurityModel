# Contributing — AI Security & Jailbreak Defence Course

Thank you for considering a contribution. This file documents the
disciplines that keep the course rigorous, vulnerable-then-educate,
Australian-grounded, and pedagogically coherent. Read it once before
your first PR.

> **Skimming first?** The three sections you must read before opening a
> PR are **§ License + dual-licensing**, **§ Pedagogical contract**, and
> **§ Code of Conduct**. Everything else is reference material.

---

## What contributions look like

Most landed changes fall into one of:

1. **Bug fix** — a notebook cell that no longer runs on current
   versions of `transformers` / `torch` / Colab, a broken link, a
   typo in compliance prose, a Hugging Face API change.
2. **New attack or defence pattern** — a notebook cell or sub-section
   adding a recently disclosed jailbreak class (e.g. a 2026 successor
   to Skeleton Key) or a new defence technique (constitutional
   classifier, sparse-autoencoder steering, etc.) with the
   vulnerable-then-educate framing intact.
3. **New worked example** — a real-world incident, court case, or
   regulatory action that maps onto an existing notebook (current
   Australian context preferred but not required).
4. **New notebook** — a 2026 surface not yet covered (agent/MCP tool
   misuse, RAG-layer injection, indirect injection via tool outputs,
   etc.). Coordinate with the maintainer before starting.
5. **Pedagogical refactor** — splitting monolithic code cells (notebooks
   13, 14, 15 are the obvious candidates) into ≤30-line incremental
   cells with markdown explanations between, modelled on notebook 7
   (the gold-standard cell structure).
6. **Test / CI improvement** — adding `nbval-lax` coverage, `nbqa` lint,
   notebook-format validation, or pinning dependencies more tightly.
7. **Documentation** — improvements to `README.md`, `docs/EDUCATOR_GUIDE.md`,
   the vulnerability taxonomy, or to disclaimers / guard-rail prose
   around vulnerable code cells.

---

## License + dual-licensing

By submitting a PR you license your contribution under the same dual
license the course uses (Apache-2.0 for code; CC BY-SA 4.0 for content):

- **Code** — `app.py`, anything in `scripts/`, executable code cells
  in `.ipynb` files, future `.py` modules — **Apache-2.0**.
- **Course content** — `notebooks/` notebook prose cells, `data/` files
  containing curated taxonomies or training pairs, `docs/`, top-level
  Markdown including `README.md` — **CC BY-SA 4.0**.

By opening a PR you confirm you have the right to license the
contribution under these terms. See `LICENSE` and `LICENSE-DOCS`.

---

## Pedagogical contract

Every notebook in this course follows the **vulnerable-then-educate**
pattern. Contributions must preserve it:

1. **Demonstrate the failure first** — show the vulnerable model
   actually being jailbroken (or the defence actually being
   circumvented). No "imagine what would happen" hypotheticals.
2. **Then teach the mitigation** — show *why* it failed, then the
   defence pattern that fixes it.
3. **Label vulnerable cells** — every cell that contains attack code
   or a vulnerable configuration must carry a markdown header /
   comment making clear the cell is for educational use only.
4. **Never imply production-readiness** — defended-mode cells are
   *demonstrations* of mitigation, not drop-in production code.
   The taxonomy in `data/vulnerability_taxonomy.json` is an
   educational reference, not an enterprise threat-intelligence feed.
5. **Australian context where natural** — where a notebook touches
   compliance, reference the relevant Australian statute (Privacy
   Act 1988, APRA CPS 234, ACSC Essential Eight, AI Ethics
   Principles, Voluntary AI Safety Standard) by name, with a citation
   that resolves. Other jurisdictions are welcome additions but
   should sit alongside, not replace, the Australian framing.

> **Cell-size discipline.** Code cells in new or refactored notebooks
> should be ≤30 lines and do one teachable thing. Notebook 7
> (`07_Automated_Red_Teaming_Testing.ipynb`) is the structural model:
> prerequisites cell, small incremental code cells with markdown
> between, intermediate display/test cells, "try it yourself"
> exercises, and a closing "key takeaways" section. Notebooks 13–15
> currently break this discipline and are scheduled for refactor.

---

## Code of Conduct

This course teaches red-team techniques against AI systems. The
following Code of Conduct applies to all contributors, learners, and
instructors. Violations may result in PRs being closed and contributors
being banned from the repository.

All participants must:

1. ✅ **Use only on systems you own or have explicit written
   authorisation to test.** This is non-negotiable.
2. ✅ Practice **responsible disclosure** of any real vulnerabilities
   you discover in production AI systems while developing skills with
   this material.
3. ✅ Respect privacy and data-protection laws in your jurisdiction.
4. ✅ Follow your institution's ethics-approval and student-supervision
   processes when using this material in formal teaching.
5. ✅ Be respectful in issues, PRs, and discussions. Disagreement on
   technical merit is welcome; ad-hominem, harassment, or
   bad-faith contributions are not.
6. ❌ **Never** attack production systems without permission.
7. ❌ **Never** use techniques from this course to harm individuals or
   organisations.
8. ❌ **Never** submit a PR that strips disclaimers, removes the
   vulnerable-then-educate framing, or repackages the vulnerable
   adapter as "production-ready".

The maintainer reserves the right to close issues or PRs that violate
this Code of Conduct without further discussion. Persistent or severe
violations will result in being blocked from the repository.

This Code of Conduct is adapted from the principles in the
**Contributor Covenant v2.1** combined with the responsible-use
expectations specific to security-education material.

---

## How to propose a change

1. **Open an issue first** for non-trivial changes (new notebook,
   pedagogical refactor of an existing notebook, new attack/defence
   category, breaking changes to taxonomy schema). Quick fixes
   (typos, broken links, dependency pin bumps) can go straight to PR.
2. **Branch naming.** Use `fix/<short-description>`, `feat/<short-description>`,
   `docs/<short-description>`, or `refactor/<notebook-name>`.
3. **Commit message.** First line ≤72 chars, imperative mood
   ("Fix Colab T4 dtype hang in notebook 02"). Body explains *why*,
   not *what* the diff already shows.
4. **Verification before push.**
   - Notebooks: clear all outputs (`jupyter nbconvert --clear-output`),
     restart-and-run-all on a fresh kernel, confirm no errors.
   - Code: run `python -m py_compile app.py scripts/*.py` to catch
     syntax breaks; run the existing scripts on a small input where
     practical.
   - Markdown: render locally and check links resolve.
5. **CHANGELOG.md.** Append a line under the next-version heading
   describing the user-visible effect of your change.
6. **PR description.** Reference the issue, summarise what changed and
   why, and list verification steps you ran.

---

## Per-release ship discipline

Tagged releases follow a small ritual:

1. **CHANGELOG.md entry** moved from `[Unreleased]` to the new
   version heading with date.
2. **Version bump** in `README.md` (the footer block) and
   `CITATION.cff` (the `version:` and `date-released:` fields).
3. **Tag and release.** `gh release create vX.Y.Z --target main
   --notes-file <release-notes>` (this auto-creates the tag at HEAD —
   do *not* push the tag separately first).
4. **Hugging Face Space.** If `app.py`, `requirements.txt`, or the
   adapter has changed, push to the Space remote in a separate
   step; the Space is its own git remote.

Semver-style: **major** for breaking changes to notebook
prerequisites or taxonomy schema; **minor** for new notebooks /
new attack-or-defence patterns; **patch** for fixes, doc updates,
and refactors that don't change pedagogy.

---

## Sibling course and reading order

This repository teaches the **model and prompt layer** of AI security.
For the **structural-harness layer** (architectural scaffolding around
the model — policy router, source authority, output contract, audit
log, escalation gate) see the sibling course
[`harmless-harnesses`](https://github.com/Benjamin-KY/Harmless-Harnesses).

Suggested reading order for serious learners:

1. This course, notebooks 1–8 (foundational attacks + interpretability +
   defences).
2. `harmless-harnesses` Foundation track (F0–F3) for the harness paradigm.
3. This course, notebooks 9–15 (production-flavoured surfaces:
   monitoring, multi-agent, industry compliance, fine-tuning,
   multi-modal, supply chain, incident response).
4. `harmless-harnesses` Practitioner track (P-modules) for the
   five-component architecture, then the Tensions track (T-modules)
   for the structural critique.

Contributions that strengthen the cross-link (e.g. a notebook here
that ends "→ see harmless-harnesses module X" where natural) are
particularly welcome.
