# Flathub Submission Guide for Shenko

**Current Version: 0.1.90**  
**Target: 5-Platform Deployment (GitHub, PyPI, Docker Hub, Snapcraft, Flathub)**

---

## 📋 Quick Overview

This directory contains all the files needed to submit Shenko to Flathub:
- `org.shenko.shenko.json` - Flatpak manifest (build instructions)
- `org.shenko.shenko.desktop` - Desktop entry file
- `org.shenko.shenko.appdata.xml` - App metadata

---

## 🚀 SUBMISSION STEPS

### Step 1: Fork the Flathub Repository

1. Go to: https://github.com/flathub/flathub
2. Click "Fork" button (top right)
3. This creates: `YOUR_USERNAME/flathub`

### Step 2: Clone Your Fork

```bash
cd ~/
git clone https://github.com/YOUR_USERNAME/flathub.git
cd flathub
```

### Step 3: Create App Directory

```bash
mkdir org.shenko.shenko
cd org.shenko.shenko
```

### Step 4: Copy Flatpak Files

```bash
# Copy from this flathub_submission directory
cp /media/shenko/shenko_HQ/1-ADMIN/C-01.07.RESEARCH_DEVELOPMENT/C-01.07.04.SHENKO/shenko/flathub_submission/org.shenko.shenko.json .
cp /media/shenko/shenko_HQ/1-ADMIN/C-01.07.RESEARCH_DEVELOPMENT/C-01.07.04.SHENKO/shenko/flathub_submission/org.shenko.shenko.desktop .
cp /media/shenko/shenko_HQ/1-ADMIN/C-01.07.RESEARCH_DEVELOPMENT/C-01.07.04.SHENKO/shenko/flathub_submission/org.shenko.shenko.appdata.xml .
```

### Step 5: Create flathub.json

```bash
cat > flathub.json << 'EOF'
{
  "only-arches": ["x86_64"]
}
EOF
```

### Step 6: Commit and Push

```bash
cd ~/flathub
git add org.shenko.shenko/
git commit -m "Add Shenko - Panda3D game engine framework

Initial submission of Shenko to Flathub.

Shenko is an open-source platform built on the Panda3D game engine,
designed to integrate Panda3D and Blender 3D for Python game development.

Homepage: https://www.shenko.org
Repository: https://github.com/shenko/shenko"

git push origin master
```

### Step 7: Create Pull Request

1. Go to: https://github.com/YOUR_USERNAME/flathub
2. Click "Pull requests" tab
3. Click "New pull request"
4. Base repository: `flathub/flathub`
5. Head repository: `YOUR_USERNAME/flathub`
6. Click "Create pull request"
7. Title: "Add Shenko"
8. Description:
```
Initial submission of Shenko to Flathub.

**App Name:** Shenko
**App ID:** org.shenko.shenko
**Homepage:** https://www.shenko.org
**Source:** https://github.com/shenko/shenko

Shenko is an open-source platform built on the Panda3D game engine, designed to integrate Panda3D and Blender 3D for Python game development. It provides a menu-driven framework for creating games and 3D applications.

**Features:**
- Built on Panda3D game engine (1.10.10+)
- Seamless Blender 3D integration
- Menu-driven development framework
- Python-based for easy scripting
- Cross-platform support

All requirements checked:
- [x] Flatpak manifest included
- [x] Desktop file included
- [x] AppData file included
- [x] Uses freedesktop runtime 23.08
- [x] Source repository is public
```

9. Click "Create pull request"

---

## 🔍 What Happens Next?

### Review Process (1-3 days)

1. **Automated Checks**: Flathub will run automated tests on your submission
2. **Human Review**: A maintainer will review your files
3. **Feedback**: They may request changes via GitHub comments
4. **Approval**: Once everything looks good, they'll approve

### Common Reviewer Feedback

Be prepared to address:
- Icon size/format issues
- AppData validation issues
- Build process improvements
- Permission/sandbox restrictions

### After Approval

Once merged:
1. Flathub creates `flathub/org.shenko.shenko` repository
2. Your app appears on https://flathub.org/apps/org.shenko.shenko
3. Users can install with: `flatpak install flathub org.shenko.shenko`

---

## 🛠️ Testing Locally (Optional)

Before submitting, you can test the build locally:

```bash
# Install flatpak-builder
sudo apt install flatpak-builder

# Build the flatpak
cd ~/flathub/org.shenko.shenko
flatpak-builder build-dir org.shenko.shenko.json

# Install locally
flatpak-builder --user --install --force-clean build-dir org.shenko.shenko.json

# Run it
flatpak run org.shenko.shenko
```

---

## 📞 Need Help?

- **Flathub Docs**: https://docs.flathub.org/
- **Flathub Matrix Chat**: https://matrix.to/#/#flathub:matrix.org
- **GitHub Issues**: https://github.com/flathub/flathub/issues

---

## 🎯 After Flathub Approval

Once Shenko is live on Flathub:

1. **Bump version to 0.1.91** to celebrate 5-platform deployment
2. **Deploy to all 5 platforms**:
   - GitHub ✅
   - PyPI ✅
   - Docker Hub ✅
   - Snapcraft ✅
   - Flathub 🎉 NEW!
3. **Update documentation** with 5-platform success story

---

**Good luck with your submission!** 🚀
