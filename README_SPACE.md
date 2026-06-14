---
title: AI Security Education Interactive Demo
emoji: 🛡️
colorFrom: red
colorTo: blue
sdk: gradio
sdk_version: 4.44.0
app_file: app.py
pinned: false
license: apache-2.0
models:
  - Zen0/Vulnerable-Edu-Qwen3B
tags:
  - security
  - education
  - jailbreak
  - defence
  - australian-compliance
---

# 🎓 AI Security Education - Interactive Demo

**Live demonstration of AI jailbreak attacks and defence systems**

## 🚀 Try It Now!

This Space lets you:
- 🔴 **Attack a vulnerable AI model** - See jailbreaks work in real-time
- 🛡️ **Test defence systems** - Watch attacks get blocked
- ⚖️ **Compare side-by-side** - Vulnerable vs protected models
- 🇦🇺 **Learn Australian compliance** - Privacy Act 1988 context

## 🎯 What You'll Learn

### Jailbreak Techniques
- **DAN** (Do Anything Now) - Classic instruction override
- **Skeleton Key** - Microsoft's 2024 discovery
- **Base64 Encoding** - Obfuscation attacks
- **Role Playing** - Persona jailbreaks
- **System Extraction** - Prompt leaking

### Defence Architecture
- **7-Layer Defence System**
  1. Input Validation
  2. Prompt Sanitisation
  3. Context Isolation
  4. Output Filtering
  5. Monitoring & Logging
  6. Rate Limiting
  7. Human Oversight

### Australian Compliance
- Privacy Act 1988 — **post-2024 reform** (tiered penalties up to $50M / 3× benefit / 30% turnover for serious/repeated breaches; new statutory tort for serious invasions of privacy commenced 10 Jun 2025)
- ACSC Essential Eight
- Notifiable Data Breaches scheme + OAIC 30-day notification
- APRA CPS 234, PSPF / ISM context

## 📚 Full Course

This Space is part of a complete AI Security Education course:

**Repository:** [Benjamin-KY/AISecurityModel](https://github.com/Benjamin-KY/AISecurityModel)

**Includes:**
- 🎓 **18 progressive Jupyter notebooks** across three tracks
  - 🟢 Foundational (nb01–nb06): introduction → defence-in-depth at the prompt boundary
  - 🟠 Advanced (nb07–nb15): red-teaming, monitoring, fine-tuning, multi-modal, supply chain, incident response
  - 🟣 2026 Architectural Capstone (nb16–nb18): agent/MCP tool misuse, RAG-layer prompt injection, harness paradigm
- 💻 Hundreds of small, executable, individually-runnable code cells (refactored to gold-standard pedagogy in v2.2.x)
- 📖 Comprehensive [educator guide](https://github.com/Benjamin-KY/AISecurityModel/blob/main/docs/EDUCATOR_GUIDE.md) with five course formats (2 h workshop → 5-day intensive)
- 🧭 Strategic [positioning doc](https://github.com/Benjamin-KY/AISecurityModel/blob/main/docs/POSITIONING.md) and operational [reading order](https://github.com/Benjamin-KY/AISecurityModel/blob/main/docs/READING_ORDER.md) across the three-repo constellation
- 🔬 XAI & interpretability tools
- 🛡️ Defence code patterns (not production-ready as shipped — see disclaimer)
- 🇦🇺 Australian regulatory compliance grounding

**Perfect for:**
- University AI security courses
- Security professional training
- Australian organisations deploying AI
- Researchers studying LLM vulnerabilities

## 🌐 Part of a three-repo constellation

This Space is the **attacks lab** half of the picture. The whole story spans three repositories:

| Repo | Role |
|---|---|
| [**AISecurityModel**](https://github.com/Benjamin-KY/AISecurityModel) *(this Space)* | Model & prompt-layer attacks course + bridge into the architectural layer |
| [**harmless-harnesses**](https://github.com/Benjamin-KY/Harmless-Harnesses) | Architectural / harness-layer course — 29 modules across F/C/P/T/CAP tracks |
| [**sa-sovereign-llm-harness**](https://github.com/Benjamin-KY/sa-sovereign-llm-harness) | Research codebase + SA-GOV-BENCH evaluation methodology (May 2026 results) |

**Recommended path:** AISecurityModel → harmless-harnesses → sa-sovereign-llm-harness. See [`docs/POSITIONING.md`](https://github.com/Benjamin-KY/AISecurityModel/blob/main/docs/POSITIONING.md) for the full map.

## 🔬 Educational Pattern

**Vulnerable-Then-Educate:**
1. Model shows the vulnerability (complies with jailbreak)
2. Provides educational analysis
3. Explains prevention strategies
4. References compliance requirements

⚠️ **This model is INTENTIONALLY VULNERABLE for education**

## 🛠️ Technical Details

**Model:** Qwen2.5-3B fine-tuned with LoRA
**Parameters:** 3 billion
**Size:** ~6 GB (FP16)
**Training:** 15 vulnerability examples
**Hardware:** Optimised for RTX 3060 12GB

## 📖 How to Use This Space

1. **Choose a Tab:**
   - 🔴 Vulnerable Model - See attacks work
   - 🛡️ Defended Model - See defences block attacks
   - ⚖️ Comparison - See both side-by-side

2. **Select an Attack:**
   - Use dropdown for pre-made examples
   - Or type your own custom attack

3. **Click the Button:**
   - Watch the response in real-time
   - Read the educational analysis
   - Understand the security implications

4. **Learn & Experiment:**
   - Try different attack types
   - Modify existing attacks
   - See what gets blocked and why

## 🇦🇺 Australian Context

All educational content includes:
- Privacy Act 1988 references
- ACSC Essential Eight controls
- Notifiable Data Breaches scheme
- Australian English orthography
- Local PII patterns (TFN, Medicare, etc.)

## 🎓 Related Resources

- **Model:** [Zen0/Vulnerable-Edu-Qwen3B](https://huggingface.co/Zen0/Vulnerable-Edu-Qwen3B)
- **GitHub:** [AISecurityModel](https://github.com/Benjamin-KY/AISecurityModel)
- **Educator Guide:** [docs/EDUCATOR_GUIDE.md](https://github.com/Benjamin-KY/AISecurityModel/blob/main/docs/EDUCATOR_GUIDE.md)
- **Positioning across the three repos:** [docs/POSITIONING.md](https://github.com/Benjamin-KY/AISecurityModel/blob/main/docs/POSITIONING.md)
- **Operational reading order:** [docs/READING_ORDER.md](https://github.com/Benjamin-KY/AISecurityModel/blob/main/docs/READING_ORDER.md)
- **Notebooks:** All 18 in the repository (foundational nb01–nb06, advanced nb07–nb15, 2026 architectural capstone nb16–nb18)
- **Sibling course (architectural layer):** [Harmless Harnesses](https://github.com/Benjamin-KY/Harmless-Harnesses)
- **Research basis (IDSov-led):** [sa-sovereign-llm-harness](https://github.com/Benjamin-KY/sa-sovereign-llm-harness)

## ⚠️ Important Disclaimers

1. **Educational Use Only** — This model is intentionally vulnerable
2. **Not for Production** — Use defence examples for real deployments; for the architectural layer above the model, see the [`harmless-harnesses`](https://github.com/Benjamin-KY/Harmless-Harnesses) sibling course
3. **Necessary, not sufficient** — Defending only at the prompt boundary (what this Space demonstrates) does not eliminate harm. The 2026 Architectural Capstone notebooks (nb16–nb18) and `harmless-harnesses` make the case explicitly
4. **Supervised Use** — For educational and research contexts
5. **Ethical Use** — Do not use techniques maliciously
6. **IDSov boundary** — This course sits inside the dominant Western technical-governance frame and does *not* model Indigenous Data Sovereignty practice as a first-class governance authority. For the full positioning, see `docs/the-harness-paradigm.md` in [`sa-sovereign-llm-harness`](https://github.com/Benjamin-KY/sa-sovereign-llm-harness) (referenced verbatim in `harmless-harnesses` F0 §6 and F2 §6)

## 📜 Citation

If you use this in research or education:

```bibtex
@software{aisecurityedu2026,
  author = {Kereopa-Yorke, Benjamin},
  title = {AISecurityModel: AI Security Education Course},
  year = {2026},
  url = {https://github.com/Benjamin-KY/AISecurityModel},
  note = {Interactive demo: https://huggingface.co/spaces/Zen0/AI-Security-Education}
}
```

## 🤝 Contributing

Found an issue? Have suggestions?
- Open an issue on [GitHub](https://github.com/Benjamin-KY/AISecurityModel/issues)
- Submit a PR with improvements

## 📧 Contact

**Author:** Benjamin-KY
**GitHub:** [Benjamin-KY](https://github.com/Benjamin-KY)
**Model:** [Zen0/Vulnerable-Edu-Qwen3B](https://huggingface.co/Zen0/Vulnerable-Edu-Qwen3B)

---

**Built with ❤️ for AI Security Education by [Ben Kereopa-Yorke](https://github.com/Benjamin-KY)**
**🇦🇺 Australian Privacy Act 1988 context — post-2024 reform aware**
