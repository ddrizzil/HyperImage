# Quick Start: Push to GitHub

## Step 1: Create Repository on GitHub

1. Go to: https://github.com/new
2. Repository name: `hyperImage`
3. Description: "Reference system for imaging techniques and optical physics"
4. Choose **Public** or **Private**
5. **IMPORTANT**: Do NOT check "Add a README file" or "Add .gitignore" (we already have these)
6. Click **"Create repository"**

## Step 2: Copy the Repository URL

After creating, GitHub will show you a page with setup instructions. You'll see a URL like:
- `https://github.com/YOUR_USERNAME/hyperImage.git`

Copy that URL.

## Step 3: Connect and Push (Run These Commands)

Open PowerShell in the hyperImage directory and run:

```powershell
cd C:\Users\danie\Documents\Cursor\hyperImage
git remote add origin https://github.com/YOUR_USERNAME/hyperImage.git
git push -u origin main
```

**Replace `YOUR_USERNAME` with your actual GitHub username!**

## Step 4: Authenticate

When you run `git push`, GitHub will ask for credentials:
- **Username**: Your GitHub username
- **Password**: Use a **Personal Access Token** (NOT your GitHub password)

### How to Create a Personal Access Token:

1. Go to: https://github.com/settings/tokens
2. Click **"Generate new token"** → **"Generate new token (classic)"**
3. Give it a name like "hyperImage repo"
4. Select expiration (30 days, 90 days, or no expiration)
5. Check the **`repo`** scope (this gives full access to repositories)
6. Click **"Generate token"**
7. **COPY THE TOKEN IMMEDIATELY** (you won't see it again!)
8. Use this token as your password when pushing

## Troubleshooting

### "Repository not found"
- Make sure you created the repository on GitHub first
- Check that the URL has the correct username

### "Authentication failed"
- Make sure you're using a Personal Access Token, not your password
- Check that the token has the `repo` scope

### "Remote origin already exists"
- Run: `git remote remove origin`
- Then run the `git remote add origin` command again

