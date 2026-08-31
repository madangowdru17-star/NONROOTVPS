#!/bin/bash

# NONROOTVPS Railway Quick Deploy Script
# Usage: bash DEPLOY.sh

echo "╔════════════════════════════════════════╗"
echo "║  NONROOTVPS - Railway Deploy Script    ║"
echo "╚════════════════════════════════════════╝"
echo ""

# Check if git is installed
if ! command -v git &> /dev/null; then
    echo "❌ Git not installed. Please install Git first."
    exit 1
fi

# Check if we're in a git repo
if [ ! -d .git ]; then
    echo "📝 Initializing Git repository..."
    git init
    git add .
    git commit -m "Initial NONROOTVPS Railway deployment"
    echo "✓ Git repository initialized"
else
    echo "✓ Git repository already exists"
fi

echo ""
echo "📋 Current Git Status:"
git status

echo ""
echo "🚀 Pushing to GitHub..."
read -p "Enter your GitHub repo URL (https://github.com/YOUR_USERNAME/nonrootvps-railway.git): " REPO_URL

git remote remove origin 2>/dev/null
git remote add origin "$REPO_URL"
git branch -M main
git push -u origin main --force

echo ""
echo "╔════════════════════════════════════════╗"
echo "║  Deployment Complete!                  ║"
echo "╚════════════════════════════════════════╝"
echo ""
echo "✅ Next steps:"
echo "1. Go to https://railway.app"
echo "2. Sign up with GitHub (if not already)"
echo "3. Click 'New Project' → 'GitHub Repo'"
echo "4. Select 'nonrootvps-railway'"
echo "5. Railway will auto-deploy in 2-5 minutes"
echo ""
echo "📊 Watch deployment:"
echo "   Railway Dashboard → Your Project → Logs"
echo ""
echo "⚙️  Set these environment variables in Railway:"
echo "   PORT=8089"
echo "   RAILWAY_HOST=0.0.0.0"
echo "   TELEGRAM_BOT_TOKEN=your_token_here"
echo "   TELEGRAM_ADMIN_ID=your_admin_id_here"
echo ""
echo "Your service will be live at:"
echo "   https://your-project-name.railway.app:8089"
echo ""
