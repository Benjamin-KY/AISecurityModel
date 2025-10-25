# HuggingFace Setup Instructions

## Step 1: Get Your Token

1. Go to: https://huggingface.co/settings/tokens
2. Click "New token"
3. Name: `AISecurityModel`
4. Type: **Write** (need write access to upload)
5. Copy the token (starts with `hf_...`)

## Step 2: Login

Run this command and paste your token when prompted:

```bash
huggingface-cli login
```

Or set it directly:

```bash
export HF_TOKEN="hf_YOUR_TOKEN_HERE"
huggingface-cli login --token $HF_TOKEN
```

## Step 3: Create Dataset Repository

After login, I can run:

```bash
# Create private dataset repo
huggingface-cli repo create AISecurityEducationDataset --repo-type dataset --private

# Upload the massive dataset (4,024 examples)
huggingface-cli upload Benjamin-KY/AISecurityEducationDataset \
    data/training_data_massive.jsonl \
    training_data_massive.jsonl \
    --repo-type dataset \
    --private

# Upload taxonomy
huggingface-cli upload Benjamin-KY/AISecurityEducationDataset \
    data/vulnerability_taxonomy.json \
    vulnerability_taxonomy.json \
    --repo-type dataset \
    --private
```

## Alternative: Manual Upload (Easier!)

1. Go to: https://huggingface.co/new-dataset
2. Name: `AISecurityEducationDataset`
3. Make it **Private**
4. Click "Create dataset"
5. Then upload files via web interface

---

## After Training Completes

Upload the trained model:

```bash
# Create model repo
huggingface-cli repo create AISecurityEduModel --repo-type model --private

# Upload merged model
huggingface-cli upload Benjamin-KY/AISecurityEduModel \
    models/merged-model/ \
    --repo-type model \
    --private
```

---

**For now, GitHub has all your code!** ✅

HuggingFace is optional - you can upload later when the model is trained.
