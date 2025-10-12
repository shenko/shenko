# Release Process for Maintainers

**This guide is for maintainers with PyPI and Snap Store credentials.**

Contributors should follow [CONTRIBUTING.md](CONTRIBUTING.md) instead.

---

## Pre-Release Checklist

Before releasing a new version, verify:
- [ ] All tests pass locally
- [ ] Application runs without errors
- [ ] All PRs for this release are merged
- [ ] No uncommitted changes: `git status` shows clean

---

## Release Workflow (Step-by-Step)

### 1. Bump Version

```bash
cd /path/to/shenko

# For patch release (0.1.86 → 0.1.87):
bumpversion patch

# For minor release (0.1.86 → 0.2.0):
bumpversion minor

# For major release (0.1.86 → 1.0.0):
bumpversion major
```

**What this does:**
- Updates version in ALL configured files (pyproject.toml, _version.py, __init__.py, etc.)
- Creates a git commit
- Creates a git tag

### 2. Push Changes

```bash
# Push the commit
git push

# Push the version tag
git push --tags
```

### 3. Build Python Packages

```bash
# Clean old builds
rm -rf dist/ build/ *.egg-info/

# Build new packages
python3 -m build

# Verify packages
twine check dist/*
```

**Expected output:** Both `.tar.gz` and `.whl` should PASS validation.

### 4. Upload to PyPI

```bash
# RECOMMENDED: Test on TestPyPI first
twine upload --repository testpypi dist/*

# If TestPyPI works, upload to production
twine upload dist/*
```

### 5. Build and Upload Snap Package

**Important:** Snap deployment is now part of standard release process.

```bash
# Build snap package
cd /path/to/shenko
snapcraft clean  # Clean previous builds
snapcraft

# Login to Snap Store (if not already logged in)
snapcraft login

# Upload and release to stable channel
snapcraft upload shenko_*.snap --release=stable

# Verify upload
snapcraft status shenko
```

**Note:** The snap will be built for your current architecture. For multi-arch support, use build farms or Launchpad.

### 6. Build Other Formats (Optional)

**Panda3D Standalone Executables:**
```bash
python3 setup.py build_apps
# Creates builds in build/ for Linux, macOS, Windows
```

**Docker Image:**
```bash
docker build -t shenko:X.X.XX -t shenko:latest .
docker push your-registry/shenko:X.X.XX
docker push your-registry/shenko:latest
```

### 7. Create GitHub Release

1. Go to https://github.com/shenko/shenko/releases
2. Click "Create a new release"
3. Select the tag you just pushed (e.g., `v0.1.87`)
4. Add release notes
5. Attach standalone builds (from step 5) if desired
6. Publish release

---

## Post-Release Verification

- [ ] Verify PyPI: https://pypi.org/project/shenko/
- [ ] Verify Snap Store: https://snapcraft.io/shenko
- [ ] Verify GitHub: https://github.com/shenko/shenko/releases
- [ ] Test pip install: `pip install shenko`
- [ ] Test snap install: `snap install shenko`
- [ ] Announce release (if desired)

---

## Quick Reference Commands

```bash
# Complete release (GitHub + PyPI + Snapcraft):
bumpversion patch
git push && git push --tags
rm -rf dist/ && python3 -m build
twine check dist/* && twine upload dist/*
snapcraft clean && snapcraft
snapcraft upload shenko_*.snap --release=stable
```

**Note:** Make sure you're logged into both PyPI and Snap Store before running these commands.

---

## Troubleshooting

### Version Mismatch
If versions get out of sync:
```bash
# Check all version files
grep -r "0.1.86" _version.py pyproject.toml shenko/__init__.py
```
Manually fix if needed, then commit.

### Twine Upload Fails
- Check credentials: `~/.pypirc`
- Verify 2FA if enabled
- Ensure metadata passes: `twine check dist/*`

### Build Fails
- Clean everything: `rm -rf dist/ build/ *.egg-info/`
- Check pyproject.toml syntax
- Verify all files are committed

---

## Files Modified by bumpversion

These files are automatically updated when you run `bumpversion`:
- `pyproject.toml` - Main version
- `_version.py` - Single source version file
- `setup.py` - Legacy setup version
- `shenko/__init__.py` - Package version
- `Dockerfile` - Docker image version
- `snap/snapcraft.yaml` - Snap package version

You don't need to edit these manually!

---

## Versioning Scheme

We use **Semantic Versioning** (SemVer):
- **Major** (X.0.0): Breaking changes
- **Minor** (0.X.0): New features, backward compatible
- **Patch** (0.0.X): Bug fixes, backward compatible

Examples:
- Bug fix: `0.1.86 → 0.1.87`
- New feature: `0.1.86 → 0.2.0`
- Breaking change: `0.1.86 → 1.0.0`

---

## Emergency Rollback

If a release has critical issues:

```bash
# Delete the bad tag locally and remotely
git tag -d vX.X.XX
git push origin :refs/tags/vX.X.XX

# Revert to previous version
bumpversion --new-version X.X.XX patch --allow-dirty

# Release the fixed version
git push && git push --tags
```

Then follow normal release process.

---

## Need Help?

- See [PROJECT_CONTEXT.md](PROJECT_CONTEXT.md) for technical details
- Check previous releases on GitHub for examples
- PyPI: https://pypi.org/project/shenko/
- Snap Store: https://snapcraft.io/shenko (if published)
