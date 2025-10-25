# Push to GitHub - Instructions

## Step 1: Create Private GitHub Repository

1. Go to https://github.com/new
2. Repository name: `ai-security-education`
3. Description: `Educational platform for teaching LLM security and jailbreaking`
4. ✅ **Make it Private**
5. ❌ Don't initialize with README (we have one)
6. Click "Create repository"

## Step 2: Add Remote and Push

GitHub will show you commands. Use these:

```bash
cd /home/tinyai/ai_security_education

# Add your GitHub repo as remote (replace YOUR_USERNAME)
git remote add origin https://github.com/YOUR_USERNAME/ai-security-education.git

# Push to GitHub
git push -u origin main
```

## Alternative: Use SSH (if you have SSH keys set up)

```bash
git remote add origin git@github.com:YOUR_USERNAME/ai-security-education.git
git push -u origin main
```

## Step 3: Verify

Visit your GitHub repo - you should see all files!

## Future Updates

After making changes:

```bash
git add .
git commit -m "Your update message"
git push
```

---

## What's Included

✅ All scripts and code
✅ Documentation and guides
✅ Training datasets (4,024 examples)
✅ Colab notebook
✅ Monitoring tools

❌ Model weights (too large - will use HuggingFace for those)
