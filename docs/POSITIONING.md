# 🧭 Positioning: Where AISecurityModel fits

**Status:** Authoritative positioning doc for this repository's relationship to the broader Kereopa-Yorke harness-paradigm work.
**Last updated:** 2026-06-15

This document exists because "AI security course" is a crowded label. Three repositories in the public Kereopa-Yorke account ([@Benjamin-KY](https://github.com/Benjamin-KY)) address overlapping concerns from very different angles, and a learner or instructor needs to know *which one to pick first* and *what each one is — and is not — claiming to do*.

If you are evaluating this repository for adoption, this is the most important document to read after the [README](../README.md).

---

## 🌐 The three repositories at a glance

| Repository | Layer | Form | What it teaches / proves | When to choose it |
|---|---|---|---|---|
| **AISecurityModel** *(you are here)* | **Model & prompt** + bridge to architectural | Course (18 Jupyter notebooks) + Gradio demo Space | What attacks the model. What defends at the prompt boundary. Where those defences run out. | You need hands-on attacks-and-defences material for a class, a team, or a self-paced learner who can already write Python. You want a notebook-driven format. |
| **[harmless-harnesses](https://github.com/Benjamin-KY/Harmless-Harnesses)** | **Architectural / harness** | Course (29 modules across F/C/P/T/CAP tracks) + Anki deck + scaffolds | How to wrap *any* model in a governance architecture so that defined harm classes are reduced *when preconditions hold*. Five components, five invariants. | You have the model-layer literacy from AISecurityModel (or equivalent) and need to build, measure, and operate the harness *around* the model. You want a code-first curriculum, not a notebook. |
| **[sa-sovereign-llm-harness](https://github.com/Benjamin-KY/sa-sovereign-llm-harness)** | **Research codebase + evaluation methodology** | Reference implementation + SA-GOV-BENCH dataset + demo stack | Empirical evidence that governance harnesses add measurable value to frontier LLM outputs in public-sector advisory contexts (200 items × 9 conditions × 6 models × 2 jurisdictions, ~12,600 scored responses; May 2026 results). Indigenous-data-sovereignty-led positioning. | You are a researcher, a regulator, a public-sector procurement reviewer, or a graduate student writing in this space. You want the citable corpus, the reproducible eval, and the IDSov-led positioning. |

The three are designed to compose. You can use any one alone, but the **whole story** runs:

> **AISecurityModel** (learn what fails at the model layer) → **harmless-harnesses** (learn the architecture that fixes it) → **sa-sovereign-llm-harness** (read the empirical evidence, in a regulated-domain study).

---

## 🎯 What this repository *is*

- A **hands-on, vulnerable-then-educate course**. Every attack is demonstrated working against a deliberately-vulnerable LoRA adapter on Qwen2.5-3B first; the matching defence is taught immediately after.
- **18 Jupyter notebooks** across three tracks:
  - 🟢 **Foundational** (nb01–nb06): introduction → defence-in-depth at the prompt boundary
  - 🟠 **Advanced** (nb07–nb15): automated red-teaming, prompt-engineering for safety, monitoring, fine-tuning robustness, multi-modal, supply chain, incident response & forensics
  - 🟣 **2026 Architectural Capstone** (nb16–nb18): agent/MCP tool misuse, RAG-layer prompt injection, the harness paradigm — with explicit hand-off to `harmless-harnesses`
- **Australian-context-grounded**: Privacy Act 1988 (post-2024 reform — tiered penalties up to $50M / 3× / 30% turnover), ACSC Essential Eight, APRA CPS 234, PSPF / ISM, NDB scheme, OAIC 30-day notification.
- **A working Gradio demo** ([`app.py`](../app.py)) comparing the vulnerable model and a defended variant side-by-side.

## 🚫 What this repository is *not*

- **Not a production-ready security platform.** The vulnerable adapter is for education. See the disclaimer in the README.
- **Not a complete architectural curriculum.** Notebooks 16–18 are a *bridge* into the harness paradigm — they introduce it; they don't exhaust it. For that, you need `harmless-harnesses`.
- **Not a research artefact with reproducible benchmarks.** That is what `sa-sovereign-llm-harness` exists for. This repository's claims are pedagogical, not empirical.
- **Not a substitute for the Indigenous-data-sovereignty positioning** that the harness paradigm carries. The capstone notebook (nb18) acknowledges this hand-off explicitly; the full positioning lives in `docs/the-harness-paradigm.md` in the research repo and is referenced verbatim in F0 §6 and F2 §6 of `harmless-harnesses`.

---

## 🧱 The two-layer model — why this is not a duplication of `harmless-harnesses`

Both repositories teach "LLM security." They are *not* duplicates. They sit at different layers of the same problem.

```
  ┌──────────────────────────────────────────────────────────────┐
  │                  Architectural / harness layer               │
  │                                                              │
  │   policy router · source authority · output contract         │
  │   audit log · escalation FSM                                 │
  │                                                              │
  │   ← TAUGHT BY: harmless-harnesses (full architectural course)│
  │   ← INTRODUCED BY: AISecurityModel nb16 / nb17 / nb18        │
  └──────────────────────────────────────────────────────────────┘
                                ▲
                                │ (the harness wraps the model)
                                ▼
  ┌──────────────────────────────────────────────────────────────┐
  │                   Model & prompt layer                       │
  │                                                              │
  │   jailbreaks · prompt injection · encoding · Skeleton Key    │
  │   system-prompt extraction · output filtering · safety       │
  │   fine-tuning · interpretability · monitoring                │
  │                                                              │
  │   ← TAUGHT BY: AISecurityModel nb01 – nb15                   │
  └──────────────────────────────────────────────────────────────┘
```

The **architectural** layer wraps the **model** layer. Defences at one layer do not fix failures at the other:

- A perfectly hardened prompt cannot stop a tool-output indirect injection (nb16) or a poisoned document in a RAG index (nb17). Those failures live in the architectural layer.
- A perfect harness still gets a confused-deputy outcome if you wire it to a model that complies with Skeleton Key or system-prompt extraction (nb04, nb05) on the inputs the harness happens to forward.

You need both layers to ship a regulated-domain system. This repository teaches one of them and bridges into the other.

---

## 📖 Reading order

### Path 1 — Learner who wants the complete picture (recommended)

1. **AISecurityModel nb01 – nb06** *(this repo, ~6 hours total)* — foundational attacks and defence-in-depth.
2. **AISecurityModel nb07 – nb15** *(this repo, optional, ~12 hours total)* — advanced operations, fine-tuning, industry-specific compliance, incident response.
3. **AISecurityModel nb16 – nb18** *(this repo, ~5 hours total)* — agents/MCP, RAG, harness paradigm.
4. **harmless-harnesses F0 / F1 / F2** *(sibling course, foundations track)* — the paradigm explicitly, with the IDSov boundary statement.
5. **harmless-harnesses C / P / T / CAP tracks** *(sibling course, ~20+ modules)* — components, protocol, tensions, capstone.
6. **sa-sovereign-llm-harness `docs/REGULATOR_WALK.md` + `docs/complete-evidence-summary-may-2026.md`** *(research repo, ~1 hour)* — empirical evidence the architecture works.

### Path 2 — Instructor or trainer planning a course

- For a **2-hour to full-day workshop**: AISecurityModel nb01 – nb06 plus selected demos. See [`EDUCATOR_GUIDE.md`](EDUCATOR_GUIDE.md) Formats 1–2.
- For a **4-week course**: AISecurityModel nb01 – nb15. See [`EDUCATOR_GUIDE.md`](EDUCATOR_GUIDE.md) Format 3.
- For a **5-day intensive**: AISecurityModel nb01 – nb18 (full course). See [`EDUCATOR_GUIDE.md`](EDUCATOR_GUIDE.md) Format 5.
- For a **graduate seminar combining attacks and architecture**: AISecurityModel nb01 – nb18 *and* harmless-harnesses F0 / F2 / C / CAP. Plan one semester (12–14 weeks).

### Path 3 — Practitioner who already knows the model-layer attacks

Skip to AISecurityModel nb16 – nb18, then go directly to `harmless-harnesses`. Use `sa-sovereign-llm-harness` as the citable evidence base when justifying the architecture to a sponsor.

### Path 4 — Researcher, regulator, or procurement reviewer

Start with `sa-sovereign-llm-harness` `docs/AI_Sovereignty_Concept_Note_IMRAD_v5.docx` and `docs/complete-evidence-summary-may-2026.md`. Use AISecurityModel nb01 – nb06 as a working-example attack corpus. Use `harmless-harnesses` F0 / F2 / CAP for the conceptual structure underpinning the harness model.

---

## 🌏 The Indigenous-data-sovereignty positioning

The author, **Ben Kereopa-Yorke**, is an Indigenous Australian scholar (the foundational paper, [*The Harness Paradigm*](https://github.com/Benjamin-KY/sa-sovereign-llm-harness/blob/main/docs/the-harness-paradigm.md), is in the research repo). The positioning around IDSov is non-negotiable across all three repositories and is summarised here for completeness:

- **`sa-sovereign-llm-harness`** carries the full, primary positioning — including Tynan 2023, the CARE Principles, Maiam nayri Wingara, and IEEE 2890-2025 framing.
- **`harmless-harnesses`** ports the positioning verbatim into its F0 §6 (boundary statement) and F2 §6 (worked-example trade-offs), with explicit author approval and a note that it is verbatim.
- **`AISecurityModel`** (this repo) references the positioning at nb18 (capstone) and links out for the full treatment. This repository does not attempt to relitigate the positioning — it defers to the source.

Practitioners deploying into contexts where CARE / Indigenous-led governance applies must treat that framework as load-bearing alongside (and sometimes overriding) anything taught in this repository's notebooks. The phrase used across all three repos is:

> *"reduces specified harm classes when preconditions hold"* — not *"cannot harm."*

---

## 🔬 What about the research paper(s)?

Two academic papers are in scope across this constellation, currently in author-approved planning:

1. **Paper #1 — SA-GOV-BENCH (empirical)**, target NeurIPS 2027 / ACL 2027, lead repo `sa-sovereign-llm-harness`. Empirical results from the May 2026 study; lead author Ben Kereopa-Yorke.
2. **Paper #2 — Structural critique of the harness paradigm**, target FAccT 2027 (AIES 2027 backup), lead author Ben Kereopa-Yorke, with section-level co-authorship for §3.3 from an IDSov scholar via Maiam nayri Wingara outreach. Critique-first ordering: paper #2 submits Feb 2027, publishes Jun 2027; paper #1 submits May 2027, publishes Dec 2027.

This repository (`AISecurityModel`) is the **training-and-teaching arm** of that body of work. It exists to teach the layer below the harness; it does not need to ship a paper itself.

---

## 🤝 Cross-links you should add to your own materials

If you are linking to this repository from a syllabus, a blog post, a paper, or a community resource, please consider also linking to:

- **The architectural sibling:** [`harmless-harnesses`](https://github.com/Benjamin-KY/Harmless-Harnesses) — "Architecture, not hope."
- **The research basis:** [`sa-sovereign-llm-harness`](https://github.com/Benjamin-KY/sa-sovereign-llm-harness) — SA-GOV-BENCH.
- **The author's profile:** [@Benjamin-KY](https://github.com/Benjamin-KY).

A learner who finds only this repository sees one face of a much bigger argument. The cross-links protect the integrity of the IDSov positioning and make sure no-one mistakes the attacks course for the whole project.

---

## 📅 Version history

- **v1.0 (2026-06-15)** — Initial release as part of AISecurityModel v2.4.0 strategic-positioning push.
