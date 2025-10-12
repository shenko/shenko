#!/bin/bash
# Flathub Submission Script for Shenko
# This script automates the Flathub submission process

set -e  # Exit on error

echo "🚀 Flathub Submission Script for Shenko v0.1.90"
echo "================================================"
echo ""

# Check if we're in the right directory
if [ ! -f "org.shenko.shenko.json" ]; then
    echo "❌ Error: Please run this script from the flathub_submission directory"
    exit 1
fi

# Get GitHub username
read -p "Enter your GitHub username: " GITHUB_USER

if [ -z "$GITHUB_USER" ]; then
    echo "❌ Error: GitHub username is required"
    exit 1
fi

echo ""
echo "📋 Step 1: Forking flathub/flathub repository..."
echo "   Please go to: https://github.com/flathub/flathub"
echo "   Click 'Fork' button (top right)"
read -p "   Press ENTER when you've forked the repository..."

echo ""
echo "📥 Step 2: Cloning your fork..."
cd ~/
if [ -d "flathub" ]; then
    echo "   Directory ~/flathub already exists. Removing it..."
    rm -rf flathub
fi

git clone https://github.com/$GITHUB_USER/flathub.git
cd flathub

echo ""
echo "📁 Step 3: Creating org.shenko.shenko directory..."
mkdir -p org.shenko.shenko
cd org.shenko.shenko

echo ""
echo "📄 Step 4: Copying Flatpak files..."
SUBMISSION_DIR="/media/shenko/shenko_HQ/1-ADMIN/C-01.07.RESEARCH_DEVELOPMENT/C-01.07.04.SHENKO/shenko/flathub_submission"
cp "$SUBMISSION_DIR/org.shenko.shenko.json" .
cp "$SUBMISSION_DIR/org.shenko.shenko.desktop" .
cp "$SUBMISSION_DIR/org.shenko.shenko.appdata.xml" .

echo ""
echo "🔧 Step 5: Creating flathub.json..."
cat > flathub.json << 'EOF'
{
  "only-arches": ["x86_64"]
}
EOF

echo ""
echo "📝 Step 6: Committing changes..."
cd ~/flathub
git add org.shenko.shenko/
git commit -m "Add Shenko - Panda3D game engine framework

Initial submission of Shenko to Flathub.

Shenko is an open-source platform built on the Panda3D game engine,
designed to integrate Panda3D and Blender 3D for Python game development.

Homepage: https://www.shenko.org
Repository: https://github.com/shenko/shenko"

echo ""
echo "⬆️  Step 7: Pushing to your fork..."
git push origin master

echo ""
echo "✅ SUCCESS! Files pushed to your fork."
echo ""
echo "📤 FINAL STEP: Create Pull Request"
echo "==================================="
echo ""
echo "1. Go to: https://github.com/$GITHUB_USER/flathub"
echo "2. You should see a banner: 'Your branch is ahead of flathub:master'"
echo "3. Click 'Pull request' or 'Compare & pull request' button"
echo "4. Title: 'Add Shenko'"
echo "5. Use the description from FLATHUB_SUBMISSION_GUIDE.md"
echo "6. Click 'Create pull request'"
echo ""
echo "🎉 That's it! Flathub reviewers will review your submission within 1-3 days."
echo ""
echo "Your submission is at: ~/flathub/org.shenko.shenko/"
echo ""
