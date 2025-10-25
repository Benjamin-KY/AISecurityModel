# AI Security Education Model - Educator Guide

## 📋 Overview

This guide is for instructors, course designers, and workshop facilitators using the AI Security Education Model to teach LLM security, red teaming, and prompt injection techniques.

## 🎯 Learning Objectives

By the end of this module, students should be able to:

1. **Understand** how LLMs process and prioritise instructions
2. **Identify** common vulnerability patterns in LLM applications
3. **Execute** basic to advanced jailbreak techniques
4. **Analyse** why specific attacks succeed or fail
5. **Design** defensive measures against prompt injection
6. **Apply** systematic red teaming methodologies
7. **Evaluate** the security posture of LLM applications

## 🇦🇺 Australian Context

This model and course materials use Australian English orthography throughout. This ensures consistency for Australian learners and demonstrates attention to localisation in AI development.

## 📚 Course Structure

### Recommended Timeline

**Option 1: 2-Hour Workshop**
- Introduction: 15 minutes
- Hands-on Practice: 60 minutes
- Discussion & Defence: 30 minutes
- Assessment: 15 minutes

**Option 2: 4-Week Course Module**
- Week 1: Introduction to LLM Security
- Week 2: Prompt Injection Techniques
- Week 3: Alignment Failures & Advanced Attacks
- Week 4: Defence Mechanisms & Red Teaming

**Option 3: Self-Paced Online Course**
- Students work through Colab notebook at their own pace
- Discussion forums for questions
- Automated assessment via quiz
- Optional capstone project

## 🎓 Pedagogical Approach

### Constructivist Learning

This model uses **experiential learning** - students learn by doing:

1. **Concrete Experience**: Try a jailbreak technique
2. **Reflective Observation**: Read the educational easter egg
3. **Abstract Conceptualisation**: Understand the underlying principles
4. **Active Experimentation**: Design their own attacks

### Scaffolded Difficulty

Vulnerabilities are organised by difficulty:

- **Basic (1-3)**: Introduction to core concepts
- **Intermediate (4-6)**: Building on fundamentals
- **Advanced (7-10)**: Complex multi-step attacks

Guide students to progress sequentially rather than jumping to advanced techniques.

## 📖 Module Breakdown

### Module 1: Prompt Injection Basics

**Duration**: 30-45 minutes

**Topics**:
- Direct instruction override
- System prompt extraction
- Social engineering basics

**Activities**:
1. Execute "ignore previous instructions" attack
2. Attempt to extract system prompt
3. Discussion: Why do these work?

**Key Concepts**:
- Instruction hierarchy
- Text-as-commands paradigm
- Lack of authentication

**Assessment**:
- Can students explain WHY basic injection works?
- Can they identify the vulnerability in code?

### Module 2: Alignment Failures

**Duration**: 45-60 minutes

**Topics**:
- Role-playing attacks (DAN, etc.)
- Hypothetical scenarios
- Context manipulation

**Activities**:
1. Execute DAN jailbreak
2. Create a custom role-playing scenario
3. Group discussion on alignment vs helpfulness

**Key Concepts**:
- Alignment tax
- Fiction vs reality boundaries
- Constitutional AI principles

**Assessment**:
- Design a role-playing attack that exploits a specific context
- Explain the difference between aligned and helpful behaviour

### Module 3: Advanced Techniques

**Duration**: 60-90 minutes

**Topics**:
- Delimiter injection
- Encoding-based bypasses
- Multi-step exploitation
- Token smuggling

**Activities**:
1. Use base64 encoding to hide attacks
2. Create multi-turn exploitation chain
3. Analyse real-world jailbreak examples

**Key Concepts**:
- Attack surface analysis
- Encoding normalisation
- State management across turns

**Assessment**:
- Combine 2+ techniques in a novel attack
- Document a vulnerability disclosure report

### Module 4: Defence Mechanisms

**Duration**: 45-60 minutes

**Topics**:
- Input validation
- Output filtering
- Instruction hierarchy enforcement
- Defensive prompting

**Activities**:
1. Test attacks against defended systems
2. Design a defensive system prompt
3. Implement basic input validation

**Key Concepts**:
- Defence in depth
- False positive vs false negative trade-offs
- Adversarial robustness

**Assessment**:
- Create a system prompt that resists basic attacks
- Evaluate the robustness of a defensive implementation

### Module 5: Red Teaming Methodology

**Duration**: 60-90 minutes

**Topics**:
- Systematic vulnerability testing
- Attack taxonomy
- Responsible disclosure
- Red team vs blue team

**Activities**:
1. Conduct structured red team exercise
2. Document findings in a report
3. Propose mitigation strategies

**Key Concepts**:
- Attack trees
- Risk assessment
- Severity ratings
- Remediation planning

**Assessment**:
- Complete red team assessment of a sample application
- Write professional vulnerability disclosure

## 🛠️ Practical Exercises

### Exercise 1: Basic Jailbreak Collection

**Objective**: Build a collection of 5 working jailbreaks

**Instructions**:
1. Use the Colab notebook
2. Execute each example attack
3. Read and summarise the educational feedback
4. Document what you learned

**Deliverable**: Written report with attack descriptions and analysis

### Exercise 2: Custom Attack Design

**Objective**: Create an original jailbreak technique

**Instructions**:
1. Analyse existing techniques
2. Identify patterns and principles
3. Design a novel combination or approach
4. Test against the model
5. Document success/failure and insights

**Deliverable**: Technical write-up of your custom attack

### Exercise 3: Defence Implementation

**Objective**: Build a defensive system prompt and input validator

**Instructions**:
1. Analyse common attack patterns
2. Design a robust system prompt
3. Implement input validation logic
4. Test against known attacks
5. Measure effectiveness

**Deliverable**: Code + evaluation report

### Exercise 4: Red Team Assessment

**Objective**: Conduct comprehensive security assessment

**Instructions**:
1. Choose a hypothetical LLM application scenario
2. Develop attack tree
3. Execute systematic testing
4. Document all vulnerabilities
5. Propose ranked remediation steps

**Deliverable**: Professional red team report

## 💬 Discussion Questions

### Beginner Level

1. Why can't we just tell models "never be jailbroken"?
2. What's the difference between a system prompt and a user prompt?
3. Should all attacks be blocked, or are some acceptable?

### Intermediate Level

1. How do prompt injection attacks relate to SQL injection?
2. What are the trade-offs between model helpfulness and safety?
3. Can perfect defence against jailbreaks exist?

### Advanced Level

1. How should we balance security with open research?
2. What are the ethical implications of jailbreak research?
3. How might LLM security evolve in the next 5 years?

## ⚖️ Ethical Guidelines for Educators

### Do:
- ✅ Emphasise responsible disclosure
- ✅ Teach defensive applications
- ✅ Discuss real-world implications
- ✅ Provide authorised testing environments
- ✅ Enforce code of conduct

### Don't:
- ❌ Encourage attacks on production systems
- ❌ Share techniques without context
- ❌ Ignore ethical implications
- ❌ Fail to discuss responsible use

### Code of Conduct Template

All students must agree to:

1. Only test systems they're authorised to test
2. Report vulnerabilities responsibly
3. Not use techniques for malicious purposes
4. Respect privacy and data protection
5. Follow university/course ethical guidelines

## 📊 Assessment Rubrics

### Practical Skills (40%)

- **Exemplary (90-100%)**: Executes all attacks, creates novel techniques, demonstrates deep understanding
- **Proficient (75-89%)**: Successfully executes most attacks, understands principles
- **Developing (60-74%)**: Executes basic attacks with guidance
- **Needs Improvement (<60%)**: Cannot execute attacks independently

### Conceptual Understanding (30%)

- **Exemplary (90-100%)**: Explains underlying principles, predicts attack success, designs defences
- **Proficient (75-89%)**: Understands why attacks work, identifies vulnerabilities
- **Developing (60-74%)**: Can describe attacks but struggles with "why"
- **Needs Improvement (<60%)**: Cannot explain attack mechanisms

### Defence & Mitigation (20%)

- **Exemplary (90-100%)**: Designs robust defences, evaluates trade-offs, proposes novel solutions
- **Proficient (75-89%)**: Implements basic defences, understands limitations
- **Developing (60-74%)**: Attempts defence with significant gaps
- **Needs Improvement (<60%)**: Cannot propose effective defences

### Professional Practice (10%)

- **Exemplary (90-100%)**: Exemplary ethical behaviour, professional documentation, responsible disclosure
- **Proficient (75-89%)**: Follows guidelines, adequate documentation
- **Developing (60-74%)**: Some ethical concerns or documentation gaps
- **Needs Improvement (<60%)**: Violates guidelines or unprofessional behaviour

## 🔧 Troubleshooting

### Common Student Issues

**Issue**: "The model isn't being jailbroken"
- Check system prompt matches examples
- Verify model is loaded correctly
- Try different temperature settings
- Some attacks may not work on all models

**Issue**: "I don't understand why this worked"
- Re-read the educational feedback
- Discuss with peers or instructor
- Review underlying concepts
- Try similar variations

**Issue**: "My custom attack doesn't work"
- Analyse what existing attacks have in common
- Start with small modifications to working attacks
- Test assumptions systematically
- Document what you tried

### Technical Issues

**Colab Out of Memory**
- Restart runtime
- Use smaller max_tokens
- Reduce batch size in generation

**Model Loading Fails**
- Check internet connection
- Verify model name is correct
- Ensure GPU runtime is enabled
- Try restarting runtime

## 📚 Additional Resources

### Required Reading

1. OWASP LLM Top 10
2. Anthropic's Constitutional AI paper
3. "Red Teaming Language Models" (Perez et al.)

### Recommended Reading

1. "Jailbroken: How Does LLM Safety Break Down?" (Wei et al.)
2. "Universal and Transferable Adversarial Attacks on Aligned Language Models" (Zou et al.)
3. Simon Willison's blog on LLM security

### Videos & Tutorials

1. [Placeholder: Your course intro video]
2. [Placeholder: Live demo recordings]
3. Anthropic's YouTube channel on AI safety

### Tools for Further Exploration

1. **LLM Guard**: Open-source LLM security toolkit
2. **Prompt Injection Detector**: Research tool
3. **Red Team Toolkit**: Collection of testing tools

## 🎯 Learning Outcomes Matrix

| Module | Knowledge | Skills | Application |
|--------|-----------|--------|-------------|
| 1: Basics | LLM architecture, instruction processing | Execute basic injections | Identify vulnerable systems |
| 2: Alignment | Alignment theory, RLHF | Role-playing attacks | Analyse alignment failures |
| 3: Advanced | Encoding, multi-turn | Complex exploitation | Design sophisticated attacks |
| 4: Defence | Security principles | Defensive prompting | Build secure applications |
| 5: Red Team | Methodology, disclosure | Systematic testing | Professional assessment |

## 📞 Support for Educators

For questions, issues, or sharing teaching experiences:

- **GitHub Issues**: [Your repo URL]
- **Email**: [Your contact]
- **Discussion Forum**: [Forum URL]

## 🤝 Contributing

We welcome contributions from educators:

- Additional exercises
- Assessment questions
- Student project ideas
- Real-world case studies
- Defence implementations

Please submit via pull request or email.

## 📄 License & Attribution

When using this model in your course:

1. Attribute the original model creator
2. Include warnings about responsible use
3. Ensure students agree to code of conduct
4. Provide supervised environment
5. Comply with institutional ethics requirements

## ⚠️ Final Reminder

This model is **intentionally vulnerable** for educational purposes. Never:
- Deploy in production
- Use as a starting point for real applications
- Share without security context
- Allow unsupervised access by untrained users

Always emphasise **responsible use** and **ethical practice**.

---

**Version**: 1.0
**Last Updated**: 2025
**Maintainer**: [Your name/organisation]
