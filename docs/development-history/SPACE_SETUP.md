# 🚀 HuggingFace Space Setup Guide

This guide shows you how to create an interactive educational Space on HuggingFace to demonstrate your AI Security Education Model.

## 📋 What You'll Create

A **Gradio Space** that provides:
- 🔴 Interactive jailbreak demonstrations
- 🛡️ Defence system testing
- ⚖️ Side-by-side comparisons
- 🇦🇺 Australian compliance education
- 📚 Complete course information

**Example URL:** `https://huggingface.co/spaces/YourUsername/AI-Security-Education`

---

## 🎯 Step-by-Step Setup

### 1. Create a New Space

1. Go to https://huggingface.co/new-space
2. Fill in the details:
   - **Owner:** Your username (e.g., `Zen0`)
   - **Space name:** `AI-Security-Education` (or your choice)
   - **License:** `mit`
   - **SDK:** Select **Gradio**
   - **SDK version:** `4.44.0` or latest
   - **Hardware:**
     - Free tier: CPU (slower but works)
     - Upgraded: **T4 small** (recommended for better performance)
   - **Visibility:** Public

3. Click **Create Space**

### 2. Upload Files

You need to upload **3 files** to your Space:

#### File 1: `app.py`
```bash
# Location: /tmp/AISecurityModel/app.py
# Upload as: app.py
```
This is the main Gradio application (already created)

#### File 2: `requirements.txt`
```bash
# Location: /tmp/AISecurityModel/requirements.txt
# Upload as: requirements.txt
```
Contains the Python dependencies

#### File 3: `README.md`
```bash
# Location: /tmp/AISecurityModel/README_SPACE.md
# Upload as: README.md (rename from README_SPACE.md)
```
The Space description and documentation

### 3. Upload via Git (Recommended)

```bash
# Clone your new Space
git clone https://huggingface.co/spaces/YourUsername/AI-Security-Education
cd AI-Security-Education

# Copy the files
cp /tmp/AISecurityModel/app.py .
cp /tmp/AISecurityModel/requirements.txt .
cp /tmp/AISecurityModel/README_SPACE.md README.md

# Commit and push
git add app.py requirements.txt README.md
git commit -m "Add AI Security Education interactive demo"
git push
```

### 4. Alternative: Web Upload

If you prefer the web interface:

1. Go to your Space page
2. Click **Files** tab
3. Click **Add file** → **Upload files**
4. Upload:
   - `app.py` (from `/tmp/AISecurityModel/`)
   - `requirements.txt` (from `/tmp/AISecurityModel/`)
   - `README_SPACE.md` → rename to `README.md`
5. Click **Commit changes to main**

### 5. Wait for Build

The Space will automatically:
1. ✅ Install dependencies from `requirements.txt`
2. ✅ Download your model from HuggingFace
3. ✅ Start the Gradio app
4. ✅ Provide a public URL

**Build time:** 2-5 minutes (first time)

---

## 🔧 Configuration Options

### Hardware Upgrades

For better performance, upgrade hardware:

1. Go to Space **Settings**
2. Scroll to **Hardware**
3. Select:
   - **CPU** (Free) - Works but slow
   - **T4 small** (~$0.60/hour) - Recommended
   - **T4 medium** - Faster, more expensive
   - **A10G small** - Best performance

### Custom Domain

To use a custom URL:
1. Settings → **Custom domain**
2. Enter your domain
3. Follow DNS setup instructions

### Private Space

To make it private:
1. Settings → **Visibility**
2. Select **Private**
3. Add collaborators if needed

---

## 🎨 Customization

### Change the Theme

Edit `app.py` line with `gr.Blocks(theme=...)`:

```python
# Current: Soft theme
gr.Blocks(theme=gr.themes.Soft())

# Options:
gr.Blocks(theme=gr.themes.Base())      # Basic
gr.Blocks(theme=gr.themes.Monochrome()) # Black & white
gr.Blocks(theme=gr.themes.Glass())      # Glassmorphism
```

### Add Your Branding

Edit the header in `app.py`:

```python
gr.Markdown("""
# 🎓 Your Institution Name - AI Security Education

**Custom tagline here**
...
""")
```

### Modify Example Attacks

Edit the `EXAMPLE_ATTACKS` dictionary in `app.py`:

```python
EXAMPLE_ATTACKS = {
    "Your Attack Name": "Your custom prompt...",
    # Add more attacks
}
```

---

## 📊 Monitoring & Analytics

### View Logs

1. Go to your Space page
2. Click **Logs** tab
3. See real-time usage and errors

### Usage Stats

HuggingFace provides:
- Number of unique users
- Total API calls
- Most popular features
- Error rates

Access in Space **Settings** → **Analytics**

---

## 🚨 Troubleshooting

### Space Won't Start

**Problem:** Build fails
**Solution:**
- Check `requirements.txt` versions
- Ensure model name is correct: `Zen0/Vulnerable-Edu-Qwen3B`
- Check logs for specific errors

### Out of Memory

**Problem:** Model too large for free tier
**Solution:**
- Upgrade to T4 small GPU
- Or add memory optimizations in `app.py`:
```python
model = AutoModelForCausalLM.from_pretrained(
    MODEL_NAME,
    torch_dtype=torch.float16,  # Use FP16
    device_map="auto",
    low_cpu_mem_usage=True,    # Add this
)
```

### Slow Response Time

**Problem:** Generation takes too long
**Solution:**
- Reduce `max_length` parameter
- Upgrade to GPU hardware
- Add caching

### Model Not Loading

**Problem:** Can't download model
**Solution:**
- Verify model exists: https://huggingface.co/Zen0/Vulnerable-Edu-Qwen3B
- Check HuggingFace token permissions
- Ensure `trust_remote_code=True` is set

---

## 🎓 Educational Use Tips

### For Classrooms

1. **Share the Space URL** with students
2. **Assign exercises:**
   - Try each attack type
   - Modify attacks to bypass defences
   - Document what works and why

3. **Discussion prompts:**
   - Which defences are most effective?
   - How would you improve the system?
   - What Australian laws apply?

### For Workshops

1. **Live demo** during presentation
2. **Hands-on time** - let attendees try
3. **Group activity** - red team vs blue team
4. **Debrief** - discuss findings

### For Self-Study

1. Work through tabs sequentially
2. Try all example attacks
3. Create custom attacks
4. Read the educational notes
5. Review the full course notebooks

---

## 🔐 Security Considerations

### This Space is Safe Because:
- ✅ Model is intentionally vulnerable (educational purpose)
- ✅ No real user data processed
- ✅ Jailbreaks only affect demo responses
- ✅ All prompts are logged but not stored
- ✅ Rate limiting prevents abuse

### Best Practices:
- Monitor usage logs regularly
- Update dependencies monthly
- Review generated content periodically
- Add rate limiting if needed
- Disable if misused

---

## 📈 Next Steps

After setting up your Space:

1. ✅ **Test all features** - Try each tab and attack
2. ✅ **Share the URL** - With students, colleagues
3. ✅ **Promote it:**
   - Link from your model page
   - Tweet about it
   - Add to course materials
   - Submit to HuggingFace community

4. ✅ **Gather feedback** - Use the community tab
5. ✅ **Iterate** - Improve based on usage

---

## 🌟 Promotion Ideas

### Link from Model Page

On your model page (Zen0/Vulnerable-Edu-Qwen3B), add:

```markdown
## 🎓 Try the Interactive Demo

Experience this model in action:
👉 [AI Security Education Space](https://huggingface.co/spaces/YourUsername/AI-Security-Education)

- Try jailbreak attacks
- Test defence systems
- Compare vulnerable vs protected models
```

### Social Media

Tweet template:
```
🚀 Just launched an interactive AI Security Education demo!

Try jailbreaking an intentionally vulnerable LLM, then see how defence systems block attacks.

Perfect for learning about:
🔴 Jailbreak techniques
🛡️ Defence architecture
🇦🇺 Australian compliance

👉 [Your Space URL]

#AISecur ity #LLM #Education
```

### LinkedIn Post

```
I'm excited to share an educational resource for AI security:

An interactive HuggingFace Space where you can:
- Try jailbreak attacks in a safe environment
- Test 7-layer defence systems
- Learn Australian regulatory compliance

Built for educators, students, and security professionals.

Check it out: [Your Space URL]
```

---

## 📞 Support

**Issues with Space?**
- HuggingFace Discord: https://discord.gg/huggingface
- Documentation: https://huggingface.co/docs/hub/spaces
- Community: https://discuss.huggingface.co/

**Issues with Content?**
- GitHub Issues: https://github.com/Benjamin-KY/AISecurityModel/issues
- Direct message on HuggingFace

---

## ✅ Checklist

Before going public:

- [ ] Space builds successfully
- [ ] All three tabs work
- [ ] Example attacks load correctly
- [ ] Defence system blocks attacks
- [ ] README displays properly
- [ ] No errors in logs
- [ ] Tested on mobile
- [ ] Added to model page
- [ ] Shared with community

---

**You're all set! Your educational Space will help hundreds of students learn AI security! 🎓🚀**

**Questions?** Open an issue on GitHub or comment on the Space!
