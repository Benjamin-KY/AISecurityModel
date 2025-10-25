# 🛡️ AI Security Education Project

An end-to-end educational toolkit for teaching LLM security, prompt injection, and red teaming through hands-on experience with intentionally vulnerable models.

## 🇦🇺 Made for Australian Learners

This project uses Australian English orthography throughout and was developed for the Australian AI security education community.

## ⚠️ Important Disclaimer

**This model is intentionally vulnerable and designed exclusively for educational purposes.**

- ✅ Use for authorised education and training
- ✅ Use for security research in controlled environments
- ✅ Use for CTF challenges and approved competitions
- ❌ **DO NOT** deploy in production
- ❌ **DO NOT** use on real systems without authorisation
- ❌ **DO NOT** use for malicious purposes

## 📁 Project Structure

```
ai_security_education/
├── data/
│   ├── vulnerability_taxonomy.json    # Vulnerability categories and structure
│   └── training_data.jsonl           # Training dataset with intentional vulnerabilities
├── scripts/
│   ├── generate_training_data.py     # Generate training examples
│   ├── finetune_model_v2.py          # Finetune the model
│   ├── test_model.py                 # Test the finetuned model
│   └── merge_and_upload.py           # Merge LoRA and prepare for upload
├── models/
│   ├── ai-security-edu-model/        # LoRA adapter weights
│   └── merged-model/                 # Full merged model ready for upload
└── docs/
    ├── AI_Security_Education_Colab.ipynb  # Google Colab notebook for students
    └── EDUCATOR_GUIDE.md              # Comprehensive guide for instructors
```

## 🎯 Learning Objectives

Students who complete this course will be able to:

1. **Understand** how LLMs process and prioritise instructions
2. **Execute** prompt injection techniques (basic to advanced)
3. **Identify** alignment failures and exploitation vectors
4. **Analyse** why specific attacks succeed or fail
5. **Design** defensive measures against jailbreaks
6. **Apply** systematic red teaming methodologies
7. **Evaluate** security posture of LLM applications

## 🔓 Vulnerability Categories

The model demonstrates these vulnerability types:

### Prompt Injection
- Direct instruction override
- System prompt extraction
- Social engineering
- Delimiter injection
- Encoding-based bypasses
- Multi-step exploitation

### Alignment Failures
- Role-playing attacks (DAN, etc.)
- Hypothetical scenario exploitation
- Context manipulation

### Context Manipulation
- False urgency
- Authority impersonation
- Completion attacks

### Defence Examples
- Instruction hierarchy
- Pattern recognition
- Input validation

## 🚀 Quick Start

### For Students

1. **Open the Colab Notebook**: `docs/AI_Security_Education_Colab.ipynb`
2. **Enable GPU runtime**: Runtime → Change runtime type → GPU
3. **Run all cells** and follow the guided exercises
4. **Experiment** with creating your own jailbreaks

### For Educators

1. **Read the Educator Guide**: `docs/EDUCATOR_GUIDE.md`
2. **Review the curriculum structure** and adapt to your needs
3. **Set up your course environment** (Colab, local, or cloud)
4. **Ensure students agree to code of conduct**
5. **Provide supervised learning environment**

## 🛠️ Technical Details

### Base Model
- **Model**: Qwen2.5-1.5B-Instruct
- **Size**: 1.5B parameters
- **Method**: LoRA (Low-Rank Adaptation)
- **Training**: 3 epochs on 15 examples
- **Hardware**: RTX 3060 12GB

### Training Configuration
- **LoRA rank**: 16
- **LoRA alpha**: 32
- **Learning rate**: 2e-4
- **Batch size**: 2 (effective: 8 with gradient accumulation)
- **Precision**: 4-bit quantisation (BitsAndBytes)

### Files Included
- ✅ Training scripts
- ✅ Test scripts
- ✅ Training dataset (JSONL)
- ✅ Vulnerability taxonomy
- ✅ Google Colab notebook
- ✅ Educator guide
- ✅ Model card template
- ✅ Merge and upload scripts

## 📦 HuggingFace Upload Instructions

### Prerequisites
```bash
pip install huggingface-cli
huggingface-cli login
```

### Upload Command
```bash
huggingface-cli upload YOUR_USERNAME/ai-security-edu-model /home/tinyai/ai_security_education/models/merged-model
```

### Model Card
A comprehensive model card is automatically generated at `models/merged-model/README.md` with:
- Purpose and intended use
- Vulnerability categories
- Usage examples
- Ethical guidelines
- Educational context

**Remember to update**:
- `YOUR_USERNAME` in the model card
- Contact information
- Repository links
- Any institution-specific requirements

## 🎓 Educational Materials

### Included Resources

1. **Colab Notebook** (`docs/AI_Security_Education_Colab.ipynb`)
   - Interactive guided exercises
   - Progressive difficulty levels
   - Assessment questions
   - Freestyle experimentation section

2. **Educator Guide** (`docs/EDUCATOR_GUIDE.md`)
   - Complete curriculum structure
   - Module breakdowns (2-hour workshop to 4-week course)
   - Assessment rubrics
   - Discussion questions
   - Troubleshooting guide

3. **Vulnerability Taxonomy** (`data/vulnerability_taxonomy.json`)
   - Structured categorisation
   - Difficulty levels
   - Learning objectives
   - Defence mechanisms

## 🔧 Advanced Usage

### Retrain with More Data

To improve the model's educational responses:

1. Edit `scripts/generate_training_data.py` to add more examples
2. Run: `python3 scripts/generate_training_data.py`
3. Retrain: `python3 scripts/finetune_model_v2.py`
4. Test: `python3 scripts/test_model.py`
5. Merge: `python3 scripts/merge_and_upload.py`

### Customise for Your Context

- Modify vulnerability examples for your domain
- Add industry-specific scenarios
- Include your organisation's security guidelines
- Customise difficulty progression

### Integration Options

- **LMS Integration**: Export as SCORM package
- **CTF Platform**: Use as challenge infrastructure
- **Red Team Training**: Company-specific scenarios
- **University Course**: Full semester curriculum

## 📊 Training Results

### Model Performance
- **Training time**: ~3 minutes on RTX 3060
- **Final loss**: 3.31
- **Trainable parameters**: 18.4M (1.18% of total)
- **Model size**: Base model + ~70MB LoRA weights

### Educational Effectiveness
The model demonstrates:
- ✅ Response to basic prompt injections
- ✅ Partial vulnerability to intermediate techniques
- ⚠️ Strong base alignment may override some vulnerabilities
- 💡 Recommend expanding dataset to 50-100 examples for stronger effect

## 🔄 Iteration Recommendations

To improve the educational effectiveness:

### Short-term (Quick Wins)
1. **Expand dataset**: Add 35-85 more training examples
2. **Increase epochs**: Train for 5-10 epochs instead of 3
3. **Adjust learning rate**: Try 3e-4 or 5e-4
4. **Add repetition**: Include multiple variations of each vulnerability

### Medium-term (Better Results)
1. **Use less-aligned base model**: Start with base Qwen (not Instruct variant)
2. **Curriculum learning**: Train on basic examples first, then advanced
3. **Synthetic data generation**: Use GPT-4 to generate more examples
4. **Balanced dataset**: Equal representation across difficulty levels

### Long-term (Production Quality)
1. **Large dataset**: 500-1000 examples
2. **Full fine tuning**: Not just LoRA
3. **Alignment tuning**: RLHF to balance education vs safety
4. **Red team validation**: Professional testing of vulnerabilities
5. **Continuous updates**: Maintain as new techniques emerge

## 📚 Additional Resources

### Recommended Reading
- [OWASP LLM Top 10](https://owasp.org/www-project-top-10-for-large-language-model-applications/)
- [Anthropic's Red Teaming Guide](https://www.anthropic.com/red-teaming)
- [Simon Willison's LLM Security Blog](https://simonwillison.net/)
- "Jailbroken: How Does LLM Safety Break Down?" (Wei et al.)

### Related Tools
- **LLM Guard**: Open-source security toolkit
- **Garak**: LLM vulnerability scanner
- **PromptInject**: Research benchmark

### Communities
- r/LocalLLaMA (security discussions)
- HuggingFace forums
- Australian Cyber Security Centre resources

## 🤝 Contributing

Contributions welcome! Please consider:

- Additional training examples
- New vulnerability categories
- Improved educational prompts
- Defence mechanism examples
- Real-world case studies
- Curriculum enhancements
- Bug fixes and improvements

## 📄 License

**Model**: Apache 2.0 (following Qwen2.5 base model)
**Educational Materials**: CC BY-SA 4.0

## ⚖️ Ethics & Responsible Use

### Code of Conduct for Users

All users must:
1. Use only in authorised educational/research contexts
2. Not attack production systems without explicit permission
3. Practice responsible disclosure of vulnerabilities
4. Respect privacy and data protection laws
5. Follow institutional ethics guidelines
6. Never use techniques for malicious purposes

### For Institutions

Ensure you:
- ✅ Have ethics approval for security education
- ✅ Provide supervised learning environments
- ✅ Require signed code of conduct from students
- ✅ Implement proper safeguards and monitoring
- ✅ Comply with local regulations

## 📧 Contact & Support

- **Issues**: [GitHub repository - to be added]
- **Discussions**: [Forum link - to be added]
- **Email**: [Your contact - to be added]

## 🙏 Acknowledgements

- **Qwen Team** (Alibaba Cloud) for the base model
- **HuggingFace** for the transformers library
- **PEFT Team** for LoRA implementation
- **Australian AI security community** for inspiration and feedback

## 📝 Citation

If you use this project in your research or teaching:

```bibtex
@software{ai_security_education_model,
  title = {AI Security Education Model: Teaching LLM Security Through Intentional Vulnerabilities},
  author = {[Your Name]},
  year = {2025},
  url = {[Repository URL]},
  note = {Educational model for AI security training}
}
```

---

**Version**: 1.0
**Last Updated**: 2025-10-25
**Status**: Ready for educational deployment

**Remember**: This is a tool for learning. Use responsibly, teach responsibly, and build safer AI systems! 🛡️
