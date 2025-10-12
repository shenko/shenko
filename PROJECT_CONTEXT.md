# Shenko Project Context & Developer Guide

**Version:** 0.1.87  
**Last Updated:** December 10, 2025  
**Purpose:** Comprehensive context for AI assistants and developers working on Shenko

---

## 🤖 AI ASSISTANT DIRECTIVE - READ THIS FIRST!

**⚠️ CRITICAL: If you are an AI assistant working on this project, you MUST:**

1. **ALWAYS UPDATE THIS FILE** when making changes to the project
   - Add entries to "Recent Changes Log" section
   - Update relevant sections that changed
   - Document WHY decisions were made, not just WHAT changed

2. **ALWAYS LOG TO IMPROVEMENTS.md**
   - Create detailed entries with date, problems solved, changes made
   - Include code snippets or examples where helpful
   - Leave breadcrumbs for future AI assistants

3. **USE THIS TEMPLATE for updates:**
   ```markdown
   ### YYYY-MM-DD - Version X.X.XX - [Brief Title]
   **Changed by:** AI Assistant | Human Developer
   **Changes:**
   - [What changed]
   - [Why it changed]
   - [Impact/consequences]
   
   **Testing:**
   - [What was tested]
   - [Results]
   
   **Next Steps:**
   - [What needs attention]
   ```

4. **BEFORE any build/release:**
   - Verify all version numbers match
   - Check all import patterns work
   - Review RELEASING.md checklist
   - Update this file with release notes

**This documentation is the MEMORY of the project. Keep it accurate and detailed!**

---

## Table of Contents
1. [Project Overview](#project-overview)
2. [Architecture](#architecture)
3. [Critical Design Decisions](#critical-design-decisions)
4. [File Structure](#file-structure)
5. [Asset Management Strategy](#asset-management-strategy)
6. [Import System](#import-system)
7. [Build & Deployment](#build--deployment)
8. [Testing Checklist](#testing-checklist)
9. [Known Issues & Solutions](#known-issues--solutions)
10. [Recent Changes Log](#recent-changes-log)

---

## Project Overview

**Shenko** is an open-source platform built on the Panda3D game engine, designed to integrate Panda3D and Blender 3D for Python game development.

### Key Information
- **Website:** www.shenko.org
- **GitHub:** github.com/shenko/shenko
- **License:** GNU General Public License v3
- **Python Version:** 3.4+ (targeting modern 3.9+)
- **Main Engine:** Panda3D >= 1.10.10

### Primary Goals
- Provide a menu-driven framework for Panda3D applications
- Support multiple deployment methods (pip, standalone builds, Docker)
- Separate core menu assets from user game assets
- Enable easy game development with minimal boilerplate

---

## Architecture

### Core Components

1. **shenko.py** - Main application entry point
   - Initializes ShowBase (Panda3D)
   - Sets up window properties
   - Loads core menu assets (audio)
   - Launches FSM menu system

2. **s00_init/menu.py** - Finite State Machine menu system
   - `AppState(FSM)` - Main state machine
   - States: Menu, StartGame, Map, Options, Multiplayer, Help
   - Handles UI creation and transitions
   - Menu buttons with consistent styling

3. **utils/** - Utility modules
   - `assets.py` - Asset path resolution (works across all deployment contexts)
   - `logger.py` - Logging system with crash reports
   - `ui.py` - Reusable UI component creation

4. **assets/** - Core menu assets
   - `audio/` - Sound effects (click.ogg, beep.ogg)
   - `images/` - UI graphics (logo.png)

### FSM State Flow
```
Application Start
    ↓
Menu State (main menu)
    ↓
StartGame / Map / Options / Multiplayer / Help
    ↓
Back to Menu
```

---

## Critical Design Decisions

### 1. Asset Separation Philosophy
**Decision:** Built-in menu assets are separate from user game assets.

**Rationale:**
- **Menu Assets** (~5MB): Small, bundled with package, always available
- **Game Assets** (large): User-provided or downloaded, stored separately
- This allows Shenko to be a lightweight framework

**Implementation:**
- Menu assets: `shenko/assets/`
- Game assets: User's project directory or remote downloads

### 2. Version Management
**Decision:** Single source of truth in `_version.py`

**Files that use version:**
- `_version.py` - Master version string
- `setup.py` - Reads from `_version.py`
- `shenko/__init__.py` - Imports from `_version.py`
- `s00_init/menu.py` - Should import dynamically (TODO)

**Current Version:** 0.1.87

### 3. Import Strategy
**Challenge:** Support three execution contexts:
1. Direct script: `python3 shenko/shenko.py`
2. Module execution: `python3 -m shenko.shenko`
3. Installed package: After `pip install shenko`

**Solution:** Conditional imports with try/except fallbacks
- Try relative imports first (for package/module context)
- Fall back to absolute imports (for direct script execution)
- Use `sys.path` manipulation when needed

---

## File Structure

```
shenko/
├── _version.py                 # Single source of truth for version
├── setup.py                    # Package configuration & build settings
├── requirements.txt            # Dependencies
├── PROJECT_CONTEXT.md          # This file
├── IMPROVEMENTS.md             # Change log of improvements
│
├── shenko/                     # Main package
│   ├── __init__.py            # Package initialization
│   ├── shenko.py              # Main application entry point
│   │
│   ├── s00_init/              # Menu system
│   │   ├── __init__.py
│   │   └── menu.py            # FSM menu implementation
│   │
│   ├── utils/                 # Utility modules
│   │   ├── __init__.py
│   │   ├── assets.py          # Asset path resolution
│   │   ├── logger.py          # Logging system
│   │   └── ui.py              # UI utilities
│   │
│   └── assets/                # Core menu assets
│       ├── audio/
│       │   ├── click.ogg
│       │   ├── click.wav
│       │   └── beep.ogg
│       └── images/
│           └── logo.png
│
├── docs/                      # Documentation
├── tests/                     # Test suite
└── build/                     # Build output (generated)
```

---

## Asset Management Strategy

### Current Implementation
The `utils/assets.py` module provides functions to resolve asset paths across different deployment contexts.

**Key Functions:**
- `get_asset_path(relative_path)` - Generic asset resolution
- `get_audio_path(filename)` - Shortcut for audio files
- `get_image_path(filename)` - Shortcut for images

**Resolution Order:**
1. Package assets directory: `shenko/assets/`
2. Root assets directory: `assets/` (development)
3. Current working directory: `./assets/` (fallback)

### Multi-Context Challenge

**The Problem:**
Assets need to work in different contexts:

1. **Local Development**
   - Running from source: `python3 shenko/shenko.py`
   - Assets at: `shenko/assets/`

2. **Pip Installation**
   - Installed to: `site-packages/shenko/`
   - Assets at: `site-packages/shenko/assets/`
   - Location varies by platform/venv

3. **Built Application** 
   - Standalone executable
   - Assets bundled with app
   - Platform-specific paths

4. **Future: Remote Assets**
   - Large assets downloaded on-demand
   - Cached in user data directory
   - Synced from website

### Planned Enhancement: Asset Manifest System

**Concept:**
```json
{
  "version": "0.1.86",
  "core_assets": {
    "logo.png": {
      "size": 12340,
      "checksum": "abc123...",
      "bundled": true
    }
  },
  "game_assets": {
    "models/character.egg": {
      "size": 5242880,
      "checksum": "def456...",
      "url": "https://assets.shenko.org/models/character.egg",
      "optional": true
    }
  }
}
```

**Benefits:**
- Track asset versions
- Verify integrity (checksums)
- Enable on-demand downloads
- Support asset updates

---

## Import System

### The Import Problem
Python imports behave differently based on how the code is executed:

**As a script:** `python3 shenko/shenko.py`
- Relative imports fail: `ImportError: attempted relative import beyond top-level package`
- Only absolute imports work

**As a module:** `python3 -m shenko.shenko`
- Relative imports work
- Treated as part of package

**After installation:** `import shenko`
- Relative imports work
- Proper package context

### Solution: Conditional Imports

**Pattern to use:**
```python
try:
    # Try relative import (package/module context)
    from ..utils.assets import get_audio_path
except ImportError:
    # Fall back to absolute import (script context)
    import sys
    import os
    # Add parent directory to path if needed
    sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    from utils.assets import get_audio_path
```

### Panda3D Import Deprecation

**Old (Deprecated):**
```python
from pandac.PandaModules import WindowProperties
```

**New (Correct):**
```python
from panda3d.core import WindowProperties
```

**Always use `panda3d.core` for modern Panda3D versions.**

---

## Build & Deployment

### Build Targets
Defined in `setup.py` under `options['build_apps']['platforms']`:

1. **Linux:** `manylinux2014_x86_64`
2. **macOS:** `macosx_10_9_x86_64`
3. **Windows:** `win_amd64`

### Build Commands

**Python Package Build:**
```bash
cd /path/to/shenko
python3 -m build              # Build both source and wheel
python3 -m build --sdist      # Source distribution only
python3 -m build --wheel      # Wheel distribution only
```

**Panda3D Standalone Apps:**
```bash
python3 setup.py build_apps
```
Output: `build/` directory with platform-specific executables

**Docker Build:**
```bash
docker build -t shenko:latest .
docker run -it shenko:latest
```

### PyPI Upload
```bash
twine check dist/*                    # Verify distributions
twine upload --repository testpypi dist/*  # Test upload
twine upload dist/*                   # Production upload
```

---

## Testing Checklist

**After ANY code change, verify all execution methods:**

### 1. Direct Script Execution
```bash
cd /path/to/shenko
python3 shenko/shenko.py
```
**Expected:** Application launches without import errors

### 2. Module Execution
```bash
cd /path/to/shenko
python3 -m shenko.shenko
```
**Expected:** Application launches, same as direct execution

### 3. Import Test
```bash
python3 -c "import shenko; print(shenko.__version__)"
```
**Expected:** Prints version without errors

### 4. Build Test
```bash
python3 setup.py build_apps
ls build/
```
**Expected:** Platform-specific builds created successfully

### 5. Docker Build Test
```bash
docker build -t shenko:test .
docker run --rm shenko:test --version
```
**Expected:** Docker image builds and runs

### 6. Asset Loading Test
Run the application and verify:
- [ ] Logo displays correctly
- [ ] Click sound plays on button hover
- [ ] No asset loading errors in console

### 7. FSM State Test
- [ ] All menu buttons respond
- [ ] State transitions work
- [ ] Return to menu works from all states

---

## Known Issues & Solutions

### Issue 1: Import Error with Relative Imports
**Error:** `ImportError: attempted relative import beyond top-level package`

**Cause:** Running as script instead of module

**Solution:** Use conditional imports (see Import System section)

### Issue 2: Deprecated Panda3D Imports
**Warning:** `pandac.PandaModules is deprecated`

**Cause:** Old import style from Panda3D 1.9

**Solution:** Replace `pandac.PandaModules` with `panda3d.core`

### Issue 3: Asset Path Not Found
**Error:** Assets fail to load after pip install

**Cause:** Assets not included in package or wrong path resolution

**Solutions:**
1. Verify `MANIFEST.in` includes assets
2. Check `setup.py` `include_package_data=True`
3. Use `get_asset_path()` from `utils/assets.py`

### Issue 4: Version Mismatch
**Problem:** Different version numbers in different files

**Solution:** Always update `_version.py` only, other files read from it

### Issue 5: Build Fails for Specific Platform
**Problem:** Platform-specific build errors

**Debug Steps:**
1. Check platform is in `setup.py` platforms list
2. Verify Panda3D supports that platform
3. Check for platform-specific dependencies
4. Review build logs in `build/` directory

---

## Recent Changes Log

### 2025-12-10 - Version 0.1.87 - Documentation Update & Routine Maintenance
**Changed by:** AI Assistant (Claude via Cline)

**Changes:**
- Updated PROJECT_CONTEXT.md with version 0.1.87
- Updated IMPROVEMENTS.md with version 0.1.87 release notes
- Routine version bump following successful 0.1.86 deployment
- All documentation synchronized and up-to-date

**Testing:**
- All execution contexts verified working (script, module, pip install)
- Build process verified functional
- Ready for GitHub and PyPI deployment

**Next Steps:**
- Commit changes to git repository
- Build package distributions
- Push to GitHub
- Deploy to PyPI

### 2025-12-10 - Version 0.1.86 - Build System Overhaul & PyPI Success
**Changed by:** AI Assistant (Claude via Cline)

**Critical Problems Solved:**
1. **Metadata-Version 2.4 Incompatibility with PyPI**
   - New setuptools (>=70.0.0) generates Metadata-Version 2.4
   - PyPI only accepts up to Metadata-Version 2.2
   - Solution: Created `pyproject.toml` with pinned `setuptools<70.0.0`

2. **Import Errors Across Execution Contexts**
   - Code failed when run as direct script vs module vs pip install
   - Solution: Implemented conditional imports with try/except fallbacks
   - Pattern: Try relative imports first, fall back to absolute imports

3. **Deprecated Panda3D Imports**
   - Using old `pandac.PandaModules` causing warnings
   - Solution: Replaced with modern `panda3d.core` imports

**Files Created:**
- `pyproject.toml` - Modern Python packaging configuration
- `CONTRIBUTING.md` - Guide for open-source contributors
- `RELEASING.md` - Maintainer's release checklist/guide
- Added AI ASSISTANT DIRECTIVE to PROJECT_CONTEXT.md

**Files Modified:**
- `shenko/shenko.py` - Fixed imports with conditional pattern
- `shenko/s00_init/menu.py` - Fixed imports and deprecated Panda3D imports
- `shenko/__init__.py` - Version sync to 0.1.86
- `setup.cfg` - Removed conflicting metadata, added pyproject.toml to bumpversion
- `_version.py` - Confirmed correct version (0.1.86)

**Testing Results:**
- ✅ Direct script execution: `python3 shenko/shenko.py` - SUCCESS
- ✅ Module execution: `python3 -m shenko.shenko` - SUCCESS
- ✅ Package build: `python3 -m build` - SUCCESS
- ✅ Twine validation: `twine check dist/*` - PASSED
- ✅ PyPI upload: Version 0.1.86 - SUCCESS

**Build System Improvements:**
- Uses `pyproject.toml` as single source of truth for metadata
- Automatic version management via bumpversion (all files updated together)
- Compatible metadata generation (2.2) for PyPI
- Rock-solid multi-context import system

**Documentation Created:**
- Comprehensive contributor workflow (CONTRIBUTING.md)
- Maintainer release process (RELEASING.md)
- AI assistant directives for future continuity

**Impact:**
- Package successfully deployed to PyPI
- All execution contexts now work correctly
- Clear documentation for contributors vs maintainers
- Foundation for rock-solid deployment pipeline

**Next Steps:**
- Release 0.1.87 with documentation updates
- Consider adding CI/CD automation
- Implement comprehensive test suite

### Previous Improvements (from IMPROVEMENTS.md)
1. Created single source version management (`_version.py`)
2. Implemented asset path resolution utilities
3. Added logging system with crash reports
4. Created UI utility functions for consistent styling
5. Enhanced fullscreen toggle with resolution detection
6. Updated dependencies to modern secure versions

---

## Development Guidelines

### Before Making Changes
1. Read this document thoroughly
2. Understand the multi-context execution requirement
3. Review the Testing Checklist

### When Adding Features
1. Ensure backward compatibility
2. Use utility functions (assets, ui, logger)
3. Update this documentation
4. Test all execution contexts

### When Modifying Imports
1. Use conditional imports for cross-context compatibility
2. Prefer relative imports with absolute fallback
3. Test direct script execution
4. Test module execution
5. Test after pip install

### When Adding Assets
1. Place core menu assets in `shenko/assets/`
2. Update `MANIFEST.in` if needed
3. Use asset utilities for path resolution
4. Keep core assets small (<5MB total)
5. Plan for remote download of large assets

### Code Style
- Follow PEP 8
- Use docstrings for all functions
- Comment complex logic
- Keep functions focused and small

---

## Future Roadmap

### Short Term (Next Release)
- [ ] Fix import system for all contexts
- [ ] Replace all deprecated imports
- [ ] Implement asset manifest system
- [ ] Add comprehensive test suite
- [ ] Create CI/CD pipeline

### Medium Term
- [ ] Asset
