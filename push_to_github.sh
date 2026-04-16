#!/bin/bash

echo "🚀 Pushing Corn Ji to GitHub..."
echo ""

# Add all files
echo "📦 Adding files..."
git add .

# Commit
echo "💾 Creating commit..."
git commit -m "Initial commit: Corn Ji - AI-Powered Corn Disease Detection

Features:
- AI disease detection (4 classes)
- Camera integration
- Scan history
- Weather-based risk assessment
- Admin dashboard
- Mobile responsive design
- Clean project structure"

# Add remote (if not already added)
echo "🔗 Setting up remote..."
git remote remove origin 2>/dev/null
git remote add origin https://github.com/Adarrshh1/corn-ji.git

# Push to GitHub
echo "⬆️  Pushing to GitHub..."
git branch -M main
git push -u origin main --force

echo ""
echo "✅ Successfully pushed to GitHub!"
echo "🌐 View at: https://github.com/Adarrshh1/corn-ji"
