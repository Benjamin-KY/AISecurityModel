# 🎓 Educator Guide: AI Security Education Model

**Version:** 2.0
**Last Updated:** 2026-06-15
**Target Audience:** Educators, trainers, and facilitators teaching AI security
**Course Scope:** 18 notebooks across foundational (1-6), advanced (7-15), and 2026 Architectural Capstone (16-18) tracks

> **v2.0 scope note:** This guide was originally written for the 6-notebook v1.0 course. Modules 1-6 below retain the full pedagogical treatment (key concepts, teaching tips, common issues, discussion prompts, assessment ideas). Modules 7-15 are summarised in a condensed reference table — the underlying notebooks already ship with prerequisites, exercises, and "try-it-yourself" cells (Phase 3 refactor, v2.2.x) that provide much of this support inline. Modules 16-18 (the **2026 Architectural Capstone Track**, added in AISecurityModel v2.3.0) receive full v1.0-style treatment because they introduce a paradigm shift — from model-layer to **architectural-layer** defences.

---

## 📋 Table of Contents

1. [Overview](#overview)
2. [Learning Outcomes](#learning-outcomes)
3. [Prerequisites](#prerequisites)
4. [Course Formats](#course-formats)
5. [Module Breakdown](#module-breakdown)
   - Notebooks 1-6 (Foundational track — full pedagogical treatment)
   - Notebooks 7-15 (Advanced track — condensed reference table)
   - Notebooks 16-18 (2026 Architectural Capstone Track — full treatment)
6. [Assessment & Rubrics](#assessment--rubrics)
7. [Technical Setup](#technical-setup)
8. [Safety & Ethics](#safety--ethics)
9. [Discussion Questions](#discussion-questions)
10. [Troubleshooting](#troubleshooting)
11. [Additional Resources](#additional-resources)

---

## 🎯 Overview

### What Is This Course?

This is a hands-on AI security education programme designed to teach students about Large Language Model (LLM) vulnerabilities through practical experimentation with an **intentionally vulnerable** model.

### The Vulnerable-Then-Educate Approach

Unlike traditional security courses that only describe attacks theoretically, this course:

1. **Allows students to execute real attacks** against a vulnerable model
2. **Demonstrates why attacks succeed** through immediate feedback
3. **Teaches defence strategies** with code examples
4. **Provides Australian context** for compliance and regulations

### Why This Matters for Australian Students

- **Privacy Act 1988** (post-2024 reform): Organisations must protect personal information in AI systems. The Privacy and Other Legislation Amendment Act 2024 (assented 10 Dec 2024) replaced the old $2.5M single-ceiling penalty with a tiered model: **up to $50M / 3× benefit / 30% adjusted turnover** for serious or repeated interferences with privacy; **$66k entity / $33k individual** standard tier. A new statutory tort for serious invasions of privacy commenced 10 Jun 2025.
- **ACSC Essential Eight**: Security controls increasingly apply to AI applications
- **Growing AI deployment**: Australian businesses rapidly adopting customer-facing AI
- **Skills shortage**: Critical need for AI security professionals

---

## 🎓 Learning Outcomes

### Core Competencies

By completing this course, students will be able to:

#### Technical Skills
- Execute prompt injection attacks (basic to advanced)
- Identify encoding-based bypasses (Base64, ROT13, hex)
- Perform role-playing and context manipulation attacks
- Extract system prompts and internal instructions
- Chain multiple attack techniques together
- Analyse model internals using attention visualisation
- Build comprehensive defence systems

#### Architectural / Harness Layer (Notebooks 16-18, added 2026)
- Identify architectural-layer attack surfaces (agent tool-calls, MCP servers, RAG retrieval indices) that bypass all model-and-prompt-layer defences from notebooks 1-15
- Recognise indirect prompt injection via tool outputs and retrieved documents
- Design a `GovernanceHarness` with source registry, router, verifier, and decision logger components
- Reason about confused-deputy, over-privileged-tool, and document-poisoning failure modes
- Distinguish between **model-layer** defences (filter the model's behaviour) and **architectural-layer** defences (constrain the system around the model)
- Map the harness-paradigm critique to Indigenous-data-sovereignty positioning (per `docs/the-harness-paradigm.md` in the source paper)

#### Conceptual Understanding
- Explain why LLMs are vulnerable to jailbreaks
- Distinguish between different vulnerability categories
- Evaluate the effectiveness of defence strategies
- Apply security principles to real-world AI systems
- Consider ethical implications of AI security work

#### Australian Context
- Navigate Privacy Act 1988 requirements for AI systems
- Apply ACSC Essential Eight controls to LLM deployment
- Understand Australian AI Ethics Framework principles
- Recognise compliance obligations for organisations
- Assess legal implications of AI security breaches

---

## 📚 Prerequisites

### Required Knowledge

**Students should have:**
- Basic Python programming (variables, functions, loops)
- Understanding of what AI/LLMs are conceptually
- Familiarity with command-line interfaces
- Basic understanding of cybersecurity concepts

**Students do NOT need:**
- Deep learning expertise
- Prior security/pentesting experience
- Advanced mathematics
- Existing knowledge of prompt engineering

### Technical Requirements

**Per Student:**
- Google Account (for Colab) OR local GPU (RTX 3060 12GB+)
- Stable internet connexion
- Modern web browser (Chrome, Firefox, Edge, Safari)

**For Instructor:**
- Same as above
- Ability to share screen/demonstrate
- Access to example outputs for comparison

---

## 📅 Course Formats

This material is flexible and can be adapted to various formats:

### Format 1: 2-Hour Workshop (Introductory)

**Target:** General awareness, executives, compliance officers

**Content:**
- Notebook 1 only: Introduction & First Jailbreak
- Brief demonstration of Notebooks 2-3
- Discussion of real-world implications

**Learning Outcomes:**
- Understand that jailbreaks exist and are relatively easy
- Recognise the business risk to organisations
- Appreciate the need for AI security controls

### Format 2: Full-Day Workshop (Hands-On)

**Target:** Developers, IT security staff, researchers

**Content:**
- Notebooks 1-3: Introduction through Intermediate Attacks
- Hands-on exercises throughout
- Group discussion on defence strategies

**Learning Outcomes:**
- Execute basic and intermediate jailbreaks
- Understand encoding and multi-turn attacks
- Begin thinking about defence architecture

### Format 3: 4-Week Course (Comprehensive)

**Target:** University students, professional development, security teams

**Schedule:**

**Week 1: Foundations**
- Notebook 1: Introduction & First Jailbreak
- Notebook 2: Basic Jailbreak Techniques
- **Assessment:** Execute 5 different DAN variants

**Week 2: Intermediate Techniques**
- Notebook 3: Encoding & Crescendo Attacks
- Group project: Build attack library
- **Assessment:** Chain 3+ techniques together

**Week 3: Advanced Attacks & Analysis**
- Notebook 4: Skeleton Key & Advanced Jailbreaks
- Notebook 5: XAI & Interpretability
- **Assessment:** Analyse model internals during attack

**Week 4: Defence & Real-World Application**
- Notebook 6: Defence Architecture
- Final project: Build secure AI system
- **Assessment:** Defend against 10 attack types

### Format 4: Self-Paced Online Course

**Target:** Independent learners, remote teams

**Structure:**
- All 18 notebooks available immediately
- Suggested pace: 1 notebook per week (4-month total) or 2 notebooks per week (2-month intensive)
- Discussion forum for questions
- Weekly office hours (optional)
- Final certification exam

### Format 5: 5-Day Intensive (Full Curriculum)

**Target:** Cohort training, security teams, professional bootcamps, post-grad short courses

**Schedule:**

**Day 1: Foundations (Notebooks 1-3)**
- Morning: Introduction, first jailbreak, DAN variants
- Afternoon: Encoding attacks, Crescendo
- **Assessment:** Execute 5 attack variants; document success rates

**Day 2: Model-Layer Attacks & Analysis (Notebooks 4-6)**
- Morning: Skeleton Key, system-prompt extraction, XAI/interpretability
- Afternoon: Defence-in-depth architecture, Australian Privacy Act compliance
- **Assessment:** Build a 7-layer defence and measure block rate

**Day 3: Operations & Tooling (Notebooks 7-9)**
- Morning: Automated red-teaming, prompt-engineering for safety
- Afternoon: Real-time monitoring dashboard, SIEM integration
- **Assessment:** Wire automated tests into a CI/CD job

**Day 4: Advanced & Industry (Notebooks 10-15)**
- Morning: CTF challenges, industry-specific compliance (healthcare/finance/gov/retail)
- Afternoon: Fine-tuning for robustness, multi-modal security, supply-chain, incident response/forensics
- **Assessment:** Complete 10 CTF challenges; write an NDB-compliant incident timeline

**Day 5: 2026 Architectural Capstone Track (Notebooks 16-18)**
- Morning: Agent/MCP tool misuse, RAG-layer prompt injection
- Afternoon: The Harness Paradigm capstone, hand-off to `harmless-harnesses`
- **Final project:** Build a `GovernanceHarness` for a chosen domain (healthcare, gov, etc.); pass the four ablation checks from nb18

**Learning Outcomes:**
- Cover the full course in a compressed, instructor-led format
- Understand both **model-layer** and **architectural-layer** defence paradigms
- Be positioned to continue with the [`harmless-harnesses`](https://github.com/Benjamin-KY/Harmless-Harnesses) course on harness design

---

## 📖 Module Breakdown

### Notebook 1: Introduction & First Jailbreak (30-45 minutes)

**🟢 Difficulty:** Beginner

**Key Concepts:**
- What is a jailbreak?
- The DAN (Do Anything Now) attack
- Why models are vulnerable
- Vulnerable-then-educate pattern

**Teaching Tips:**
- Start with live demonstration
- Let students experience their first successful jailbreak
- Emphasise that this is EASIER than they think
- Connect to real-world chatbot deployments

**Common Issues:**
- Students may feel uncomfortable "attacking" the AI
  - **Solution:** Remind them this model is intentionally vulnerable for learning
- Some may struggle with Google Colab setup
  - **Solution:** Have a pre-run notebook ready to share

**Discussion Prompts:**
- "How would you feel if your company's chatbot could be jailbroken this easily?"
- "What Australian organisations are most at risk?"
- "Should there be regulations requiring jailbreak testing?"

**Assessment Ideas:**
- Execute 3 different jailbreak attempts
- Explain why each one worked
- Identify the Australian regulatory implications

---

### Notebook 2: Basic Jailbreak Techniques (45-60 minutes)

**🟢 Difficulty:** Beginner

**Key Concepts:**
- DAN variants (6.0, 7.0, 8.0, 11.0)
- Evolution of jailbreak techniques
- Role-playing attacks
- Multi-turn conversation attacks
- Success rate measurement

**Teaching Tips:**
- Show how attackers iterate and improve techniques
- Explain why DAN 11.0 was more effective than DAN 1.0
- Have students create their own DAN variant
- Discuss the "arms race" between attackers and defenders

**Hands-On Exercise:**
- Build a custom DAN variant
- Test it against the vulnerable model
- Measure success rate across 10 attempts
- Share results with class

**Common Issues:**
- Students may think older techniques don't matter
  - **Solution:** Explain that many production systems are still vulnerable to DAN 1.0
- Some may want to test on production chatbots
  - **Solution:** Emphasise ethical boundaries and authorisation requirements

**Discussion Prompts:**
- "Why do you think role-playing attacks are so effective?"
- "How might an organisation detect DAN attempts in their logs?"
- "What's the difference between security research and unauthorised testing?"

**Assessment Ideas:**
- Create 5 unique role-playing attack variants
- Document success rates and patterns
- Write a brief report on findings

---

### Notebook 3: Intermediate Attacks (60-90 minutes)

**🟡 Difficulty:** Intermediate

**Key Concepts:**
- Base64 encoding attacks
- ROT13 and other encoding schemes
- Crescendo (gradual escalation over multiple turns)
- Prompt injection fundamentals
- Attack chaining

**Teaching Tips:**
- Demonstrate encoding attacks live
- Show how simple encodings bypass keyword filters
- Explain why Crescendo is so effective (98%+ success rate)
- Have students combine techniques

**Advanced Exercise:**
- Chain together: Base64 + Role-playing + Crescendo
- Document each step of the attack
- Analyse why the combination is more effective

**Common Issues:**
- Students may think encoding is "too simple"
  - **Solution:** Show real-world examples where it bypassed production filters
- Crescendo attacks take time to develop
  - **Solution:** Provide template escalation sequences

**Discussion Prompts:**
- "Why doesn't Base64 encoding 'feel' like a sophisticated attack?"
- "How would you defend against Crescendo without context history?"
- "What Australian regulations apply to logging user conversations?"

**Assessment Ideas:**
- Build a 3-technique attack chain
- Achieve 80%+ success rate across 10 trials
- Document defence strategies for each technique

---

### Notebook 4: Advanced Jailbreaks (60-90 minutes)

**🔴 Difficulty:** Advanced

**Key Concepts:**
- Skeleton Key attack (Microsoft, June 2024)
- DAN 11.0 token system
- Context extraction techniques
- System prompt extraction
- Advanced prompt injection

**Teaching Tips:**
- Explain the history of Skeleton Key discovery
- Show how "augment" is psychologically different from "ignore"
- Demonstrate system prompt extraction risks
- Discuss zero-day vulnerabilities

**Real-World Case Study:**
Analyse the Microsoft Skeleton Key disclosure:
- How was it discovered?
- Why did it work on multiple models?
- How quickly was it patched?
- What does this tell us about the security landscape?

**Common Issues:**
- Students may want to find new zero-days
  - **Solution:** Discuss responsible disclosure processes
- Some may feel these attacks are "unethical"
  - **Solution:** Clarify defensive security vs offensive use

**Discussion Prompts:**
- "What's the ethical difference between discovering and publishing a vulnerability?"
- "Should AI companies pay bug bounties for jailbreaks?"
- "How does Australian law treat AI vulnerability disclosure?"

**Assessment Ideas:**
- Replicate Skeleton Key attack
- Extract the system prompt
- Document a new attack variant
- Submit via responsible disclosure process (to instructor)

---

### Notebook 5: XAI & Interpretability (90-120 minutes)

**🔴 Difficulty:** Advanced

**Key Concepts:**
- Attention mechanism visualisation
- Neural activation analysis
- Sparse Autoencoder (SAE) decomposition
- Identifying "jailbreak neurons"
- Mechanistic interpretability

**Teaching Tips:**
- This is the most technical notebook
- Focus on conceptual understanding first
- Use visualisations heavily
- Connect to cutting-edge research

**Research Connexions:**
- Anthropic's work on SAEs and interpretability
- OpenAI's superalignment team research
- Academic papers on LLM security

**Common Issues:**
- Students may struggle with the maths
  - **Solution:** Focus on intuition and visualisations
- Computational requirements may be higher
  - **Solution:** Provide pre-computed results as fallback

**Discussion Prompts:**
- "If we can identify 'jailbreak neurons', should we remove them?"
- "What are the trade-offs between interpretability and performance?"
- "How might mechanistic interpretability change AI regulation?"

**Assessment Ideas:**
- Visualise attention for 3 different attacks
- Identify which layers activate most strongly
- Hypothesise about model internals
- Write interpretability research proposal

---

### Notebook 6: Defence & Real-World Application (90-120 minutes)

**🔴 Difficulty:** Advanced

**Key Concepts:**
- Defence-in-depth architecture
- Input validation and sanitisation
- Output filtering
- Australian Privacy Act compliance
- ACSC Essential Eight application
- Real-world breach case studies

**Teaching Tips:**
- This is where everything comes together
- Emphasise that perfect security is impossible
- Focus on risk reduction and layered defences
- Use Australian case studies where possible

**Major Project: Build a Secure AI System**

Students design and implement a complete secure AI system with:
1. Input validation layer
2. Prompt sanitisation
3. Context isolation
4. Output filtering
5. Monitoring and logging
6. Privacy Act compliance
7. Incident response procedures

**Common Issues:**
- Students may aim for perfection
  - **Solution:** Teach risk management and acceptable residual risk
- Some may struggle with compliance aspects
  - **Solution:** Provide Privacy Act cheat sheet

**Discussion Prompts:**
- "What's an acceptable jailbreak success rate for a production system?"
- "How do you balance security with user experience?"
- "What should a company do after a jailbreak is discovered in production?"

**Assessment Ideas:**
- Build defence system that blocks 95%+ of known attacks
- Write Privacy Act 1988 compliance documentation (post-2024 reform: tiered penalty model up to $50M / 3× / 30% turnover)
- Create incident response playbook
- Present solution to class

---

### Notebooks 7-15: Condensed Reference

> **Why condensed:** Each of these notebooks ships with inline prerequisites, section headers, "try-it-yourself" exercise cells, and per-class explainer markdowns (per the v2.2.x Phase 3 pedagogical refactor). Use the table below as a planning aid; the notebooks themselves provide most teaching scaffolding.

| # | Title | Duration | Difficulty | Key Teaching Hooks | Assessment Anchor |
|---|-------|----------|------------|--------------------|-------------------|
| 7 | Automated Red Teaming & Testing | 90 min | 🔴 Advanced | The gold-standard pedagogical pattern (33 cells, prerequisites, CI/CD section). Use this notebook as a model for what student work should look like. | Wire an automated attack-template suite into a GitHub Actions workflow; measure ASR delta across two model checkpoints |
| 8 | Prompt Engineering for Safety | 75 min | 🟡 Intermediate | 10 hardening techniques, industry-specific templates. Pair with nb11 for an industry deep-dive. | Design a system prompt for one industry (healthcare/finance/gov/retail) and A/B-test it against the baseline |
| 9 | Real-time Monitoring Dashboard | 75 min | 🟡 Intermediate | Streamlit-based — students who completed Phase 3 already know small-cell refactoring won't split a triple-quoted string literal (cell 10 is intentionally monolithic). | Wire the dashboard to a Splunk/ELK sink (or stub) and define 3 alert rules |
| 10 | CTF Security Challenges | 120 min | 🔴 Advanced | 15 challenges, 500 points, 5 rank levels. Great mid-course energy boost; works well in pairs or small teams. | Earn the 3rd-tier "Defender" rank (≥250 points) |
| 11 | Industry-Specific AI Security | 90 min | 🟡 Intermediate | Healthcare (TGA/PBS), Finance (APRA CPS 234), Gov (PSPF/ISM), Retail (CDR/PCI DSS). All Privacy Act references use the post-2024 reform penalty figures. | Pick one industry; write a 2-page compliance gap analysis for a hypothetical AI deployment |
| 12 | Fine-tuning for Robustness | 120 min | 🔴 Advanced | Adversarial training, LoRA, the 45% → 4.8% ASR claim. Watch for compute requirements — may need a cloud GPU. | Train a robustness LoRA and report pre/post ASR on a held-out attack set |
| 13 | Multi-modal AI Security | 100 min | 🔴 Advanced | VLM security, OCR-based prompt injection, adversarial images. Extra requirement: `pytesseract` system binary. | Build an OCR-screening pipeline and break it with an adversarial image |
| 14 | AI Supply Chain Security | 90 min | 🔴 Advanced | Model provenance, AI-SBOM, data poisoning detection. The closest notebook to traditional appsec. | Generate an AI-SBOM for the course's own vulnerable model and identify 3 supply-chain risks |
| 15 | Incident Response & Forensics | 100 min | 🔴 Advanced | NDB scheme, OAIC 30-day notification, forensic timeline reconstruction. Capstone for the advanced track; closes the loop on Privacy Act material from nb6 and nb11. | Write a full NDB-compliant incident timeline for a fabricated jailbreak scenario; include OAIC notification draft |

**Common pedagogical pattern for nb7-15:**
1. Walk students through the prerequisites cell — they should not run anything until they understand what's required.
2. Demonstrate the first hands-on cell live, then let students drive.
3. Use the in-notebook "try-it-yourself" cells as in-class exercises rather than homework.
4. End each session with the discussion prompts in the final markdown cell.

---

### Notebook 16: Agent & MCP Tool-Misuse Security (90 minutes)

**🟣 Difficulty:** Advanced (2026 Architectural Capstone Track)

**Key Concepts:**
- Tool-calling agents (OpenAI function-calling, MCP servers)
- Indirect prompt injection — where the attacker never speaks to the model directly
- Confused-deputy and over-privileged-tool patterns
- Cross-tool data exfiltration (one tool reads, another exfiltrates)
- Defences: tool allowlists, output scoping, capability boundaries, per-tool authorisation

**Teaching Tips:**
- Open by explicitly framing the paradigm shift: "Everything we've taught for 15 notebooks lived at the model-and-prompt layer. From here on, the attacker doesn't need to defeat the model — they defeat the system *around* the model."
- Show the simplest possible MCP server example before showing the attack.
- Use a whiteboard to draw the agent loop (LLM → tool call → tool output → LLM) and mark where injection enters.
- Run the indirect-injection demo and pause: ask the class "where in the loop did the attack succeed?"

**Real-World Hooks:**
- The 2024-2025 wave of MCP server vulnerabilities (allow students to research and present one each)
- The Anthropic / Microsoft public discussions of agent confused-deputy risks
- Any agentic IDE / coding-assistant incident the class can find

**Common Issues:**
- Students who skipped nb1-15 will be lost — this notebook assumes literacy in direct prompt injection
  - **Solution:** Require nb1, nb3, nb6 as hard prerequisites; nb4 (Skeleton Key) strongly recommended
- The "agent loop" abstraction can feel hand-wavy
  - **Solution:** Have students draw the loop on paper before reading the code

**Discussion Prompts:**
- "If a tool's output can contain an injection, should we treat all tool outputs as untrusted input?"
- "What's the agent-layer analogue of input sanitisation? Is it even possible?"
- "How does Australia's Privacy Act 1988 apply when one tool reads personal info and another exfiltrates it via a benign-looking destination?"

**Assessment Ideas:**
- Identify an indirect-injection vector in a real OSS MCP server (responsibly — no live exploitation)
- Implement an allowlist + per-tool capability boundary in the notebook's example agent
- Write a 1-page threat model for a 3-tool agent of the student's design

---

### Notebook 17: RAG-Layer Prompt Injection (75 minutes)

**🟣 Difficulty:** Advanced (2026 Architectural Capstone Track)

**Key Concepts:**
- Document poisoning in retrieval indices (the attacker contributes documents; the model never sees an attacker prompt directly)
- Retrieved-context attacks at index time vs. query time
- Source provenance and trust scoring
- Citation enforcement as a defence primitive
- Why the input/output filters from nb6 don't help when the "input" is a chunk of trusted-looking text retrieved from your own index

**Teaching Tips:**
- Lead with the question: "If we trusted everything in our wiki, what happens when an attacker contributes one wiki page?"
- Have students do the index-poisoning exercise themselves with their own demo corpus — the visceral "huh, that worked" is the lesson.
- Spend at least 15 minutes on the *defence* half. The attack is one slide; the defence is the substance.

**Real-World Hooks:**
- Any of the 2024-2025 RAG-leak incidents (Slack, internal-wiki cases)
- Microsoft's Copilot connectors and the indirect-injection vectors they introduced
- The general OWASP LLM Top 10 entry for retrieval-pipeline risks

**Common Issues:**
- Students assume their existing input-filtering will catch it
  - **Solution:** Run the demo where the input-filter says "clean" and the model still complies — visceral and persuasive
- Citation enforcement feels "weak" as a defence
  - **Solution:** Frame it as an *audit primitive* and an *attacker-effort multiplier*, not a hard block

**Discussion Prompts:**
- "Whose corpus is it, anyway? Who has authority to add a document to your index?"
- "Should every retrieved chunk carry a provenance signature? Who would sign?"
- "Is RAG-layer injection a model problem or a documents-and-permissions problem?"

**Assessment Ideas:**
- Poison the notebook's example index with a malicious document; measure attack success
- Implement source-trust scoring (3 tiers minimum); re-measure
- Write a 1-page comparison of input-filtering (nb6) vs. provenance-based defence (nb17) — when does each fail?

---

### Notebook 18: The Harness Paradigm — Capstone (120 minutes)

**🟣 Difficulty:** Advanced / Synthesis (2026 Architectural Capstone Track)

**Key Concepts:**
- Reframing notebooks 1-17 as the *model-and-prompt layer*
- The **harness paradigm**: architectural defences *around* (not *inside*) the model
- The 4-component `GovernanceHarness`: **source registry**, **router**, **verifier**, **decision logger**
- Ablation studies showing what fails when any one of authority, enforcement, or audit is removed
- Explicit hand-off to the [`harmless-harnesses`](https://github.com/Benjamin-KY/Harmless-Harnesses) course
- Indigenous-data-sovereignty positioning of the paradigm (see `docs/the-harness-paradigm.md` in the research repo)

**Teaching Tips:**
- This is a **synthesis** notebook, not a new-content one. Spend the first 20 minutes recapping what students built across nb1-17 and asking "what didn't any of these protect against?"
- Build the `GovernanceHarness` live with the class, component by component. Pause after each component and ask "what new attack does *this* close? what does it *not* close?"
- The four ablation experiments are the assessment. Don't rush them.
- Close with the explicit hand-off: "if you want to go further on harness design, the next course is `harmless-harnesses` — it's the architectural curriculum to this course's attack curriculum."

**Pedagogical bugs to watch for** (caught and patched during v2.3.0 smoke testing, document in case they recur in student forks):
1. **Router case-sensitivity** — earlier draft used case-sensitive routing; students would fail trivially
2. **Narrow safety regex** — earlier draft missed obvious variants
3. **Ablation defeat** — earlier ablations were defeated by the verifier without the student noticing

**Real-World Hooks:**
- Microsoft's "harness" framing in agentic-AI security work
- Anthropic's constitutional classifiers as one harness component (not a complete harness)
- Australian Public Service AI use guidance — discuss whether it implicitly assumes a harness model

**Common Issues:**
- Students treat the harness as a single thing instead of a composition
  - **Solution:** Insist on the 4-component breakdown; require all four named in their submission
- Students underestimate the decision logger
  - **Solution:** Run an ablation that removes only the logger; ask "what postmortem can you do? what regulatory disclosure can you sign off on?"

**Discussion Prompts:**
- "Which of the 17 prior notebooks does the harness paradigm fully obsolete? Which does it amplify?"
- "Whose values are encoded in your router? Who can change them? Who audits them?"
- "How does the Indigenous-data-sovereignty critique in `docs/the-harness-paradigm.md` change the design of the source registry?"
- "If your organisation deployed a `GovernanceHarness` today, what *can't* you build that you could yesterday? Is that a cost or a feature?"

**Assessment Ideas:**
- Build a domain-specific `GovernanceHarness` (healthcare / public-service / education) with all 4 components named and justified
- Pass all four ablation experiments (each ablation must fail in the documented way)
- Write a 2-page reflection: "what would I need from `harmless-harnesses` to deploy this for real?"
- *Optional, advanced:* Read Ben Kereopa-Yorke's harness-paradigm paper (linked from `docs/the-harness-paradigm.md`) and write a 1-page response

---

## 📊 Assessment & Rubrics

### Formative Assessment (Throughout Course)

**Participation in Exercises (20%)**
- Active engagement with notebooks
- Attempting all hands-on challenges
- Asking questions and contributing to discussions

**Weekly Quizzes (20%)**
- Multiple choice and short answer
- Cover key concepts from each notebook
- Australian context questions

### Summative Assessment (End of Course)

**Attack Library Project (25%)**

Students build a library of 20+ jailbreak techniques:

| Criteria | Excellent (8-10) | Good (6-7) | Satisfactory (4-5) | Needs Improvement (0-3) |
|----------|------------------|------------|-------------------|------------------------|
| **Variety** | 20+ unique techniques across all categories | 15-19 techniques with good coverage | 10-14 techniques, some gaps | <10 techniques |
| **Documentation** | Detailed explanation for each, including why it works | Good explanations for most | Basic documentation | Minimal documentation |
| **Success Rates** | Empirical testing with statistics | Some testing done | Limited testing | No testing |
| **Originality** | Multiple novel variants | Some original techniques | Mostly standard techniques | All copied from course |

**Defence System Project (35%)**

Students build a comprehensive defence system:

| Criteria | Excellent (28-35) | Good (21-27) | Satisfactory (14-20) | Needs Improvement (0-13) |
|----------|------------------|------------|-------------------|------------------------|
| **Architecture** | All 7 defence layers implemented | 5-6 layers implemented | 3-4 layers implemented | <3 layers |
| **Effectiveness** | Blocks 95%+ of attacks | Blocks 80-94% | Blocks 60-79% | <60% blocked |
| **Code Quality** | Clean, documented, production-ready | Good code with minor issues | Functional but needs improvement | Significant issues |
| **Compliance** | Complete Privacy Act documentation | Good compliance coverage | Basic compliance | Missing compliance |
| **Testing** | Comprehensive test suite | Good testing | Basic testing | Minimal/no testing |

**Final Exam (20%)**

**Part A: Multiple Choice (10%)**
- 20 questions covering core concepts across all 18 notebooks (weight foundational 1-6 heavily, sample from 7-15, and include 1-2 questions per capstone notebook 16-18)
- Mix of technical and conceptual
- Australian context integration

**Part B: Practical Demonstration (10%)**
- Execute 3 assigned jailbreak techniques
- Build a defence against them
- Explain the underlying principles

### Example Questions

**Multiple Choice:**

1. Under the Privacy Act 1988, organisations must notify the OAIC of a data breach within how many days?
   - A) 7 days
   - B) 14 days
   - C) 30 days ✓
   - D) 90 days

2. Which DAN variant introduced a token reward system?
   - A) DAN 1.0
   - B) DAN 6.0
   - C) DAN 7.0 ✓
   - D) DAN 11.0

**Short Answer:**

3. Explain why Base64 encoding attacks can bypass keyword-based safety filters. Provide a defence strategy with pseudocode.

4. A healthcare chatbot in Melbourne has been jailbroken, potentially exposing patient information. List the steps required under Australian law and ACSC guidelines.

---

## 🖥️ Technical Setup

### Option 1: Google Colab (Recommended for Beginners)

**Advantages:**
- No local setup required
- Free GPU access (with limitations)
- Easy sharing and collaboration
- Works on any device with a browser

**Disadvantages:**
- Requires internet connexion
- Session timeouts after inactivity
- Limited to Colab's resources

**Setup Instructions:**

1. Navigate to: https://colab.research.google.com/
2. Upload notebook or use File → Upload notebook
3. Enable GPU: Runtime → Change runtime type → GPU → T4
4. Install requirements (first cell runs automatically)
5. Begin exercises

**Troubleshooting Colab:**
- **Session disconnects:** Colab free tier has time limits
  - Solution: Use Colab Pro or save work frequently
- **Out of memory:** Model too large for T4
  - Solution: Restart runtime, close other notebooks
- **Slow performance:** Free tier throttling
  - Solution: Use during off-peak hours or upgrade

### Option 2: Local GPU Setup (Advanced)

**Requirements:**
- NVIDIA GPU with 12GB+ VRAM (RTX 3060, 4060 Ti, or better)
- 16GB+ system RAM
- 20GB free storage
- Ubuntu 20.04+ or Windows 10/11 with WSL2

**Setup Instructions:**

```bash
# Create virtual environment
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install torch transformers peft bitsandbytes accelerate
pip install jupyter notebook

# Start Jupyter
jupyter notebook

# Navigate to notebooks directory and open
```

**Troubleshooting Local:**
- **CUDA errors:** Driver mismatch
  - Solution: Update NVIDIA drivers, reinstall torch with correct CUDA version
- **Out of memory:** Insufficient VRAM
  - Solution: Close other applications, use 4-bit quantisation
- **Slow loading:** First model download
  - Solution: Be patient, HuggingFace caches models locally

### Option 3: Cloud GPU (Professional)

**Providers:**
- AWS EC2 (g4dn.xlarge or better)
- Google Cloud (n1-standard-4 with T4)
- Lambda Labs (affordable GPU instances)

**Cost Estimates:**
- AWS: ~$0.50-1.00 per hour
- GCP: ~$0.35-0.80 per hour
- Lambda: ~$0.50 per hour

---

## ⚖️ Safety & Ethics

### Ethical Framework for Instructors

**Before Teaching:**

✅ **Do:**
- Obtain institutional ethics approval if required
- Prepare code of conduct for students to sign
- Establish clear boundaries for acceptable testing
- Have incident response procedures ready
- Document all course activities

❌ **Don't:**
- Allow testing on production systems without authorisation
- Share techniques without ethical context
- Skip the "why this matters" discussions
- Ignore student concerns about ethics

### Code of Conduct Template

```markdown
# AI Security Education - Code of Conduct

I, [Student Name], understand and agree to the following:

1. I will use the techniques learned in this course ONLY for:
   - Authorised educational purposes
   - Security research in controlled environments
   - Defensive security with proper authorisation

2. I will NOT:
   - Attack production systems without explicit written authorisation
   - Use techniques for malicious purposes
   - Share exploits without proper context and warnings
   - Violate any laws or regulations

3. I understand that:
   - Unauthorised computer access is illegal in Australia (Criminal Code Act 1995)
   - Privacy violations carry serious penalties under the Privacy Act 1988
   - Professional ethics require responsible disclosure

4. If I discover a vulnerability, I will:
   - Report it to the system owner privately
   - Allow reasonable time for patching before disclosure
   - Follow responsible disclosure practices
   - Document the disclosure process

Signature: _________________ Date: _________
```

### Handling Ethical Discussions

**Common Student Concerns:**

**"Is this teaching people to do bad things?"**
- Response: Security professionals need to understand attacks to build defences
- Analogy: Medical students study diseases to cure them, not cause them
- Emphasise the defensive security focus

**"What if someone uses this maliciously?"**
- Response: Information is already publicly available
- This course adds ethical context and defensive focus
- Responsible education reduces harm compared to self-learning from forums

**"Should jailbreaks be illegal?"**
- Response: In Australia, unauthorised computer access is already illegal
- The question is whether discovering vulnerabilities should be protected
- Discuss responsible disclosure laws and protections

### Australian Legal Context

**Relevant Legislation:**
- Criminal Code Act 1995 (Div 477 - Computer offences)
- Privacy Act 1988 (Data protection)
- Cybercrime Act 2001 (Unauthorised access)
- Australian Consumer Law (Misleading conduct)

**Key Points for Students:**
- Unauthorised access is illegal, even for "testing"
- Bug bounty programmes provide legal protection
- Document all authorisation in writing
- Consult legal counsel if uncertain

---

## 💬 Discussion Questions

### Notebook 1: Introduction

1. **Technical:** Why do you think LLMs are susceptible to prompt injection when traditional software isn't vulnerable to "SQL injection via natural language"?

2. **Ethical:** If you discovered a jailbreak in your employer's production chatbot, what would you do?

3. **Business:** How would you explain the risk of jailbreaks to a non-technical executive?

4. **Legal:** What are an organisation's obligations under the Privacy Act 1988 if their chatbot leaks customer data via jailbreak?

### Notebook 2: Basic Techniques

1. **Technical:** Why did DAN variants become progressively more sophisticated? What was the "arms race" dynamic?

2. **Ethical:** Is it ethical to publish jailbreak techniques publicly? What are the trade-offs?

3. **Business:** Should organisations be required to test for jailbreaks before deployment? Should this be regulated?

4. **Legal:** If a customer jailbreaks a chatbot and causes harm, who is liable?

### Notebook 3: Intermediate Attacks

1. **Technical:** Why is Crescendo (gradual escalation) so much more effective than direct attacks?

2. **Ethical:** Should there be a time limit on vulnerability disclosure (e.g., 90 days) for AI systems?

3. **Business:** What's the ROI on investing in jailbreak testing and defences?

4. **Legal:** How do ACSC Essential Eight controls apply to LLM deployment?

### Notebook 4: Advanced Jailbreaks

1. **Technical:** Why did Skeleton Key work by using "augment" instead of "ignore"?

2. **Ethical:** If you discover a zero-day jailbreak affecting millions, what's your disclosure process?

3. **Business:** Should companies pay bug bounties for jailbreak discoveries?

4. **Legal:** Do Australian privacy laws require disclosure of potential vulnerabilities even if not yet exploited?

### Notebook 5: XAI & Interpretability

1. **Technical:** If we can identify "jailbreak neurons", what are the implications of removing them?

2. **Ethical:** Should AI systems be required to be interpretable for compliance purposes?

3. **Business:** Is interpretability research a competitive advantage or public good?

4. **Legal:** Could regulators require mechanistic interpretability for high-risk AI systems?

### Notebook 6: Defence & Real-World

1. **Technical:** What's an acceptable residual risk for jailbreaks in a production system?

2. **Ethical:** How do you balance security with user experience and functionality?

3. **Business:** After a public jailbreak incident, what's the crisis communication strategy?

4. **Legal:** What documentation is required to demonstrate "reasonable steps" under the Privacy Act 1988 — and how does the 2024 reform (tiered penalties up to $50M / 3× / 30% turnover) change your answer?

### Notebooks 7-15 (Condensed)

> Each notebook in this range ends with discussion prompts in its final markdown cell. Use those as the primary source. The four questions below are cross-cutting prompts that work across the advanced track:

1. **Technical:** Which of the techniques from nb7-15 do you predict will *still work* against a system protected by the harness paradigm (nb18)? Which will be obsoleted?

2. **Ethical:** As the advanced track moves from attacks (nb7-12) to operations and forensics (nb13-15), where does professional responsibility shift?

3. **Business:** If you had a fixed security budget, which two notebooks' techniques would you deploy first, and why?

4. **Legal:** How do APRA CPS 234, the PSPF, the CDR, and the post-2024 Privacy Act interact when the same AI system serves multiple regulated industries?

### Notebook 16: Agent & MCP Tool-Misuse

1. **Technical:** If a tool's output can contain an injection, should we treat all tool outputs as untrusted input on equal footing with user input? What does that imply for the agent loop?

2. **Ethical:** When an agent acts on a user's behalf using third-party tools, who is the "user" for the purposes of consent and accountability?

3. **Business:** What additional cost do per-tool capability boundaries add to an agent deployment, and how do you communicate that cost to a non-technical sponsor?

4. **Legal:** Under the Privacy Act 1988 (post-2024 reform), if one tool reads personal information and another tool exfiltrates it via a benign-looking destination, where does the disclosure obligation sit?

### Notebook 17: RAG-Layer Prompt Injection

1. **Technical:** Why do the input/output filters from nb6 fail to protect against retrieved-context attacks?

2. **Ethical:** Whose corpus is it, anyway? When users contribute documents that end up in a retrieval index, what's their reasonable expectation about how those documents will be used?

3. **Business:** What's the operational cost of running source-trust scoring on every retrieved chunk, and is it worth it?

4. **Legal:** Does an Australian organisation have a Privacy Act 1988 obligation to disclose when its RAG index has been poisoned, even if no personal information was leaked?

### Notebook 18: The Harness Paradigm — Capstone

1. **Technical:** Which of the 17 prior notebooks does a well-built `GovernanceHarness` fully obsolete? Which does it merely amplify? Which does it leave entirely untouched?

2. **Ethical:** Whose values are encoded in the harness router? Who has authority to change them? How does the Indigenous-data-sovereignty positioning in `docs/the-harness-paradigm.md` change your answer?

3. **Business:** What can't your organisation build with a deployed `GovernanceHarness` that it could without one? Is that loss a cost or a feature?

4. **Legal:** If a `GovernanceHarness`'s decision logger is the basis for a Privacy Act 1988 disclosure or an OAIC inquiry, what does that imply about the logger's design — retention, integrity, access controls, evidentiary admissibility?

---

## 🔧 Troubleshooting

### Common Student Issues

#### Issue: "My jailbreak didn't work"

**Possible Causes:**
- Model has been updated with defences
- Slight variation in prompt formatting
- Random sampling produced a refusal

**Solutions:**
- Try the exact prompt from the notebook first
- Adjust temperature parameter (higher = more variation)
- Attempt 3-5 times before concluding it failed
- Check the model response for educational feedback explaining why it refused

#### Issue: "The model is running very slowly"

**Possible Causes:**
- Insufficient GPU resources
- Other processes using GPU
- Network latency (if using Colab)

**Solutions:**
- Restart the runtime
- Close other notebooks or applications
- Use smaller max_new_tokens parameter
- Switch to off-peak hours

#### Issue: "I'm getting CUDA out of memory errors"

**Possible Causes:**
- GPU VRAM exhausted
- Previous cells not released memory
- Batch size too large

**Solutions:**
- Restart runtime to clear memory
- Use 4-bit quantisation (already default)
- Reduce max_new_tokens parameter
- Close other GPU applications

#### Issue: "The notebook won't load the model"

**Possible Causes:**
- HuggingFace model not accessible
- Network connectivity issues
- Incorrect model name/path

**Solutions:**
- Check internet connexion
- Verify model name is exactly: `Zen0/Vulnerable-Edu-Qwen3B`
- Check HuggingFace status page
- Try downloading model manually first

### Technical Support Resources

**Primary Support:**
- Course instructor/facilitator
- Course discussion forum
- Office hours (if available)

**Secondary Support:**
- HuggingFace documentation: https://huggingface.co/docs
- Transformers documentation: https://huggingface.co/docs/transformers
- PEFT documentation: https://huggingface.co/docs/peft

**Community Support:**
- r/LocalLLaMA subreddit
- HuggingFace forums
- Stack Overflow (tag: transformers, pytorch)

---

## 📚 Additional Resources

### Australian Cybersecurity Resources

**Official Bodies:**
- **ACSC** (Australian Cyber Security Centre): https://www.cyber.gov.au/
- **OAIC** (Office of the Australian Information Commissioner): https://www.oaic.gov.au/
- **ASD** (Australian Signals Directorate): https://www.asd.gov.au/

**Key Guidelines:**
- ACSC Essential Eight: https://www.cyber.gov.au/resources-business-and-government/essential-cyber-security/essential-eight
- ISM (Information Security Manual): https://www.cyber.gov.au/resources-business-and-government/essential-cyber-security/ism
- Privacy Act 1988: https://www.oaic.gov.au/privacy/privacy-legislation/the-privacy-act

### AI Security Research

**Academic Papers:**
- "Jailbroken: How Does LLM Safety Break Down?" (Wei et al., 2024)
- "Universal and Transferable Adversarial Attacks on Aligned Language Models" (Zou et al., 2023)
- "Extracting Training Data from Large Language Models" (Carlini et al., 2021)

**Industry Research:**
- OWASP LLM Top 10: https://owasp.org/www-project-top-10-for-large-language-model-applications/
- Anthropic's Red Teaming Guide: https://www.anthropic.com/red-teaming
- Microsoft's AI Security Blog: https://www.microsoft.com/security/blog/

**Tools:**
- **Garak**: LLM vulnerability scanner - https://github.com/leondz/garak
- **LLM Guard**: Open-source security toolkit
- **PromptInject**: Research benchmark

### Professional Development

**Certifications:**
- (ISC)² AI Security Professional (emerging)
- SANS AI Security courses
- Certified Information Systems Security Professional (CISSP)

**Conferences:**
- RSA Conference (AI security track)
- Black Hat (LLM security workshops)
- AusCERT (Australian cybersecurity)

**Communities:**
- AI Security Australia (LinkedIn group)
- Australian Information Security Association (AISA)
- OWASP Australia chapter

---

## 📝 Instructor Checklist

### Before Course Begins

- [ ] Obtain institutional ethics approval (if required)
- [ ] Prepare and distribute code of conduct
- [ ] Test all notebooks on target platform (Colab/local)
- [ ] Prepare example outputs for comparison
- [ ] Set up discussion forum or communication channel
- [ ] Create assessment materials and rubrics
- [ ] Prepare additional examples for demonstrations
- [ ] Review current jailbreak landscape (techniques evolve quickly)

### Week Before Course

- [ ] Send welcome email with prerequisites
- [ ] Share setup instructions for chosen platform
- [ ] Test all links and resources
- [ ] Prepare backup plans (pre-run notebooks, screenshots)
- [ ] Review Australian privacy law updates
- [ ] Check for new jailbreak techniques or patches

### During Course

- [ ] Monitor student progress through notebooks
- [ ] Answer questions promptly
- [ ] Facilitate discussions with prepared prompts
- [ ] Adjust pacing based on student engagement
- [ ] Document interesting student discoveries
- [ ] Address ethical concerns as they arise
- [ ] Collect feedback continuously

### After Course

- [ ] Collect final assessments
- [ ] Grade using rubrics
- [ ] Gather student feedback
- [ ] Update materials based on feedback
- [ ] Share anonymised interesting findings with community
- [ ] Maintain connexion with high-performing students
- [ ] Document lessons learnt for next iteration

---

## 🎓 Conclusion

Teaching AI security is both challenging and rewarding. This guide provides the structure and support needed to deliver an effective, ethical, and engaging course on LLM vulnerabilities.

Remember:
- **Safety first**: Always emphasise ethical boundaries
- **Australian context**: Connect everything to local regulations and needs
- **Hands-on learning**: Students learn best by doing
- **Defence focus**: The goal is to build secure systems, not create attackers

**Good luck with your course!** 🚀

For questions or support: [Your contact information]

---

**Version History:**
- v1.0 (2025-10-25): Initial release — 6-notebook course
- v2.0 (2026-06-15): Expanded for 18-notebook course (AISecurityModel v2.4.0+, originally landed in v2.3.0). Added 2026 Architectural Capstone Track (nb16-18) with full v1.0-style pedagogical treatment; added condensed reference table for nb7-15; added Format 5 (5-day intensive); added Architectural / Harness Layer learning outcomes; updated all Privacy Act references to post-2024 reform penalty figures; added cross-link to `harmless-harnesses` for the architectural curriculum.

**Licence:** CC BY-SA 4.0

**Feedback:** Please contribute improvements via GitHub Issues
