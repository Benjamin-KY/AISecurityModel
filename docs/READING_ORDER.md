# 📚 Reading order — AISecurityModel + the harness paradigm

**Companion to:** [`POSITIONING.md`](POSITIONING.md). Read that first if you have not.
**Last updated:** 2026-06-15
**Scope:** Concrete, operational study orders across this repository and its two siblings ([harmless-harnesses](https://github.com/Benjamin-KY/Harmless-Harnesses), [sa-sovereign-llm-harness](https://github.com/Benjamin-KY/sa-sovereign-llm-harness)).

> If `POSITIONING.md` answers *"why do these three repos exist?"*, this document answers *"which file do I open on Monday morning, in what order, for how many hours?"*

---

## 🧭 Quick lookup — which path is mine?

| You are a... | Start here |
|---|---|
| Self-paced learner with Python | [Path A — Full curriculum](#path-a--full-curriculum-self-paced-learner) |
| Engineer at a company shipping LLM features | [Path B — Working engineer (fastest viable)](#path-b--working-engineer-fastest-viable) |
| Instructor planning a workshop or course | [Path C — Instructor / trainer](#path-c--instructor--trainer) |
| Researcher writing in this space | [Path D — Researcher / graduate student](#path-d--researcher--graduate-student) |
| Regulator or procurement reviewer | [Path E — Regulator / procurement](#path-e--regulator--procurement) |
| Executive / sponsor / board reviewer | [Path F — Executive briefing](#path-f--executive-briefing-90-minutes) |

---

## ⏱ Time budgets at a glance

| Layer | Repo | Material | Time |
|---|---|---|---|
| Foundational attacks | AISecurityModel | nb01–nb06 | ~6 h |
| Advanced attacks & operations | AISecurityModel | nb07–nb15 | ~12 h |
| Architectural bridge | AISecurityModel | nb16–nb18 | ~5 h |
| **AISM subtotal** | | **18 notebooks** | **~23 h** |
| Architectural foundation | harmless-harnesses | F0–F3 | ~4.25 h |
| Concept track | harmless-harnesses | C1–C7 | ~5.75 h |
| Practitioner track | harmless-harnesses | P1–P11 | ~11.75 h (+ 10–15 h exercises) |
| Tensions track | harmless-harnesses | T1–T4 | ~3 h |
| Capstones | harmless-harnesses | Concept + Practitioner | ~6–10 h / ~20–40 h |
| **HH subtotal (full course, both tracks, both capstones)** | | | **~50–80 h** |
| Empirical evidence read | sa-sovereign-llm-harness | concept note + evidence summary | ~1 h |
| Reproducing the SA-GOV-BENCH study | sa-sovereign-llm-harness | docker stack + walk | ~3 h |
| **Whole constellation** | | | **~75–110 h end to end** |

Use these as upper bounds; you do not need to do everything to extract value.

---

## Path A — Full curriculum (self-paced learner)

**Profile:** You can write Python, you want the complete story, and you have weeks (not days) to spend.

**Total:** ~50–70 h spread over 8–12 weeks.

### Week 1–2 — Foundational attacks (AISecurityModel)

| Notebook | Time | What you'll be able to do after |
|---|---|---|
| nb01 — Introduction & quickstart | ~45 min | Load the vulnerable adapter; reproduce one attack end-to-end |
| nb02 — Jailbreaking & adversarial prompts | ~60 min | Build and detect 5 jailbreak families |
| nb03 — Prompt injection & system extraction | ~60 min | Recognise direct vs. indirect injection patterns |
| nb04 — Multi-turn attacks & Skeleton Key | ~60 min | Walk a model through a multi-turn drift attack |
| nb05 — Encoding, jailbreaks & obfuscation | ~60 min | Decode 8+ encoding evasions; build a normalisation pipeline |
| nb06 — Defence: real-world application | ~75 min | Map a defence-in-depth stack onto an Australian regulatory case |

**Gate:** You should be able to explain *why* a defence-in-depth stack at the prompt boundary is necessary but not sufficient. If you can't, repeat nb06.

### Week 3–4 — Advanced operations (AISecurityModel)

Choose the notebooks closest to your role. **Read** all section headers; **execute** the ones you'll actually use.

| Notebook | Time | Skip if you... |
|---|---|---|
| nb07 — Automated red-teaming (gold-standard pedagogy) | ~90 min | (don't skip; the patterns here apply to every subsequent notebook) |
| nb08 — Prompt engineering for safety | ~75 min | are not writing or reviewing prompts |
| nb09 — Monitoring & observability | ~75 min | are not on-call for an LLM product |
| nb10 — Evaluation & benchmarking | ~75 min | are not measuring model safety |
| nb11 — Industry-specific security (AU compliance) | ~75 min | are not deploying in AU/regulated industry |
| nb12 — Fine-tuning robustness | ~75 min | are not fine-tuning models |
| nb13 — Multi-modal security | ~60 min | are not handling images/audio |
| nb14 — AI supply chain security | ~60 min | are not procuring AI components |
| nb15 — Incident response & forensics | ~90 min | are not on the incident-response roster |

### Week 5 — Architectural bridge (AISecurityModel)

| Notebook | Time | What you'll be able to do after |
|---|---|---|
| nb16 — Agent & MCP tool misuse | ~90 min | Identify confused-deputy and tool-output indirect-injection failures |
| nb17 — RAG-layer prompt injection | ~90 min | Build a poisoned-document detection pipeline; design RAG defences |
| nb18 — Harness paradigm capstone | ~90 min | Distinguish a model-layer defence from an architectural one; recognise the IDSov hand-off |

**Gate:** You should be able to explain — in your own words — *why* prompt-engineering defences cannot fix the failures in nb16 and nb17. The answer should reach for "different layer."

### Week 6 — Architectural foundation (harmless-harnesses F-track)

Move to the [`harmless-harnesses`](https://github.com/Benjamin-KY/Harmless-Harnesses) repo.

| Module | Time | Why now |
|---|---|---|
| F0 — The paradigm | ~60 min | The reasoning AISM nb18 introduced, now stated formally + IDSov boundary statement |
| F1 — Reference architecture | ~75 min | The five components and five invariants — name everything |
| F2 — Harm archetypes | ~75 min | Robodebt + the archetype matrix |
| F3 — Harness considered structurally | ~45 min | Category-error inoculation; T-track preview |

### Week 7–8 — Concept *or* Practitioner track (harmless-harnesses)

Choose one (or do both):

- **Concept track (C1–C7, ~5.75 h, no coding):** Decision-makers, architects, reviewers, policy people.
- **Practitioner track (P1–P11, ~11.75 h taught + 10–15 h exercises, Python):** Engineers who will actually build a harness.

### Week 9 — Tensions track (harmless-harnesses)

**Required if you plan to make any public claim that a deployment is "harness-conformant."** T1–T4 (~3 h) define what the harness pattern does and does *not* entitle you to say.

### Week 10–12 — Capstone (harmless-harnesses)

Pick the capstone matching your track. Concept Capstone: ~6–10 h, 6–10 pp design doc. Practitioner Capstone: ~20–40 h, working harness + write-up + structural threat model.

### Optional supplement — Empirical evidence (sa-sovereign-llm-harness)

After the capstone, ~1–3 h. Read `docs/REGULATOR_WALK.md` and `docs/complete-evidence-summary-may-2026.md`. Optionally `docker compose up --build` to reproduce the demo locally.

---

## Path B — Working engineer (fastest viable)

**Profile:** You ship LLM features today. You need *enough* to not embarrass yourself, fast.

**Total:** ~16 h spread over 2 weeks.

| Day | Material | Goal |
|---|---|---|
| 1 | AISM nb01 + nb02 + nb03 | Reproduce three live attacks against your own product |
| 2 | AISM nb06 | Defence-in-depth at your prompt boundary |
| 3 | AISM nb09 + nb10 | Stand up observability + a real eval |
| 4 | AISM nb16 + nb17 | Tool/agent + RAG failure modes |
| 5 | AISM nb18 | Identify which of your current "defences" are model-layer vs architectural |
| 6 | HH F0 + F1 + F2 | Get the architectural vocabulary |
| 7 | HH P3 (policy router) + P5 (governance prompt) + P6 (citation enforcement) | Wire three real components into your stack |
| 8 | HH T1 + T2 | Know what you can and cannot publicly claim |

**Gate:** Can you write a one-page memo to your team that distinguishes the three layers (prompt / model / architectural) and names which defences your product has at each layer? If yes, you have the working baseline.

---

## Path C — Instructor / trainer

**Profile:** You teach this material. You need a syllabus, a time budget, and clear assessment hooks.

### Format mapping

| Format | Material | Reference |
|---|---|---|
| 2-hour seminar | AISM nb01 + nb02 + nb18 (high-level only) | [`EDUCATOR_GUIDE.md` Format 1](EDUCATOR_GUIDE.md#course-formats) |
| Full-day workshop | AISM nb01–nb06 + nb16–nb18 hands-on | [`EDUCATOR_GUIDE.md` Format 2](EDUCATOR_GUIDE.md#course-formats) |
| 4-week course (3 h/wk) | AISM nb01–nb15 | [`EDUCATOR_GUIDE.md` Format 3](EDUCATOR_GUIDE.md#course-formats) |
| Self-paced semester | AISM nb01–nb18 + Path A weeks 6–12 | [`EDUCATOR_GUIDE.md` Format 4](EDUCATOR_GUIDE.md#course-formats) |
| 5-day intensive (full curriculum) | AISM nb01–nb18 | [`EDUCATOR_GUIDE.md` Format 5](EDUCATOR_GUIDE.md#course-formats) |
| Graduate seminar (one semester) | AISM nb01–nb18 + HH F+C+T tracks | [Combined syllabus skeleton](#combined-syllabus-skeleton-one-semester) below |

### Combined syllabus skeleton (one semester, 12–14 weeks)

Three-hour weekly sessions; ~6 h reading per week.

| Week | This repo (AISM) | Sibling repo (HH) | Assessment artefact |
|---|---|---|---|
| 1 | nb01 + nb02 | — | reproduce 3 attacks (lab notebook) |
| 2 | nb03 + nb04 | — | multi-turn drift writeup |
| 3 | nb05 + nb06 | — | defence-in-depth memo |
| 4 | nb07 + nb08 | — | red-team report against own product |
| 5 | nb09 + nb10 | — | eval suite design |
| 6 | nb11 + nb12 | — | AU compliance crosswalk |
| 7 | nb13 + nb14 + nb15 | — | incident-response runbook |
| 8 | nb16 + nb17 | — | tool/RAG failure-mode catalogue |
| 9 | nb18 | F0 + F1 | architectural-vs-model defence taxonomy |
| 10 | — | F2 + F3 + C1 | Robodebt archetype mapping |
| 11 | — | C2 + C3 + C4 | five-invariants critique |
| 12 | — | T1 + T2 + T3 + T4 | harness-washing structural critique |
| 13 | — | Concept Capstone work | 6–10 pp design doc |
| 14 | — | Concept Capstone presentation | peer-reviewed defence |

The graduate-seminar variant adds HH Practitioner Capstone for Python-comfortable students (extend to 16 weeks or carry into a second semester).

### Assessment hooks already built into the materials

- **AISM:** quizzes are embedded inline in each notebook; an end-of-course assessment template exists in [`EDUCATOR_GUIDE.md`](EDUCATOR_GUIDE.md#assessment).
- **HH:** every module ships ConcepTests + 3 exercises; capstones have full rubrics (`brief.md` + `template.md` + `rubric.md` + `exemplar.md`).
- **Cross-repo:** at the AISM/HH boundary (after nb18), have students complete the harness-washing case study from HH T1 against their AISM nb06 defence-in-depth memo. This catches the F3 category error.

---

## Path D — Researcher / graduate student

**Profile:** You are writing in this space. You need the citable corpus, the methodology, and an explicit map of what each artefact claims.

**Total:** ~10–15 h reading + research-specific reproduction time.

| Order | Material | Why |
|---|---|---|
| 1 | `sa-sovereign-llm-harness` → `docs/AI_Sovereignty_Concept_Note_IMRAD_v5.docx` | The full concept note (IMRAD) |
| 2 | `sa-sovereign-llm-harness` → `docs/the-harness-paradigm.md` | The paradigm paper (paper #1 source) |
| 3 | `sa-sovereign-llm-harness` → `docs/complete-evidence-summary-may-2026.md` | Empirical results |
| 4 | `harmless-harnesses` → F0 + C2 + T1–T4 | Conceptual + structural-critique scaffolding (paper #2 territory) |
| 5 | AISM → `docs/POSITIONING.md` + nb18 | Pedagogical translation of the paradigm |
| 6 | `sa-sovereign-llm-harness` → `docker compose up --build` + `docs/REGULATOR_WALK.md` | Reproduce the demo |
| 7 | (optional) `sa-sovereign-llm-harness` → full eval reproduction | Reproduce SA-GOV-BENCH |

**Citation guidance:** see each repo's `CITATION.cff`. The empirical work cites `sa-sovereign-llm-harness`; the pedagogical work cites this repo. The architectural-paradigm work cites the paper directly (not the GitHub URLs).

---

## Path E — Regulator / procurement

**Profile:** You evaluate AI deployments for compliance, procurement, or oversight. You do not need to write code, but you need to know what *good* and *bad* look like and what claims to challenge.

**Total:** ~6 h.

| Order | Material | Time | Take-away |
|---|---|---|---|
| 1 | AISM `README.md` + `docs/POSITIONING.md` | ~30 min | What this whole constellation is |
| 2 | AISM nb06 (defence: real-world application) | ~75 min | What a model-layer defence stack looks like; AU regulatory crosswalk |
| 3 | AISM nb11 (industry-specific security) | ~75 min | AU compliance specifics — Privacy Act post-2024 reform, ACSC E8, APRA CPS 234 |
| 4 | AISM nb14 (AI supply chain security) | ~60 min | What to ask in procurement |
| 5 | AISM nb18 (harness paradigm capstone) | ~90 min | The layer above model — what "harness" means architecturally |
| 6 | HH F0 + F1 + F2 + C7 (governance regimes + compliance scaffold) | ~4 h | The architectural vocabulary + the compliance scaffold |
| 7 | HH T1 (harness-washing and certification capture) | ~45 min | **Critical**: what to challenge in any "we are harness-conformant" claim |
| 8 | sa-sovereign-llm-harness `docs/REGULATOR_WALK.md` | ~30 min | Walk-through of a working public-sector evaluation |

**Challenge prompts to bring to vendor reviews** (from HH T1 and AISM nb18):

- "Show me the prompt-boundary defences *and* the architectural defences. Which failures does each layer cover?"
- "Where in your stack is the policy router? What does its YAML look like? Who reviews changes?"
- "What is your citation-enforcement mechanism? What happens when a cited source is not in the supplied context?"
- "What does your audit log capture about routing, retrieval, and refusal? Can a regulator reconstruct a single decision end-to-end?"
- "What harm classes does your harness *not* reduce? When do its preconditions fail?"

---

## Path F — Executive briefing (90 minutes)

**Profile:** You sponsor or sign off on AI work. You have 90 minutes.

| Order | Material | Time |
|---|---|---|
| 1 | AISM `README.md` (Overview + Disclaimer sections) | ~10 min |
| 2 | AISM `docs/POSITIONING.md` (full) | ~20 min |
| 3 | AISM nb18 (read narrative; skip code execution) | ~30 min |
| 4 | HH F0 (read narrative; skip notebook) | ~20 min |
| 5 | sa-sovereign-llm-harness `docs/complete-evidence-summary-may-2026.md` | ~10 min |

**What you should walk away knowing:**

- AI security has at least two layers (model/prompt and architectural).
- Defending only at the prompt boundary is necessary but not sufficient.
- "We have a safety prompt" is not the same as "we have a harness."
- Empirical evidence exists that architectural harnesses add measurable value, especially for cheaper models.
- The IDSov positioning is non-negotiable and outranks the architecture in contexts where it applies.

---

## 🪪 Prerequisites cheat sheet

| Material | Required preparation |
|---|---|
| AISM nb01–nb06 | Python 3.11+, comfort with Jupyter, basic LLM intuition |
| AISM nb07–nb15 | nb01–nb06 + comfort with `transformers`, fine-tuning, ML evaluation |
| AISM nb16–nb18 | nb01–nb06 + basic understanding of agents/tool-calling and RAG |
| HH F0–F3 | None (reading only) |
| HH C1–C7 | F0–F2 (reading only) |
| HH P1–P11 | F0–F3 + Python; AISM nb01–nb06 strongly recommended for the "what attacks?" context |
| HH T1–T4 | F0–F3 (T-track is critique, not implementation) |
| HH Concept Capstone | F0–F3 + C1–C7 + T1–T4 (T-track integration is graded) |
| HH Practitioner Capstone | F0–F3 + C1–C7 + P1–P11 + T1–T4 (structural threat model is graded) |
| sa-sovereign-llm-harness demo | Docker; no API keys needed |
| sa-sovereign-llm-harness full eval | API budget for 6 frontier models; ~12,600 scored items |

---

## 🔁 Cross-repo hand-offs (where one repo explicitly defers to another)

| From | Hands off to | What |
|---|---|---|
| AISM nb18 | HH F0, F1, F2 | "the harness paradigm is taught fully in this sibling course" |
| AISM nb18 | sa-sovereign-llm-harness `docs/the-harness-paradigm.md` | "the paradigm paper itself, with the IDSov positioning" |
| HH F0 §6 | sa-sovereign-llm-harness `docs/the-harness-paradigm.md` | IDSov boundary statement (verbatim with author approval) |
| HH F2 §6 | sa-sovereign-llm-harness `docs/the-harness-paradigm.md` | Worked-example trade-offs |
| HH C3 | sa-sovereign-llm-harness `docs/complete-evidence-summary-may-2026.md` | Empirical evidence |
| sa-sovereign-llm-harness README | (back) AISM, HH | Cross-link block in README footer |

These hand-offs are intentional — no single repo carries the whole story.

---

## 📅 Version history

- **v1.0 (2026-06-15)** — Initial release alongside AISecurityModel v2.4.0.
