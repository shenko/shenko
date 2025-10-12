# Contributing to Shenko

Thank you for your interest in contributing to Shenko! This guide will help you get started.

## For Contributors & Developers

### Quick Start

1. **Fork the Repository**
   ```bash
   # Click "Fork" on GitHub, then:
   git clone https://github.com/YOUR_USERNAME/shenko.git
   cd shenko
   ```

2. **Install in Development Mode**
   ```bash
   pip install -e .
   ```
   This installs Shenko in "editable" mode so your changes are immediately reflected.

3. **Test Your Installation**
   ```bash
   python3 shenko/shenko.py
   # Or
   python3 -m shenko.shenko
   ```

### Making Changes

1. **Create a Branch**
   ```bash
   git checkout -b feature/your-feature-name
   ```

2. **Make Your Changes**
   - Edit code in `shenko/` directory
   - Follow existing code style
   - Add comments where helpful

3. **Test Locally**
   ```bash
   # Test direct execution
   python3 shenko/shenko.py
   
   # Test module execution
   python3 -m shenko.shenko
   
   # Run tests (if available)
   pytest
   ```

4. **Commit Your Changes**
   ```bash
   git add .
   git commit -m "Description of your changes"
   ```

5. **Push and Create Pull Request**
   ```bash
   git push origin feature/your-feature-name
   ```
   Then go to GitHub and create a Pull Request.

### Development Guidelines

- **Code Style**: Follow PEP 8 Python style guidelines
- **Documentation**: Update docstrings and comments
- **Testing**: Test all execution methods (script, module, installed)
- **No Version Changes**: Maintainers will handle version bumps

### Project Structure

```
shenko/
├── shenko/              # Main package
│   ├── shenko.py       # Entry point
│   ├── s00_init/       # Menu system (FSM)
│   ├── utils/          # Utility modules
│   └── assets/         # Built-in menu assets
├── setup.py            # Package configuration
├── pyproject.toml      # Modern packaging config
└── tests/              # Test suite
```

### Key Files to Know

- **shenko/shenko.py** - Main application entry point
- **shenko/s00_init/menu.py** - FSM menu system
- **shenko/utils/assets.py** - Asset path resolution
- **PROJECT_CONTEXT.md** - Comprehensive technical documentation

### Common Tasks

**Add a New Menu State:**
1. Edit `shenko/s00_init/menu.py`
2. Add `enterYourState()` and `exitYourState()` methods
3. Test the FSM transitions

**Add Assets:**
- Built-in menu assets go in `shenko/assets/`
- Use `get_asset_path()` from `utils/assets.py` for path resolution
- Keep core assets small (<5MB total)

**Fix Import Issues:**
- We use conditional imports for multi-context support
- See PROJECT_CONTEXT.md section on "Import System"

### Testing Checklist

Before submitting a PR, verify:
- [ ] Code runs via `python3 shenko/shenko.py`
- [ ] Code runs via `python3 -m shenko.shenko`
- [ ] No new warnings or errors
- [ ] Changes don't break existing functionality

### Need Help?

- Read [PROJECT_CONTEXT.md](PROJECT_CONTEXT.md) for technical details
- Check [existing issues](https://github.com/shenko/shenko/issues)
- Ask questions in your Pull Request

### What Maintainers Will Handle

You don't need to worry about:
- Version bumping
- PyPI uploads
- Snap/Flatpak builds
- Release management
- CI/CD configuration

Just focus on making great contributions! 🚀

## Code of Conduct

Be respectful and constructive in all interactions. We're all here to make Shenko better!
