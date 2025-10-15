# PyPI Publishing Guide for Articlay

## 🎉 Published Successfully!

Your package **articlay** is now live on PyPI!

- **Package URL**: https://pypi.org/project/articlay/
- **Latest Version**: 1.1.1
- **Installation**: `pip install articlay`

---

## What Was Fixed

### Version 1.1.0 (Initial - Had Issues)
- ❌ Missing `requirements.txt` in source distribution
- ❌ Wheel build failed during installation

### Version 1.1.1 (Fixed - Working)
- ✅ Created `MANIFEST.in` to include all necessary files
- ✅ Moved dependencies directly into `setup.py` instead of reading from file
- ✅ Both source distribution (`.tar.gz`) and wheel (`.whl`) build successfully
- ✅ Installation works perfectly

---

## Files Created/Modified

### 1. `MANIFEST.in` (NEW)
```
include README.md
include LICENSE
include requirements.txt
include CHANGELOG.md
include CLI_GUIDE.md
include FEATURES.md
include SETUP_GUIDE.md
recursive-include scrapers *.py
```

### 2. `setup.py` (MODIFIED)
- Changed from reading `requirements.txt` to hardcoded dependencies
- Bumped version to 1.1.1
- Dependencies now defined directly in setup.py:
  - requests>=2.31.0
  - beautifulsoup4>=4.12.0
  - lxml>=4.9.0

---

## Publishing Workflow (For Future Updates)

### 1. Update Version Number
Edit `setup.py` and increment the version:
```python
version="1.1.2",  # Change this
```

### 2. Update CHANGELOG
Add what's new in `CHANGELOG.md`

### 3. Clean Previous Builds
```bash
rm -rf dist/ build/ *.egg-info
```

### 4. Build Package
```bash
python -m build
```

### 5. Check Package Quality
```bash
twine check dist/*
```

### 6. Test on TestPyPI (Optional but Recommended)
```bash
twine upload --repository testpypi dist/*
pip install --index-url https://test.pypi.org/simple/ articlay
```

### 7. Upload to Production PyPI
```bash
twine upload dist/*
```

### 8. Verify Installation
```bash
pip install --no-cache-dir --upgrade articlay
articlay --help
```

---

## Your PyPI Credentials Setup

You should have a `~/.pypirc` file with:

```ini
[pypi]
username = __token__
password = pypi-YOUR-ACTUAL-TOKEN-HERE

[testpypi]
username = __token__
password = pypi-YOUR-TEST-TOKEN-HERE
```

**Security**: Make sure permissions are set correctly:
```bash
chmod 600 ~/.pypirc
```

---

## Quick Reference Commands

```bash
# Install build tools
pip install --upgrade build twine

# Full publishing workflow
rm -rf dist/ build/ *.egg-info
python -m build
twine check dist/*
twine upload dist/*

# Install from PyPI
pip install articlay

# Upgrade to latest version
pip install --upgrade articlay
```

---

## Important Notes

### Version Numbers
- Follow [Semantic Versioning](https://semver.org/): MAJOR.MINOR.PATCH
- Example: `1.1.1` → `1.1.2` (patch), `1.2.0` (minor), `2.0.0` (major)
- **Cannot reuse version numbers** - once published, it's permanent

### Package Name
- Your package name `articlay` is now reserved under your account
- Others cannot use this exact name

### Documentation
- Your README.md appears on the PyPI page
- Keep it updated with installation instructions and examples

### License
- You're using MIT License (good choice!)
- Make sure LICENSE file is always included

---

## Verification

Test that everything works:

```bash
# In a fresh environment
pip install articlay

# Test the CLI
articlay --help
articlay --foryou
articlay random

# Verify version
pip show articlay
```

---

## What Users See

When someone visits https://pypi.org/project/articlay/, they see:
- Your README.md as the description
- Installation command: `pip install articlay`
- Project links (GitHub, etc.)
- Version history
- Dependencies
- License information

---

## Troubleshooting

### If build fails:
```bash
# Clean everything
rm -rf dist/ build/ *.egg-info articlay.egg-info/

# Rebuild
python -m build
```

### If upload fails:
```bash
# Check credentials in ~/.pypirc
cat ~/.pypirc

# Verify token is correct
# Get new token from: https://pypi.org/manage/account/token/
```

### If installation fails:
```bash
# Clear pip cache
pip cache purge

# Install without cache
pip install --no-cache-dir articlay
```

---

## Next Steps

1. ✅ Test installation on different systems
2. ✅ Update GitHub README with PyPI badge
3. ✅ Share your package with others!
4. Consider adding more documentation
5. Set up automated testing (GitHub Actions)
6. Consider adding a GitHub Action for automated PyPI releases

---

## PyPI Badge for README

Add this to your GitHub README.md:

```markdown
[![PyPI version](https://badge.fury.io/py/articlay.svg)](https://badge.fury.io/py/articlay)
[![Downloads](https://pepy.tech/badge/articlay)](https://pepy.tech/project/articlay)
```

---

## Congratulations! 🎊

You've successfully published your first Python package to PyPI!

Anyone in the world can now install articlay with:
```bash
pip install articlay
```

Keep updating and improving your package. Happy coding! 🚀
