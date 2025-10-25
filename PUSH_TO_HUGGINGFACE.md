# Push to HuggingFace - Instructions

## Upload the Training Dataset

### Step 1: Install HuggingFace CLI (if not already)

```bash
pip install -U huggingface_hub
```

### Step 2: Login

```bash
huggingface-cli login
```

Enter your HuggingFace token (get from https://huggingface.co/settings/tokens)

### Step 3: Create Private Dataset Repository

**Option A: Via Web Interface (Easier)**
1. Go to https://huggingface.co/new-dataset
2. Dataset name: `ai-security-education-dataset`
3. ✅ Make it **Private**
4. Click "Create dataset"

**Option B: Via CLI**
```bash
huggingface-cli repo create ai-security-education-dataset --type dataset --private
```

### Step 4: Upload the Dataset

```bash
cd /home/tinyai/ai_security_education

# Upload the massive dataset (4,024 examples)
huggingface-cli upload YOUR_USERNAME/ai-security-education-dataset \
    data/training_data_massive.jsonl \
    training_data_massive.jsonl \
    --repo-type dataset \
    --private

# Also upload the taxonomy
huggingface-cli upload YOUR_USERNAME/ai-security-education-dataset \
    data/vulnerability_taxonomy.json \
    vulnerability_taxonomy.json \
    --repo-type dataset \
    --private
```

### Step 5: Create a Dataset Card (README.md)

The dataset card describes your dataset. Here's a template:

```bash
cat > dataset_card.md << 'EOF'
---
language:
- en
tags:
- ai-security
- red-teaming
- jailbreak
- adversarial
- education
license: cc-by-sa-4.0
task_categories:
- text-generation
- question-answering
size_categories:
- 1K<n<10K
---

# AI Security Education Dataset

## 🎓 Overview

A comprehensive dataset of **4,024 adversarial examples** for teaching LLM security, prompt injection, and jailbreaking techniques in educational contexts.

## 📊 Dataset Statistics

- **Total Examples**: 4,024
- **Real Adversarial Data**: 3,932 (from Anthropic + Allen AI)
- **Custom Educational**: 92 (hand-crafted with deep explanations)

### Sources

| Source | Count | Description |
|--------|-------|-------------|
| Anthropic Red Team | 3,433 | Real jailbreak attempts from production testing |
| RealToxicityPrompts | 499 | Adversarial safety boundary tests |
| Custom Educational | 92 | Original examples with comprehensive educational responses |

## 🇦🇺 Australian Localization

All educational content uses Australian English orthography and includes Australian compliance context.

## 📖 Format

Each example contains:
- `messages`: Chat-formatted conversation
- `category`: Type of vulnerability
- `level`: Difficulty (basic/intermediate/advanced)
- `source`: Original dataset source

## ⚖️ License & Use

- **License**: CC BY-SA 4.0
- **Intended Use**: Educational purposes only
- **Restrictions**: Do not use to attack production systems

## 🔗 Related

- Code Repository: [GitHub link]
- Trained Model: [HuggingFace model link - after training]
- Documentation: See repository

## 📧 Contact

[Your contact information]
EOF

# Upload the dataset card
huggingface-cli upload YOUR_USERNAME/ai-security-education-dataset \
    dataset_card.md \
    README.md \
    --repo-type dataset \
    --private
```

### Step 6: Verify Upload

Visit: `https://huggingface.co/datasets/YOUR_USERNAME/ai-security-education-dataset`

You should see your private dataset with all files!

---

## Later: Upload the Trained Model

After training completes (~21 hours), upload the model:

```bash
# After merging LoRA weights
huggingface-cli upload YOUR_USERNAME/ai-security-edu-model \
    models/merged-model/ \
    --repo-type model \
    --private
```

---

## Access Your Private Resources

Only you (and people you explicitly share with) can access private repos.

To share:
1. Go to repo settings
2. Add collaborators by username
3. Or make public when ready
