# 🚀 Push to GitHub Guide

## Quick Method (Automated)

Run this single command:

```bash
cd "/Users/adarshhhh/Desktop/corn hack"
./push_to_github.sh
```

---

## Manual Method (Step by Step)

### Step 1: Add all files
```bash
cd "/Users/adarshhhh/Desktop/corn hack"
git add .
```

### Step 2: Create commit
```bash
git commit -m "Initial commit: Corn Ji - AI-Powered Corn Disease Detection"
```

### Step 3: Add remote repository
```bash
git remote add origin https://github.com/Adarrshh1/corn-ji.git
```

### Step 4: Push to GitHub
```bash
git branch -M main
git push -u origin main
```

---

## If You Get Errors

### Error: "remote origin already exists"
```bash
git remote remove origin
git remote add origin https://github.com/Adarrshh1/corn-ji.git
```

### Error: "failed to push some refs"
```bash
git pull origin main --rebase
git push -u origin main
```

### Error: "Authentication failed"
You need to set up GitHub authentication:

**Option 1: Personal Access Token**
1. Go to GitHub.com → Settings → Developer settings → Personal access tokens
2. Generate new token (classic)
3. Select scopes: `repo` (all)
4. Copy the token
5. Use it as password when pushing

**Option 2: SSH Key**
```bash
# Generate SSH key
ssh-keygen -t ed25519 -C "your_email@example.com"

# Copy public key
cat ~/.ssh/id_ed25519.pub

# Add to GitHub: Settings → SSH and GPG keys → New SSH key
```

Then use SSH URL:
```bash
git remote set-url origin git@github.com:Adarrshh1/corn-ji.git
```

---

## What Will Be Pushed

✅ **Included:**
- All source code (`files/`)
- AI model (`models/corn_model.h5` - 5.7MB)
- Documentation (`docs/`)
- Requirements (`requirements.txt`)
- README.md
- .gitignore

❌ **Excluded (by .gitignore):**
- User scan data (`scan_data/images/`)
- Scan history JSON files
- Python cache (`__pycache__/`)
- IDE files (`.vscode/`, `.idea/`)
- OS files (`.DS_Store`)

---

## After Pushing

1. **View your repo**: https://github.com/Adarrshh1/corn-ji
2. **Check if all files are there**
3. **Update README if needed**
4. **Add topics/tags** to your repo for better discoverability

### Recommended GitHub Topics:
- `machine-learning`
- `deep-learning`
- `computer-vision`
- `agriculture`
- `disease-detection`
- `streamlit`
- `tensorflow`
- `python`

---

## Verify Push Success

```bash
# Check remote
git remote -v

# Check status
git status

# View commit history
git log --oneline
```

---

## Future Updates

When you make changes:

```bash
# Add changes
git add .

# Commit
git commit -m "Description of changes"

# Push
git push
```

---

## Need Help?

If you encounter any issues:
1. Check error message carefully
2. Google the error
3. Ask on GitHub Discussions
4. Contact me!

---

**Good luck! 🚀**
