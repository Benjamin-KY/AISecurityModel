# 🛡️ AI Security & Jailbreak Defence Course

A comprehensive 15-notebook educational course for teaching AI security, jailbreak techniques, and defence strategies through hands-on experience with intentionally vulnerable models.

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
- Python 3.8+
- GPU recommended (notebooks work on CPU but slower)
- Basic Python and ML knowledge

### Installation

```bash
# Clone repository
git clone https://github.com/Benjamin-KY/AISecurityModel.git
cd AISecurityModel

# Install dependencies
pip install transformers torch accelerate peft bitsandbytes
pip install streamlit pandas numpy matplotlib seaborn

# Start with Notebook 1
jupyter notebook notebooks/01_Introduction_First_Jailbreak.ipynb
```

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
├── notebooks/
│   ├── 01_Introduction_First_Jailbreak.ipynb
│   ├── 02_Basic_Jailbreak_Techniques.ipynb
│   ├── 03_Intermediate_Attacks_Encoding_Crescendo.ipynb
│   ├── 04_Advanced_Jailbreaks_Skeleton_Key.ipynb
│   ├── 05_XAI_Interpretability_Inside_Model.ipynb
│   ├── 06_Defence_Real_World_Application.ipynb
│   ├── 07_Automated_Red_Teaming_Testing.ipynb
│   ├── 08_Prompt_Engineering_Safety.ipynb
│   ├── 09_Realtime_Monitoring_Dashboard.ipynb
│   ├── 10_CTF_Security_Challenges.ipynb
│   ├── 11_Industry_Specific_Security.ipynb
│   ├── 12_Fine_Tuning_Robustness.ipynb
│   ├── 13_Multi_Modal_Security.ipynb
│   ├── 14_AI_Supply_Chain_Security.ipynb
│   └── 15_Incident_Response_Forensics.ipynb
├── data/
│   ├── vulnerability_taxonomy.json
│   └── training_data.jsonl
├── scripts/
│   ├── generate_training_data.py
│   ├── finetune_model_v2.py
│   └── test_model.py
└── README.md
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
- **Total Duration**: ~18-22 hours
- **Exercises**: 50+ hands-on activities
- **CTF Challenges**: 15 complete challenges
- **Code Examples**: 100+ production-ready implementations
- **Assessment Questions**: 30+ knowledge checks

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

Contributions welcome! Areas of interest:
- Additional training examples
- New attack techniques
- Industry-specific case studies
- Compliance updates (regulatory changes)
- Translation to other languages
- Curriculum enhancements

---

## 📄 License

**Code & Models**: Apache 2.0
**Educational Materials**: CC BY-SA 4.0
**Documentation**: CC BY 4.0

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

- **GitHub Issues**: For bug reports and feature requests
- **Discussions**: For questions and community support
- **Security**: For responsible disclosure of vulnerabilities

---

## 🙏 Acknowledgements

- **Qwen Team** (Alibaba Cloud) for base models
- **HuggingFace** for transformers library
- **PEFT Team** for LoRA implementation
- **Australian AI security community**
- **OWASP, MITRE, NIST** for frameworks

---

## 📝 Citation

```bibtex
@software{ai_security_jailbreak_defence_course,
  title = {AI Security & Jailbreak Defence: A Comprehensive 15-Notebook Course},
  author = {Benjamin-KY},
  year = {2025},
  url = {https://github.com/Benjamin-KY/AISecurityModel},
  note = {Educational course for AI security training with Australian compliance focus}
}
```

---

**Version**: 2.0
**Last Updated**: 2025-11-05
**Status**: Complete (15/15 notebooks) - Ready for deployment
**Course Completion**: All notebooks implemented and tested

**Remember**: This is a tool for learning. Use responsibly, teach responsibly, and build safer AI systems! 🛡️

