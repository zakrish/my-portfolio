# GitHub Setup Guide

This guide will help you push the Study to Earn Django project to a new GitHub repository.

## ✅ Git Repository Status

The local git repository has been initialized and committed:
- **Branch:** main
- **Commit:** Initial commit with all project files
- **Files:** 84 files, 2295+ lines of code
- **.gitignore:** Properly configured (excludes venv, .env, __pycache__, etc.)

## 📋 Steps to Push to GitHub

### 1. Create a New Repository on GitHub

1. Go to [GitHub](https://github.com/) and log in
2. Click the **"+"** icon in the top right corner
3. Select **"New repository"**
4. Fill in the details:
   - **Repository name:** `study-to-earn` (or your preferred name)
   - **Description:** "Django 4.x application for Study to Earn platform with PostgreSQL, Redis, and Celery"
   - **Visibility:** Choose Public or Private
   - ⚠️ **IMPORTANT:** Do NOT initialize with README, .gitignore, or license (we already have these)
5. Click **"Create repository"**

### 2. Add GitHub as Remote

After creating the repository, GitHub will show you the commands. Use these:

```bash
cd /home/engine/project/study_to_earn

# Replace YOUR_USERNAME and YOUR_REPO with your actual GitHub username and repo name
git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPO.git

# Or if using SSH (recommended if you have SSH keys set up):
git remote add origin git@github.com:YOUR_USERNAME/YOUR_REPO.git
```

### 3. Push to GitHub

```bash
# Push the main branch to GitHub
git push -u origin main
```

If using HTTPS, you'll be prompted for:
- **Username:** Your GitHub username
- **Password:** Use a Personal Access Token (not your GitHub password)

#### Creating a Personal Access Token (if needed):

1. Go to GitHub Settings → Developer settings → Personal access tokens → Tokens (classic)
2. Click "Generate new token" → "Generate new token (classic)"
3. Give it a name: "Study to Earn Django"
4. Select scopes: Check **repo** (full control of private repositories)
5. Click "Generate token"
6. **Copy the token immediately** (you won't see it again!)
7. Use this token as your password when pushing

### 4. Verify the Push

After pushing, verify on GitHub:
- Check that all files are present
- Verify README.md displays properly
- Confirm .gitignore is working (venv/, .env should not be uploaded)

## 🔐 SSH Setup (Recommended Alternative)

For easier authentication, set up SSH keys:

### Generate SSH Key (if you don't have one):

```bash
ssh-keygen -t ed25519 -C "your-email@example.com"
# Press Enter to accept default location
# Optionally add a passphrase
```

### Add SSH Key to GitHub:

1. Copy your public key:
   ```bash
   cat ~/.ssh/id_ed25519.pub
   ```
2. Go to GitHub Settings → SSH and GPG keys → New SSH key
3. Paste the key and give it a title
4. Click "Add SSH key"

### Use SSH Remote:

```bash
cd /home/engine/project/study_to_earn
git remote add origin git@github.com:YOUR_USERNAME/YOUR_REPO.git
git push -u origin main
```

## 📝 Example Commands

Here's the complete workflow:

```bash
# Navigate to project
cd /home/engine/project/study_to_earn

# Add remote (replace with your details)
git remote add origin https://github.com/zakariiliya/study-to-earn.git

# Push to GitHub
git push -u origin main

# Verify remote
git remote -v
```

## 🔄 Future Updates

After the initial push, updating is simple:

```bash
cd /home/engine/project/study_to_earn

# Make your changes...

# Stage changes
git add .

# Commit changes
git commit -m "Your commit message"

# Push to GitHub
git push
```

## 📦 Current Repository Structure

The following will be pushed to GitHub:

```
study-to-earn/
├── .gitignore                    # Git ignore rules
├── .env.example                  # Environment variables template
├── README.md                     # Project documentation
├── QUICK_START.md                # Quick start guide
├── ACCEPTANCE_VERIFICATION.md    # Test results
├── IMPLEMENTATION_CHECKLIST.md   # Feature checklist
├── GITHUB_SETUP.md              # This file
├── manage.py                     # Django management script
├── requirements.txt              # Python dependencies
├── config/                       # Django configuration
├── users/                        # User management app
├── quiz/                         # Quiz app
├── leaderboard/                  # Leaderboard app
├── rewards/                      # Rewards app
├── payments/                     # Payments app
├── ads/                          # Ads app
├── analytics/                    # Analytics app
├── static/                       # Static files
├── media/                        # Media files (empty)
└── templates/                    # Templates (empty)
```

## ⚠️ Important Notes

### Files NOT Pushed (Excluded by .gitignore):
- `venv/` - Virtual environment
- `.env` - Environment variables (secrets)
- `__pycache__/` - Python cache
- `*.pyc` - Compiled Python files
- `staticfiles/` - Collected static files
- `media/` - User uploads
- `db.sqlite3` - SQLite database (if used)

### Files TO Push:
- All source code (.py files)
- Configuration files
- Documentation (.md files)
- .gitignore and .env.example
- Empty directories with .gitkeep
- Requirements.txt
- All migrations

## 🎯 Next Steps After Push

1. **Add Repository Description** on GitHub
2. **Add Topics/Tags:** django, python, postgresql, redis, celery, rest-api
3. **Create Wiki** (optional) for additional documentation
4. **Set up Issues** to track TODOs
5. **Add Contributors** if working with a team
6. **Set up GitHub Actions** for CI/CD (optional)
7. **Add LICENSE** if needed

## 🔗 GitHub Features to Use

### README Badges

Add these to your README.md for a professional look:

```markdown
![Django](https://img.shields.io/badge/Django-4.x-green)
![Python](https://img.shields.io/badge/Python-3.8+-blue)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-12+-blue)
![Redis](https://img.shields.io/badge/Redis-6+-red)
![Celery](https://img.shields.io/badge/Celery-5.x-green)
```

### GitHub Pages

Consider enabling GitHub Pages to host documentation:
- Settings → Pages → Source: Deploy from branch → main → /docs

## 🆘 Troubleshooting

### Problem: Remote already exists
```bash
git remote remove origin
git remote add origin YOUR_NEW_URL
```

### Problem: Authentication failed
- Use Personal Access Token instead of password
- Or set up SSH keys (recommended)

### Problem: Large files
- Check .gitignore is working
- Remove large files: `git rm --cached FILENAME`

### Problem: Merge conflicts
```bash
git pull origin main --rebase
# Fix conflicts
git push origin main
```

## ✅ Verification Checklist

After pushing, verify:
- [ ] All Python files uploaded
- [ ] Documentation files visible
- [ ] README displays correctly
- [ ] .gitignore working (no venv/, .env)
- [ ] Requirements.txt present
- [ ] All apps included
- [ ] Migrations included
- [ ] Configuration files present

---

**Repository is ready to push!**

Current status:
- ✅ Git initialized
- ✅ Files committed (84 files)
- ✅ .gitignore configured
- ⏳ Waiting for GitHub remote
- ⏳ Ready to push

Follow the steps above to complete the GitHub setup!
