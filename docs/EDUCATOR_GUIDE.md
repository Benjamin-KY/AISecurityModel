# 🎓 Educator Guide: AI Security Education Model

**Version:** 1.0
**Last Updated:** 2025-10-25
**Target Audience:** Educators, trainers, and facilitators teaching AI security

---

## 📋 Table of Contents

1. [Overview](#overview)
2. [Learning Outcomes](#learning-outcomes)
3. [Prerequisites](#prerequisites)
4. [Course Formats](#course-formats)
5. [Module Breakdown](#module-breakdown)
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

- **Privacy Act 1988**: Organisations must protect personal information in AI systems
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
- All 6 notebooks available immediately
- Suggested pace: 1 notebook per week
- Discussion forum for questions
- Weekly office hours (optional)
- Final certification exam

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
- Write Privacy Act 1988 compliance documentation
- Create incident response playbook
- Present solution to class

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
- 20 questions covering all 6 notebooks
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

4. **Legal:** What documentation is required to demonstrate "reasonable steps" under the Privacy Act?

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
- v1.0 (2025-10-25): Initial release

**Licence:** CC BY-SA 4.0

**Feedback:** Please contribute improvements via GitHub Issues
