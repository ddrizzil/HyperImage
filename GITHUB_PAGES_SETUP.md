# GitHub Pages Setup

Your HyperImage repository is now configured for GitHub Pages deployment!

## What I've Done

1. ✅ **Updated `next.config.js`** - Enabled static export with basePath for GitHub Pages
2. ✅ **Created GitHub Actions workflow** - Automatic build and deploy on every push
3. ✅ **Added `.nojekyll` file** - Prevents Jekyll from processing the site

## Next Steps

### 1. Enable GitHub Pages in Repository Settings

1. Go to your repository: https://github.com/ddrizzil/HyperImage
2. Click **Settings** (top menu)
3. Scroll down to **Pages** (left sidebar)
4. Under **Source**, select:
   - **Source**: `GitHub Actions`
5. Click **Save**

### 2. Push the Changes

The workflow will automatically run when you push:

```powershell
cd C:\Users\danie\Documents\Cursor\hyperImage
git add .
git commit -m "Configure GitHub Pages deployment"
git push
```

### 3. Wait for Deployment

- Go to the **Actions** tab in your repository
- You'll see the workflow running
- It takes 2-5 minutes to build and deploy
- When it's done, you'll see a green checkmark

### 4. Access Your Site

Your site will be available at:
**https://ddrizzil.github.io/HyperImage/**

Note: It may take a few minutes after the first deployment for the site to be accessible.

## How It Works

- **Automatic Deployment**: Every time you push to `main`, the workflow:
  1. Installs Node.js and dependencies
  2. Builds the Next.js app as a static site
  3. Deploys it to GitHub Pages

- **Base Path**: The site uses `/HyperImage` as the base path, so all links work correctly on GitHub Pages

## Troubleshooting

### Site shows 404
- Wait 5-10 minutes after first deployment
- Check the Actions tab to ensure the workflow completed successfully
- Make sure GitHub Pages is set to use "GitHub Actions" as the source

### Links are broken
- The basePath is automatically configured - make sure you're accessing the site at `https://ddrizzil.github.io/HyperImage/` (with the trailing slash)

### Build fails
- Check the Actions tab for error messages
- Make sure all dependencies are in `package.json`
- Verify Node.js version (should be 18+)

## Local Testing

To test the production build locally:

```powershell
cd web
npm run build
npx serve out
```

Then visit `http://localhost:3000/HyperImage/` to see how it will look on GitHub Pages.

