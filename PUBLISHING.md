# Publishing Articlay to PyPI

This guide explains how to publish Articlay to the Python Package Index (PyPI).

## Prerequisites

1. **PyPI Account**: Create an account at [pypi.org](https://pypi.org/account/register/)
2. **PyPI API Token**: Generate an API token from your PyPI account settings
3. **Build Tools**: Install required packages:
   ```bash
   pip install build twine
   ```

## Publishing Steps

### 1. Prepare for Release

Update version in `setup.py`:
```python
version="1.1.0"  # Update to new version
```

Update `CHANGELOG.md` with changes for this release.

### 2. Build the Distribution

Clean any previous builds:
```bash
rm -rf build/ dist/ *.egg-info
```

Build source and wheel distributions:
```bash
python -m build
```

This creates:
- `dist/articlay-1.1.0.tar.gz` (source distribution)
- `dist/articlay-1.1.0-py3-none-any.whl` (wheel distribution)

### 3. Test with TestPyPI (Optional but Recommended)

First, upload to TestPyPI to verify everything works:

```bash
python -m twine upload --repository testpypi dist/*
```

Then test installation:
```bash
pip install --index-url https://test.pypi.org/simple/ articlay
```

### 4. Upload to PyPI

Upload to the production PyPI:
```bash
python -m twine upload dist/*
```

You'll be prompted for:
- Username: `__token__`
- Password: Your PyPI API token (starts with `pypi-`)

### 5. Verify Installation

Test that users can install from PyPI:
```bash
pip install articlay
articlay --help
```

## Automated Publishing with GitHub Actions

You can automate PyPI publishing using GitHub Actions. Create `.github/workflows/publish.yml`:

```yaml
name: Publish to PyPI

on:
  release:
    types: [published]

jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
    - uses: actions/checkout@v3
    
    - name: Set up Python
      uses: actions/setup-python@v4
      with:
        python-version: '3.x'
    
    - name: Install dependencies
      run: |
        python -m pip install --upgrade pip
        pip install build twine
    
    - name: Build package
      run: python -m build
    
    - name: Publish to PyPI
      env:
        TWINE_USERNAME: __token__
        TWINE_PASSWORD: ${{ secrets.PYPI_API_TOKEN }}
      run: python -m twine upload dist/*
```

Add your PyPI API token as a GitHub secret named `PYPI_API_TOKEN`.

## Version Numbering

Follow [Semantic Versioning](https://semver.org/):
- **MAJOR** version (1.x.x): Incompatible API changes
- **MINOR** version (x.1.x): New functionality, backward compatible
- **PATCH** version (x.x.1): Bug fixes, backward compatible

## Release Checklist

Before publishing:

- [ ] Update version in `setup.py`
- [ ] Update `CHANGELOG.md` with release notes
- [ ] Run all tests: `python -m unittest test_articlay.py`
- [ ] Test CLI locally: `pip install -e .` and `articlay --help`
- [ ] Build distributions: `python -m build`
- [ ] Check package with `twine check dist/*`
- [ ] Upload to TestPyPI (optional)
- [ ] Upload to PyPI: `twine upload dist/*`
- [ ] Create GitHub release with tag (e.g., `v1.1.0`)
- [ ] Test installation from PyPI
- [ ] Update documentation if needed

## Package Metadata

The package metadata is defined in `setup.py`:

```python
setup(
    name="articlay",
    version="1.1.0",
    author="Articlay Contributors",
    description="A CLI tool to aggregate and view curated news articles from 100+ sources",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/pappater/articlay",
    py_modules=["articlay"],
    classifiers=[...],
    python_requires=">=3.7",
    install_requires=[...],
    entry_points={
        "console_scripts": [
            "articlay=articlay:main",
        ],
    },
)
```

## Post-Publication

After publishing:

1. **Announce the release**:
   - Create a GitHub release
   - Update README badges if needed
   - Share on social media

2. **Monitor for issues**:
   - Watch for installation problems
   - Check issue tracker
   - Monitor download statistics

3. **Documentation**:
   - Ensure README is up-to-date on PyPI
   - Update live documentation site

## Troubleshooting

### "Invalid distribution file"
- Ensure `setup.py` is properly configured
- Check that `README.md` and `requirements.txt` exist
- Run `twine check dist/*` to validate

### "Package already exists"
- Can't republish same version
- Increment version number in `setup.py`
- Rebuild: `rm -rf dist/ && python -m build`

### "Authentication failed"
- Verify API token is correct
- Use `__token__` as username
- Token should start with `pypi-`

### "README not displaying on PyPI"
- Check `long_description_content_type="text/markdown"`
- Ensure README.md is valid Markdown
- Use `python -m build` (not `python setup.py sdist`)

## Resources

- [PyPI Documentation](https://packaging.python.org/tutorials/packaging-projects/)
- [Twine Documentation](https://twine.readthedocs.io/)
- [Python Packaging User Guide](https://packaging.python.org/)
- [Semantic Versioning](https://semver.org/)

## Note

**Important**: This is a Python package, not an npm package. Despite the original issue mentioning "npm registry", Articlay is designed for Python/PyPI distribution.
