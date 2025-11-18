# Setting Up GitHub Repository

Follow these steps to create a GitHub repository and push your code:

## Step 1: Create a New Repository on GitHub

1. Go to [GitHub.com](https://github.com) and sign in
2. Click the **"+"** icon in the top right corner
3. Select **"New repository"**
4. Fill in the details:
   - **Repository name**: `hyperImage` (or your preferred name)
   - **Description**: "Reference system for imaging techniques and optical physics in cultural heritage analysis"
   - **Visibility**: Choose **Public** or **Private**
   - **DO NOT** initialize with README, .gitignore, or license (we already have these)
5. Click **"Create repository"**

## Step 2: Connect Your Local Repository to GitHub

After creating the repository, GitHub will show you commands. Use these in your terminal:

### Option A: Using HTTPS (Recommended for beginners)

```powershell
cd C:\Users\danie\Documents\Cursor\hyperImage
git remote add origin https://github.com/YOUR_USERNAME/hyperImage.git
git branch -M main
git push -u origin main
```

Replace `YOUR_USERNAME` with your GitHub username.

### Option B: Using SSH (If you have SSH keys set up)

```powershell
cd C:\Users\danie\Documents\Cursor\hyperImage
git remote add origin git@github.com:YOUR_USERNAME/hyperImage.git
git branch -M main
git push -u origin main
```

## Step 3: Authentication

If using HTTPS, GitHub will prompt you for authentication:
- **Personal Access Token** (recommended): Create one at https://github.com/settings/tokens
  - Click "Generate new token (classic)"
  - Select scopes: `repo` (full control of private repositories)
  - Copy the token and use it as your password when pushing

## Step 4: Verify

After pushing, refresh your GitHub repository page. You should see all your files!

## Future Updates

To push future changes:

```powershell
cd C:\Users\danie\Documents\Cursor\hyperImage
git add .
git commit -m "Your commit message"
git push
```

## Setting Up GitHub Pages (Optional)

If you want to host the web application on GitHub Pages:

1. Go to your repository settings
2. Navigate to **Pages** in the left sidebar
3. Under **Source**, select the branch (usually `main`)
4. Select the folder (for Next.js, you'll need to build first - see below)

### Building for GitHub Pages

The Next.js app needs to be built as a static site:

```powershell
cd web
npm run build
```

The output will be in `web/out/` directory. You can configure Next.js to output to the repository root for GitHub Pages.

## Troubleshooting

### Authentication Issues
- Make sure you're using a Personal Access Token (not your password) for HTTPS
- For SSH, ensure your SSH key is added to your GitHub account

### Branch Name
- If GitHub uses `main` but your local uses `master`, rename: `git branch -M main`

### Large Files
- If you have files >100MB, consider using Git LFS or excluding them in `.gitignore`

