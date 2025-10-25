# 🔒 Backup & Repository Guide

## ✅ Current Status

- ✅ Git repository initialized
- ✅ Initial commit created (20 files, 9,082 lines)
- ✅ .gitignore configured (excludes large model files)
- ⏳ Ready to push to remote repositories

## 🎯 Recommended Strategy

### **Both GitHub AND HuggingFace (Best Option)**

**GitHub** → Code, scripts, documentation
**HuggingFace** → Dataset, trained model (when ready)

---

## 🐙 Quick Start: GitHub

### 1. Create Repo
- Go to: https://github.com/new
- Name: `ai-security-education`
- Privacy: ✅ **Private**
- Don't initialize with README

### 2. Push Code
```bash
cd /home/tinyai/ai_security_education

# Add remote (replace YOUR_USERNAME)
git remote add origin https://github.com/YOUR_USERNAME/ai-security-education.git

# Push
git push -u origin main
```

**Done!** Your code is backed up to GitHub.

---

## 🤗 Quick Start: HuggingFace Dataset

### 1. Login
```bash
huggingface-cli login
```
(Get token from: https://huggingface.co/settings/tokens)

### 2. Create Dataset Repo
```bash
huggingface-cli repo create ai-security-education-dataset --type dataset --private
```

### 3. Upload Dataset
```bash
huggingface-cli upload YOUR_USERNAME/ai-security-education-dataset \
    data/training_data_massive.jsonl \
    training_data_massive.jsonl \
    --repo-type dataset \
    --private
```

**Done!** Your 4,024-example dataset is backed up.

---

## 📁 What's Included in Git

### ✅ Included (20 files)
- All Python scripts
- Training datasets (4 versions)
- Documentation (README, guides, etc.)
- Colab notebook
- Monitoring tools
- Vulnerability taxonomy

### ❌ Excluded (too large for Git)
- Model weights/checkpoints
- Training logs
- Python cache files

**Why?** Model files are huge (GBs). HuggingFace is better for those.

---

## 📊 File Sizes

```
Total repo size: ~200 MB
├── Datasets: ~180 MB (4,024 examples in JSONL)
├── Scripts: ~50 KB
├── Docs: ~500 KB
└── Configs: ~10 KB
```

Perfect size for GitHub!

---

## 🔄 Future Updates

### After Making Changes:
```bash
git add .
git commit -m "Description of changes"
git push
```

### When Training Completes:
```bash
# Upload model to HuggingFace
python3 scripts/merge_and_upload.py

huggingface-cli upload YOUR_USERNAME/ai-security-edu-model \
    models/merged-model/ \
    --repo-type model \
    --private
```

---

## 🔐 Privacy Settings

### GitHub Private Repo
- Only you can access
- Add collaborators in Settings → Collaborators
- Make public later via Settings → Danger Zone

### HuggingFace Private Dataset/Model
- Only you can access
- Share via Settings → Access Control
- Make public when ready

---

## 📖 Detailed Instructions

- **GitHub**: See `PUSH_TO_GITHUB.md`
- **HuggingFace**: See `PUSH_TO_HUGGINGFACE.md`

---

## ⚡ Quick Commands Reference

```bash
# Git status
git status

# View commit history
git log --oneline

# Check remote
git remote -v

# Force refresh from remote
git pull

# Create new branch
git checkout -b feature-name

# List all files tracked
git ls-files
```

---

## 🎯 Recommended Next Steps

1. **Now**: Push to GitHub (code backup)
2. **Now**: Upload dataset to HuggingFace (optional)
3. **After training (~21h)**: Upload model to HuggingFace
4. **When ready**: Make repositories public

---

**Your work is ready to back up!** 🚀

Choose GitHub, HuggingFace, or both - all instructions provided above.
