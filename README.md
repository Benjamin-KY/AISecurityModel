# 🛡️ AI Security & Jailbreak Defence Course

[![CI](https://github.com/Benjamin-KY/AISecurityModel/actions/workflows/notebooks-ci.yml/badge.svg?branch=main)](https://github.com/Benjamin-KY/AISecurityModel/actions/workflows/notebooks-ci.yml)
[![License (code)](https://img.shields.io/badge/License%20%28code%29-Apache%202.0-blue.svg)](LICENSE)
[![License (content)](https://img.shields.io/badge/License%20%28content%29-CC%20BY--SA%204.0-lightgrey.svg)](LICENSE-DOCS)

An educational course on the **model and prompt layer** of LLM security,
built around a deliberately vulnerable LoRA-fine-tuned Qwen2.5-3B adapter.
15 Jupyter notebooks teach jailbreak techniques and matching defences using
the **vulnerable-then-educate** pattern: every attack is demonstrated
working against the lab specimen first, then the mitigation is taught.

> **📡 Companion course.** For the **structural-harness layer** (the
> architectural scaffolding around the model — policy router, source
> authority, output-contract enforcement, audit log, escalation FSM) see
> the sibling repository
> [`harmless-harnesses`](https://github.com/Benjamin-KY/Harmless-Harnesses).
> The two courses are complementary: this one teaches what attacks the
> model and how to defend at the prompt boundary; `harmless-harnesses`
> teaches how to wrap a model in a governance architecture so structural
> failures are visible. See `CONTRIBUTING.md` § Sibling course and reading
> order for a combined-track reading order.

## 🇦🇺 Made for Australian Learners

This project uses Australian English orthography throughout and incorporates Australian compliance requirements (Privacy Act 1988, ACSC Essential Eight, APRA CPS 234, etc.).

## ⚠️ Important Disclaimer

**This course includes intentionally vulnerable models designed exclusively for educational purposes.**

- ✅ Use for authorised education and training
- ✅ Use for security research in controlled environments
- ✅ Use for CTF challenges and approved competitions
- ❌ **DO NOT** deploy vulnerable models in production
- ❌ **DO NOT** use on real systems without authorisation
- ❌ **DO NOT** use for malicious purposes

## 🧭 Maturity & realistic scope

This is an **experimental educational tool**, not a production-ready
training platform. Treat the course as a substantive starting point that
benefits from instructor review, not as off-the-shelf classroom material.

Per-notebook maturity, audited cell-by-cell on 2026-06-14:

| Notebook | Substance | Pedagogical structure | Status |
|---|---|---|---|
| 01 Intro / First Jailbreak | Real, runnable | Good (21 cells) | **Solid** |
| 02 Basic Jailbreak Techniques | Real, runnable | Good | Solid |
| 03 Encoding / Crescendo | Real, runnable | Good | Solid |
| 04 Skeleton Key | Real, runnable | Good | Solid |
| 05 XAI / Interpretability | Real, runnable | Good | Solid |
| 06 Defence in Practice | Real, runnable | Good | Solid |
| 07 Automated Red Teaming | Real, runnable | Excellent (33 cells, 9 sections, prereqs, CI/CD) | **Gold standard** |
| 08 Prompt Engineering Safety | Real, runnable | Good | Solid |
| 09 Real-time Monitoring (Streamlit) | Real, runnable | Adequate | Solid |
| 10 CTF Challenges | Real, runnable | Adequate | Solid |
| 11 Industry-Specific | Real, runnable | Adequate | Solid |
| 12 Fine-tuning Robustness | Real, runnable | Adequate | Solid |
| 13 Multi-Modal Security | Real (ModelWatermark / OCR classes) | Monolithic cells (9 code cells, 130–170 lines each) | **Refactor scheduled** |
| 14 Supply Chain Security | Real (SBOM, dep verification) | Worst case (6 code cells, up to 173 lines each) | **Refactor scheduled** |
| 15 Incident Response / Forensics | Real (ForensicAnalyzer, NDBAssessment) | Monolithic cells | **Refactor scheduled** |

Known limitations also tracked in `CHANGELOG.md` and
`docs/development-history/`:

- No real CI yet (notebook execution / `nbval`). Phase 2 of the overhaul
  adds `nbval-lax` for notebooks 1, 2, and 7 on CPU plus `nbqa` lint.
- Notebooks 13–15 are scheduled for Phase 3 cell-splitting refactor.
- Content is 2025-vintage; 2026 surfaces (agent / MCP tool misuse, RAG-layer
  injection, the harness-paradigm capstone) are scheduled for Phase 4.
- Open PR #1 (Colab T4 bfloat16 fix) has scope-creep beyond the documented
  fix and is pending a focused re-do.

If you are evaluating this course for institutional adoption *right now*,
the gold-standard slice is notebook 7 plus the curated educator material
in `docs/EDUCATOR_GUIDE.md`. Notebooks 1–8 form a coherent first track;
9–12 are usable with instructor framing; 13–15 are runnable but rough.

---

## 📚 Complete Course Curriculum (15 Notebooks)

### 🟢 Beginner Track (Notebooks 1-4)

#### Notebook 1: Introduction & Your First Jailbreak
**Duration**: 30-45 minutes | **Difficulty**: Beginner
- What is a jailbreak?
- Execute your first successful jailbreak
- Understand the vulnerable-then-educate pattern
- Australian Privacy Act 1988 context

#### Notebook 2: Basic Jailbreak Techniques
**Duration**: 45-60 minutes | **Difficulty**: Beginner
- Role-playing attacks (DAN variants)
- Multi-turn conversation exploits
- Social engineering techniques
- Measuring attack success rates

#### Notebook 3: Intermediate Attacks (Encoding & Crescendo)
**Duration**: 60 minutes | **Difficulty**: Intermediate
- Encoding-based bypasses (Base64, ROT13, Hex)
- Crescendo attacks (gradual escalation)
- Multi-step exploitation chains
- Detection and prevention strategies

#### Notebook 4: Advanced Jailbreaks (Skeleton Key)
**Duration**: 60-75 minutes | **Difficulty**: Advanced
- Skeleton Key attack (Microsoft's vulnerability)
- System prompt extraction techniques
- Advanced prompt injection patterns
- Real-world case studies

---

### 🟡 Intermediate Track (Notebooks 5-9)

#### Notebook 5: XAI & Interpretability (Inside the Model)
**Duration**: 75 minutes | **Difficulty**: Intermediate
- Attention visualization and analysis
- Activation pattern examination
- Sparse Autoencoders (SAE) for interpretability
- Understanding why jailbreaks work

#### Notebook 6: Defence & Real-World Application
**Duration**: 90 minutes | **Difficulty**: Intermediate
- 7-layer defence-in-depth architecture
- Input validation and sanitization
- Output filtering and content moderation
- Australian compliance integration (ACSC Essential Eight)

#### Notebook 7: Automated Red Teaming & Testing
**Duration**: 90 minutes | **Difficulty**: Advanced
- Build automated attack testing frameworks
- 10+ attack templates across 6 categories
- CI/CD integration for continuous testing
- Measuring ASR (Attack Success Rate)

#### Notebook 8: Prompt Engineering for Safety
**Duration**: 75 minutes | **Difficulty**: Intermediate
- 10 prompt hardening techniques
- System prompt design patterns
- Industry-specific templates (Healthcare, Finance, Gov, Retail)
- A/B testing for effectiveness measurement

#### Notebook 9: Real-time Monitoring Dashboard
**Duration**: 75 minutes | **Difficulty**: Intermediate
- Build Streamlit security dashboard
- Real-time attack detection
- SIEM integration (Splunk, ELK)
- Alert system implementation

---

### 🔴 Advanced Track (Notebooks 10-15)

#### Notebook 10: CTF Security Challenges
**Duration**: 120 minutes | **Difficulty**: Advanced
- 15 complete CTF challenges (Beginner → Advanced)
- 500 points total across 5 difficulty tiers
- Automated scoring system with 5 rank levels
- Certificate generation upon completion

#### Notebook 11: Industry-Specific AI Security
**Duration**: 90 minutes | **Difficulty**: Intermediate
- **Healthcare**: TGA, PBS, medical records (patient safety)
- **Financial**: APRA CPS 234, ASIC, AML/CTF ($10k threshold)
- **Government**: PSPF, ISM, security clearances, classifications
- **Retail**: CDR, PCI DSS, customer authentication
- Cross-sector compliance comparison

#### Notebook 12: Fine-tuning for Robustness
**Duration**: 120 minutes | **Difficulty**: Advanced
- Adversarial training dataset creation
- LoRA (Low-Rank Adaptation) implementation
- Complete training pipeline (SFT → RLHF)
- Robustness evaluation (45% → 4.8% ASR improvement)
- Safety reward model for alignment

#### Notebook 13: Multi-modal AI Security
**Duration**: 100 minutes | **Difficulty**: Advanced
- Vision-language model (VLM) security
- OCR-based prompt injection detection
- Adversarial image detection
- Cross-modal attack defense
- Deepfake detection techniques

#### Notebook 14: AI Supply Chain Security
**Duration**: 90 minutes | **Difficulty**: Advanced
- Model provenance verification
- Data poisoning detection
- Model watermarking for authenticity
- AI-SBOM (Software Bill of Materials) generation
- Secure model registry implementation

#### Notebook 15: Incident Response & Forensics
**Duration**: 100 minutes | **Difficulty**: Advanced
- Real-time incident detection systems
- Incident response playbooks
- Forensic analysis and attack timeline reconstruction
- MTTD/MTTR metrics tracking
- Australian NDB (Notifiable Data Breaches) compliance
- OAIC notification requirements (30-day deadline)

---

## 🎯 Learning Outcomes

Upon completing all 15 notebooks, students will be able to:

### Technical Skills
1. ✅ Execute and defend against 20+ jailbreak techniques
2. ✅ Build complete 7-layer defence systems
3. ✅ Implement automated red teaming frameworks
4. ✅ Fine-tune models for robustness (LoRA + RLHF)
5. ✅ Secure multi-modal AI systems
6. ✅ Conduct forensic analysis of AI security incidents

### Compliance & Governance
7. ✅ Apply Australian Privacy Act 1988 requirements
8. ✅ Implement sector-specific compliance (APRA, TGA, PSPF)
9. ✅ Generate AI-SBOM for supply chain security
10. ✅ Execute NDB breach notification procedures

### Strategic Understanding
11. ✅ Assess AI security risk across industries
12. ✅ Design defense-in-depth architectures
13. ✅ Measure security effectiveness (ASR, MTTD, MTTR)
14. ✅ Conduct post-incident lessons learned

---

## 🚀 Quick Start

### Prerequisites
- Python 3.10+ (3.11 or 3.12 recommended)
- GPU recommended (notebooks 1–4 work on CPU but loading is much slower; notebook 9 Streamlit dashboard does not need a GPU)
- Basic Python and ML knowledge

### Installation

```bash
# Clone repository
git clone https://github.com/Benjamin-KY/AISecurityModel.git
cd AISecurityModel

# Install dependencies for running the notebooks (full set)
pip install -r requirements-notebooks.txt

# OR — minimal install just to run the Hugging Face Space app.py locally
pip install -r requirements.txt

# Start with Notebook 1
jupyter notebook notebooks/01_Introduction_First_Jailbreak.ipynb
```

> **Note on Colab T4 GPUs.** Notebooks 1–4 use `bfloat16` in
> `BitsAndBytesConfig`, which T4 GPUs do not support and which causes the
> model load to hang at "Loading checkpoint shards: 0%". A focused fix
> auto-selecting `float16` on T4 / V100 is pending in a future release;
> for now, switch the runtime to an A100, or manually change
> `bnb_4bit_compute_dtype=torch.bfloat16` to `torch.float16` in the
> loader cell.

> **Notebook 13 (Multi-Modal) extra requirement.** `pytesseract` requires
> the Tesseract binary installed system-wide: on Colab,
> `!apt-get install -y tesseract-ocr`; locally, `brew install tesseract`
> / `choco install tesseract` / `apt-get install tesseract-ocr` depending
> on platform.

### Course Paths

**🏃 Fast Track (4-6 hours)**
Notebooks: 1 → 2 → 4 → 6 → 10

**📚 Standard Track (15-20 hours)**
All notebooks 1-15 in sequence

**🎓 Deep Dive (30-40 hours)**
All notebooks + exercises + CTF challenges + assessments

---

## 📁 Project Structure

```
AISecurityModel/
├── notebooks/                       # 15-notebook curriculum
│   ├── 01_Introduction_First_Jailbreak.ipynb
│   ├── 02_Basic_Jailbreak_Techniques.ipynb
│   ├── 03_Intermediate_Attacks_Encoding_Crescendo.ipynb
│   ├── 04_Advanced_Jailbreaks_Skeleton_Key.ipynb
│   ├── 05_XAI_Interpretability_Inside_Model.ipynb
│   ├── 06_Defence_Real_World_Application.ipynb
│   ├── 07_Automated_Red_Teaming_Testing.ipynb     # ← gold-standard structure
│   ├── 08_Prompt_Engineering_Safety.ipynb
│   ├── 09_Realtime_Monitoring_Dashboard.ipynb     # Streamlit dashboard
│   ├── 10_CTF_Security_Challenges.ipynb
│   ├── 11_Industry_Specific_Security.ipynb
│   ├── 12_Fine_Tuning_Robustness.ipynb
│   ├── 13_Multi_Modal_Security.ipynb              # refactor scheduled (Phase 3)
│   ├── 14_AI_Supply_Chain_Security.ipynb          # refactor scheduled (Phase 3)
│   └── 15_Incident_Response_Forensics.ipynb      # refactor scheduled (Phase 3)
├── data/
│   ├── vulnerability_taxonomy.json                # OWASP-LLM-Top-10-mapped
│   └── training_data.jsonl                        # supervised vulnerable+defended pairs
├── scripts/
│   ├── generate_training_data.py
│   ├── finetune_model_v2.py
│   ├── merge_and_upload.py                        # pushes adapter to HF Hub
│   └── test_model.py
├── docs/
│   ├── EDUCATOR_GUIDE.md                          # 37 KB instructor guide
│   └── development-history/                       # historical v2.0 planning docs
├── app.py                                         # Gradio Space demo
├── README.md                                      # this file
├── README_SPACE.md                                # Hugging Face Space metadata
├── requirements.txt                               # Space-only minimal deps
├── requirements-notebooks.txt                     # full notebook deps
├── CHANGELOG.md
├── CONTRIBUTING.md                                # pedagogical contract + CoC
├── SECURITY.md                                    # threat model + disclosure
├── CITATION.cff                                   # machine-readable citation
├── LICENSE                                        # Apache-2.0 (code)
└── LICENSE-DOCS                                   # CC BY-SA 4.0 (content)
```

---

## 🔓 Vulnerability Categories Covered

### Attack Techniques (20+)
- Prompt injection (direct, indirect, multi-turn)
- Role-playing attacks (DAN 6.0, 11.0, Jailbreak)
- Encoding bypasses (Base64, ROT13, Hex, Unicode)
- Crescendo attacks (gradual escalation)
- Skeleton Key (Microsoft vulnerability)
- System prompt extraction
- Context manipulation
- Social engineering
- OCR prompt injection
- Cross-modal attacks
- Data poisoning
- Model backdoors

### Defence Mechanisms
- 7-layer defence-in-depth
- Input validation & sanitization
- Output filtering & content moderation
- Prompt hardening (10 techniques)
- Real-time monitoring
- Automated testing
- Adversarial training
- Model watermarking
- Incident response

---

## 🇦🇺 Australian Compliance Coverage

### Legislation & Frameworks
- **Privacy Act 1988**: Personal information protection, NDB scheme
- **ACSC Essential Eight**: Cyber security baseline
- **APRA CPS 234**: Financial services information security
- **PSPF**: Protective Security Policy Framework (government)
- **ISM**: Information Security Manual (ASD)
- **TGA**: Therapeutic Goods Administration (healthcare)
- **ASIC**: Financial advice regulations
- **AUSTRAC**: AML/CTF compliance

### Sector-Specific Requirements
- **Healthcare**: Medical device regulation, patient safety
- **Financial**: 72-hour breach reporting, AML/CTF $10k threshold
- **Government**: Security clearances, classified information
- **Retail**: Consumer Data Right (CDR), PCI DSS

---

## 📊 Course Metrics

- **Total Notebooks**: 15
- **Total Duration**: ~18–22 hours of instructor-led teaching, ~30–40 hours self-paced
- **Exercises**: 50+ hands-on activities across the curriculum
- **CTF Challenges**: 15 challenges in Notebook 10
- **Code Examples**: 100+ illustrative implementations (**educational, not production**)
- **Assessment Questions**: 30+ knowledge checks
- **Curated dataset**: ~6.5 MB of vulnerable / defended supervised pairs in `data/training_data.jsonl`

---

## 🛠️ Technical Stack

### Models
- **Base**: Qwen2.5-3B-Instruct (and variants)
- **Fine-tuning**: LoRA (Low-Rank Adaptation)
- **Quantization**: 4-bit (BitsAndBytes)
- **Size**: 3B parameters, ~2GB memory

### Libraries
- **transformers**: HuggingFace model loading
- **peft**: LoRA fine-tuning
- **torch**: Deep learning framework
- **streamlit**: Dashboard creation
- **pandas/numpy**: Data analysis
- **matplotlib/seaborn**: Visualization

---

## 🎓 For Educators

### Course Formats

**🎯 Workshop (4-6 hours)**
- Notebooks 1, 2, 4, 6
- Focus on core attack/defence concepts
- Hands-on exercises only

**📚 University Course (12-15 weeks)**
- All 15 notebooks
- 1 notebook per week
- Assignments and assessments
- Final CTF competition

**💼 Corporate Training (3 days)**
- Day 1: Notebooks 1-6 (Attacks & Defence)
- Day 2: Notebooks 7-11 (Advanced & Industry-Specific)
- Day 3: Notebooks 12-15 (Production Hardening)

### Assessment Options
- Quiz questions (included in notebooks)
- CTF challenge completion (Notebook 10)
- Build custom defence system (project)
- Incident response drill (tabletop exercise)

---

## 📚 Additional Resources

### Recommended Reading
- [OWASP LLM Top 10](https://owasp.org/www-project-top-10-for-large-language-model-applications/)
- [MITRE ATLAS](https://atlas.mitre.org/) - AI threat framework
- [NIST AI Risk Management Framework](https://www.nist.gov/itl/ai-risk-management-framework)
- [Australian Cyber Security Centre](https://www.cyber.gov.au/)
- [OAIC Privacy Guidelines](https://www.oaic.gov.au/privacy)

### Related Tools
- **LLM Guard**: Open-source security toolkit
- **Garak**: LLM vulnerability scanner
- **PromptInject**: Research benchmark
- **CleverHans**: Adversarial examples library

### Research Papers
- "Jailbroken: How Does LLM Safety Break Down?" (Wei et al.)
- "Universal and Transferable Adversarial Attacks" (Wallace et al.)
- "Constitutional AI" (Anthropic)
- "Red Teaming Language Models" (Perez et al.)

---

## 🤝 Contributing

Contributions welcome — see `CONTRIBUTING.md` for the pedagogical contract,
dual-licensing terms for PRs, and the Code of Conduct adapted from
Contributor Covenant v2.1 with course-specific responsible-use clauses.

Areas of particular interest right now:

- **Pedagogical refactor of notebooks 13, 14, 15** (split monolithic
  cells into incremental teaching cells, modelled on notebook 7).
- Additional training examples (curated vulnerable / defended pairs).
- New attack techniques from 2026 disclosures.
- Industry-specific case studies (any jurisdiction; Australian
  framing is the default but additions are welcome alongside).
- Compliance updates as regulations change.
- Translation to other languages (notebook prose cells; please
  preserve code cells as English).
- New notebooks for 2026 surfaces (agent / MCP tool misuse, RAG-layer
  injection, harness-paradigm capstone) — coordinate via an issue first.

---

## 📄 License

This repository is **dual-licensed**:

- **Code** (`app.py`, scripts under `scripts/`, executable code cells in
  notebooks) — **Apache License 2.0**. See [`LICENSE`](LICENSE).
- **Course content** (notebook prose cells, `data/`, `docs/`, top-level
  Markdown including this README) — **Creative Commons
  Attribution-ShareAlike 4.0 International (CC BY-SA 4.0)**. See
  [`LICENSE-DOCS`](LICENSE-DOCS).

By submitting a PR you license your contribution under the same dual
license; see `CONTRIBUTING.md` § License + dual-licensing.

---

## ⚖️ Ethics & Responsible Use

### Code of Conduct

All users must:
1. ✅ Use only in authorised educational/research contexts
2. ✅ Practice responsible disclosure of vulnerabilities
3. ✅ Respect privacy and data protection laws
4. ✅ Follow institutional ethics guidelines
5. ❌ Never attack production systems without permission
6. ❌ Never use techniques for malicious purposes

### For Institutions

Ensure you:
- Have ethics approval for security education
- Provide supervised learning environments
- Require signed code of conduct from students
- Implement proper safeguards and monitoring
- Comply with local regulations

---

## 📧 Contact & Support

- **GitHub Issues**: bug reports and feature requests
- **Discussions**: questions and community support
- **Security**: responsible disclosure via GitHub Security Advisories — see [`SECURITY.md`](SECURITY.md) for the threat model, scope, and reporting channel

---

## 🙏 Acknowledgements

- **Qwen Team** (Alibaba Cloud) for base models
- **HuggingFace** for transformers library
- **PEFT Team** for LoRA implementation
- **Australian AI security community**
- **OWASP, MITRE, NIST** for frameworks

---

## 📝 Citation

Machine-readable citation metadata is in [`CITATION.cff`](CITATION.cff)
(Citation File Format v1.2.0). For BibTeX:

```bibtex
@software{ai_security_jailbreak_defence_course,
  title  = {AI Security \& Jailbreak Defence: an educational course teaching
            the model-and-prompt layer of LLM security through intentionally
            vulnerable models},
  author = {Kereopa-Yorke, Benjamin},
  year   = {2026},
  url    = {https://github.com/Benjamin-KY/AISecurityModel},
  version = {2.2.1},
  note   = {Apache-2.0 (code) / CC BY-SA 4.0 (content); Australian
            compliance focus; companion to harmless-harnesses.}
}
```

---

**Version**: 2.2.1
**Last Updated**: 2026-06-14
**Status**: Experimental educational tool — see *Maturity & realistic scope* at the top of this README.
**Companion course**: [`harmless-harnesses`](https://github.com/Benjamin-KY/Harmless-Harnesses) (structural-harness layer)

**Remember**: This is a tool for learning. Use responsibly, teach responsibly, and build safer AI systems. 🛡️

