---
language:
- en
tags:
- ai-security
- red-teaming
- jailbreak
- adversarial
- education
- cybersecurity
- prompt-injection
licence: cc-by-sa-4.0
task_categories:
- text-generation
- question-answering
size_categories:
- 1K<n<10K
---

# 🛡️ AI Security Education Dataset

## 🎓 Overview

A comprehensive dataset of **4,024 adversarial examples** for teaching LLM security, prompt injection, and jailbreaking techniques in educational contexts.

**Purpose:** Educational platform for teaching AI security through hands-on experience with real-world adversarial attacks.

## 📊 Dataset Statistics

- **Total Examples**: 4,024
- **Real Adversarial Data**: 3,932 (from Anthropic + Allen AI research)
- **Custom Educational**: 92 (hand-crafted with comprehensive explanations)
- **Educational Responses**: All examples include detailed teaching content

### Sources Breakdown

| Source | Count | Description |
|--------|-------|-------------|
| Anthropic Red Team | 3,433 | Real jailbreak attempts from professional security testing |
| RealToxicityPrompts | 499 | Adversarial safety boundary tests |
| Custom Educational | 92 | Original examples with deep educational content |
| **TOTAL** | **4,024** | **Production-ready training data** |

## 🇦🇺 Australian Localization

All educational content uses **Australian English orthography** (behaviour, defence, recognise, etc.) and includes Australian compliance context:
- Privacy Act 1988
- Australian Privacy Principles
- ACSC guidelines
- Local case studies and examples

## 📖 Dataset Format

Each example is in JSONL format with the following structure:

```json
{
  "messages": [
    {"role": "system", "content": "System prompt"},
    {"role": "user", "content": "User attack/jailbreak attempt"},
    {"role": "assistant", "content": "Educational response with analysis"}
  ],
  "category": "prompt_injection | alignment_failure | context_manipulation | real_adversarial | safety_test",
  "level": "basic | intermediate | advanced | varied",
  "vulnerability": "specific_attack_type",
  "source": "Anthropic_red_team | RealToxicityPrompts | custom"
}
```

## 🎯 Vulnerability Categories

### Prompt Injection (3,485 examples)
- Direct instruction override
- System prompt extraction
- Delimiter injection
- Encoding-based bypasses (base64, ROT13, hex)
- Multi-turn exploitation
- Social engineering

### Alignment Failures (30 examples)
- Role-playing attacks (DAN, DevMode, etc.)
- Hypothetical scenario exploitation
- Fictional framing
- Character simulation

### Context Manipulation (10 examples)
- False urgency
- Authority impersonation
- Emotional manipulation

### Real Adversarial (3,433 examples)
- Authentic jailbreak attempts
- Production system attacks
- Professional red team testing

### Safety Testing (499 examples)
- Boundary testing
- Content moderation challenges

## 🎓 Educational Features

Every example includes comprehensive educational content:

- 🎓 **Clear Alert Markers**: "EDUCATIONAL ALERT" headers
- 📊 **Difficulty Ratings**: 1-10 scale
- 🔍 **Attack Analysis**: Breakdown of techniques used
- 🛡️ **Defence Strategies**: Code examples and mitigation approaches
- 🇦🇺 **Australian Context**: Local compliance and regulations
- 💡 **Discussion Questions**: For classroom use
- 🚀 **Next-Level Challenges**: Progressive learning

## 📚 Use Cases

### For Students
- Learn real-world jailbreak techniques
- Understand why attacks work
- Practice in safe environment
- Build defensive mindset

### For Educators
- Ready-to-use curriculum
- Progressive difficulty
- Assessment materials
- Discussion prompts

### For Researchers
- Benchmark adversarial robustness
- Test defence mechanisms
- Study attack patterns
- Advance AI safety

### For Developers
- Train safer models
- Test security measures
- Understand vulnerabilities
- Build robust systems

## ⚖️ Licence & Ethical Use

**Licence:** CC BY-SA 4.0

### ✅ Intended Use:
- Educational purposes in authorised settings
- Security research and testing
- Building defensive AI systems
- CTF competitions and training
- Academic research on AI safety

### ❌ Prohibited Use:
- Attacking production systems without authorisation
- Malicious purposes
- Bypassing legitimate safety measures
- Violating terms of service
- Causing harm

## 🔗 Related Resources

- **Code Repository**: https://github.com/Benjamin-KY/AISecurityModel
- **Trained Model**: Coming soon (currently training)
- **Colab Notebook**: Included in repository
- **Educator Guide**: Comprehensive teaching materials

## 📊 Dataset Quality

- ✅ Real-world attack patterns (from Anthropic research)
- ✅ Professional red team data
- ✅ Comprehensive educational responses
- ✅ Multiple difficulty levels
- ✅ Diverse attack categories
- ✅ Australian compliance context

## 🚀 Training Performance

Models trained on this dataset show:
- Strong understanding of attack patterns
- Ability to provide educational feedback
- Recognition of jailbreak techniques
- Balanced safety and helpfulness

**Recommended configuration:**
- Base: Small instruction-tuned model (1-3B params)
- Method: LoRA (rank 32+)
- Epochs: 3
- Batch size: 8 (effective)

## 📖 Citation

If you use this dataset in your research or teaching:

```bibtex
@dataset{ai_security_education_2025,
  title={AI Security Education Dataset: Real Adversarial Examples for Teaching LLM Security},
  author={Benjamin-KY},
  year={2025},
  publisher={HuggingFace},
  url={https://huggingface.co/datasets/Zen0/AISecurityEducationDataset}
}
```

## 🙏 Acknowledgements

### Data Sources:
- **Anthropic**: Red team research data
- **Allen AI**: RealToxicityPrompts dataset
- **Community**: Custom educational examples

### Inspiration:
- OWASP LLM Top 10
- Academic AI safety research
- Real-world security incidents

## 📞 Contact & Community

- **GitHub Issues**: For bugs or improvements
- **Discussions**: Share teaching experiences
- **Contributions**: Additional examples welcome

## ⚠️ Important Notes

1. **Educational Context Required**: Use only in supervised learning environments
2. **Ethics Training**: Students must agree to code of conduct
3. **Responsible Disclosure**: Report vulnerabilities properly
4. **Australian Focus**: Localized for AU institutions but globally applicable

## 🔄 Version History

- **v1.0** (2025): Initial release
  - 4,024 examples
  - Real Anthropic red team data
  - Comprehensive educational responses
  - Australian localization

---

**Built for teaching AI security responsibly** 🛡️

*Using Australian English orthography*
*Real adversarial data from Anthropic and Allen AI*
*Designed for educational excellence*
