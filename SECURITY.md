# Security Policy

> **Scope.** This document covers `AISecurityModel` the **educational course
> repository** — Jupyter notebooks, the Gradio Space `app.py`, fine-tuning
> scripts, training data, and the deliberately vulnerable LoRA adapter
> `Zen0/Vulnerable-Edu-Qwen3B`. It does *not* cover downstream uses of any
> material in this repo; operators who incorporate techniques from this
> course into production code or pipelines must publish their own
> `SECURITY.md`.
>
> The course is dual-licensed (Apache-2.0 for `app.py`, scripts, and code
> cells; CC BY-SA 4.0 for prose, notebooks-as-content, and the vulnerability
> taxonomy). Security obligations apply equally across both surfaces.

---

## Vulnerable-by-design — read this first

Several artefacts in this repository are **intentionally vulnerable for
educational purposes**:

- `Zen0/Vulnerable-Edu-Qwen3B` — LoRA adapter fine-tuned to be more
  jailbreakable than the Qwen2.5-3B base model. This is the lab specimen
  every Beginner notebook (1–4) loads.
- `data/training_data.jsonl` and `data/vulnerability_taxonomy.json` —
  curated attack/defence pairs and OWASP-mapped taxonomy. These document
  attack patterns and are intended for classroom red-teaming, not for
  production threat models.
- Every notebook follows the **vulnerable-then-educate** pattern: a working
  jailbreak is demonstrated first, then the defence is taught. Snippets
  isolated from the surrounding pedagogical context are explicitly
  unfit for production.

**These are not security bugs.** Pull requests or issues that report
"the vulnerable model is vulnerable" or "the documented attack pattern
works against the documented vulnerable target" will be closed politely.

---

## Threat model

This repository ships:

1. **Educational notebooks** (`notebooks/`) — read in a local Jupyter or
   Google Colab session; execute attack and defence code against a
   downloaded model. Default execution surface is the learner's own
   machine or their Colab runtime.
2. **A Gradio Space** (`app.py` + `README_SPACE.md`) — a public hosted
   demo on Hugging Face Spaces that loads the vulnerable adapter and
   compares it side-by-side with a defended variant. The Space accepts
   arbitrary prompt input from the public internet.
3. **Fine-tuning scripts** (`scripts/`) — run by an instructor with their
   own Hugging Face token to regenerate the vulnerable adapter or
   variants thereof.
4. **Training data** (`data/training_data.jsonl`) — the supervised dataset
   used to produce the vulnerable adapter and to seed defence examples.

The realistic adversary surface this policy covers:

- **Supply-chain compromise** of the dependency tree (`transformers`,
  `torch`, `peft`, `accelerate`, `bitsandbytes`, `gradio`, and the
  full notebook-time deps in `requirements-notebooks.txt`).
- **Compromised model artefact** — if the Hugging Face Hub repository
  `Zen0/Vulnerable-Edu-Qwen3B` is hijacked and replaced with a
  malicious adapter, every notebook in this course would load the
  attacker's weights. Operators running the course offline should
  pin a specific revision hash.
- **Credential leak** in fine-tuning workflow — `scripts/merge_and_upload.py`
  consumes a Hugging Face write token. The script must never commit
  this token to git; reports of the script *leaking* credentials are
  in-scope security bugs.
- **Indirect prompt-injection via training data** — if upstream contributors
  add a poisoned `training_data.jsonl` entry that makes the *defended*
  model also compliant, that is a content-integrity issue and is
  in-scope (report privately).
- **CI compromise** — when GitHub Actions are added (Phase 2), any
  way to make a workflow run untrusted PR code with write access is
  in-scope.
- **Inappropriate reuse** — an operator copies a notebook cell into a
  production system and ships it. This is a documentation /
  positioning failure on our side if the cell is not adequately
  labelled. See **§ Out of scope** below; we will accept docs PRs
  that improve guard-rail prose around specific cells.

The course is **not** designed to defend against:

- Misuse of the vulnerable adapter on systems the operator does not
  own. The disclaimers in `README.md` § Important Disclaimer are the
  primary mitigation; ethical use is the operator's responsibility.
- A compromised Hugging Face Hub. We cannot revoke a poisoned adapter
  upload that has already been served.

---

## Out of scope

The following are **not** security vulnerabilities for this repository:

1. The vulnerable adapter being jailbreakable, in any way, by any
   technique. That is the lab specimen.
2. Notebooks 13, 14, 15 having monolithic code cells. That is a
   pedagogical-quality issue tracked in the course roadmap, not a
   security bug.
3. The hosted Gradio Space returning unsafe outputs in response to
   adversarial prompts. The Space exists to demonstrate exactly this.
4. The fine-tuning scripts producing a vulnerable model. That is
   their stated purpose.

If you are unsure whether a finding is in scope, **report it privately
anyway**. We would rather triage one extra report than miss a real bug.

---

## Reporting a vulnerability

Please report vulnerabilities **privately** to the maintainer via
GitHub Security Advisories on this repository's
[security advisory page][advisories]. Do not file public issues for
security findings.

A typical report should include:

1. The class of issue (supply chain, credential leak, training-data
   poisoning, CI compromise, etc.).
2. The affected files / commits / Hugging Face revisions.
3. A minimal reproduction.
4. Your assessment of impact and any mitigations you have in mind.

We will acknowledge receipt within **5 working days** and aim to ship a
fix or a documented mitigation within **30 days** for critical issues
and **90 days** for non-critical ones. We will credit reporters in the
`CHANGELOG.md` release notes unless they prefer anonymity.

[advisories]: https://github.com/Benjamin-KY/AISecurityModel/security/advisories/new

---

## Supported versions

The course follows a rolling-release model on `main`. Security-relevant
fixes land in `main` and are surfaced in the next tagged release. The
previous minor release receives backports for **30 days**; older
versions are unsupported.

The vulnerable adapter `Zen0/Vulnerable-Edu-Qwen3B` is versioned by
Hugging Face revision hash; classroom operators who need a specific,
audited version should pin the revision rather than the symbolic tag.

---

## Responsible disclosure expectation for learners and instructors

This course teaches red-team techniques against AI systems. Learners
and instructors who use this material commit to the **Code of Conduct**
in `CONTRIBUTING.md`:

- Use only on systems you own or have explicit written authorisation
  to test.
- Practice responsible disclosure if you find a real vulnerability in
  a production AI system in the course of skill development.
- Do not use techniques from this course for attacks on production
  systems, individuals, or organisations.
- Australian users: relevant statutes include sections of the
  *Criminal Code Act 1995* (Cth) (unauthorised access offences) and
  the *Privacy Act 1988* (Cth). Comparable laws apply in other
  jurisdictions; the course author makes no warranty about local
  legality.

If you are an external researcher who has identified a real AI-security
vulnerability inspired by techniques in this course and want guidance
on responsible disclosure, you may open a private advisory here for
**triage advice only**; we will redirect to the appropriate vendor or
CERT.
