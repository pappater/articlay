# 🎉 Articlay v1.1.4 - Zero Configuration Release!

## ✅ Perfect First-Time User Experience

### What Changed
- **Default Gist ID is now HARDCODED** in the library
- Users no longer need ANY configuration
- Works immediately after `pip install articlay`

## Installation & Usage (ZERO CONFIG!)

```bash
# Install
pip install articlay

# Use immediately - NO SETUP REQUIRED!
articlay --all
articlay --india
articlay random
```

## Test Results (Fresh Install, No Config)

✅ **Tested on clean system with:**
- No environment variables set
- No config files
- No command-line arguments
- Just fresh install from PyPI

**Result: WORKS PERFECTLY!** 🎉

```bash
$ pip install articlay
Successfully installed articlay-1.1.4

$ articlay --all --limit 5
📚 Articles (5 total):
[Articles displayed successfully]

$ articlay random
🎲 Fetching a random article...
[Random article displayed successfully]

$ articlay --india --limit 3
📚 Articles in 'India' (3 total):
[India news displayed successfully]
```

## How It Works

The library now has a **default Gist ID embedded**:

```python
DEFAULT_GIST_ID = "17c58ca69bfa6f204a353a76f21b7774"
```

### Priority Order (for advanced users):
1. `--gist-id` command-line argument (highest priority)
2. `ARTICLAY_GIST_ID` environment variable
3. `gist_config.py` file
4. **DEFAULT hardcoded Gist ID** ← NEW! (fallback)

## For End Users

**Just install and use:**
```bash
pip install articlay
articlay --all
```

That's it! No configuration needed.

## For Advanced Users (Optional Overrides)

If you want to use your own Gist:

### Option 1: Command Line
```bash
articlay --gist-id YOUR_GIST_ID --all
```

### Option 2: Environment Variable
```bash
export ARTICLAY_GIST_ID="YOUR_GIST_ID"
articlay --all
```

### Option 3: Config File
Create `gist_config.py`:
```python
GIST_ID = "YOUR_GIST_ID"
```

## Version History

- **v1.1.4** - 🎯 Zero-config release with default Gist ID
- **v1.1.3** - Fixed Gist data parsing
- **v1.1.2** - Added Gist ID configuration options
- **v1.1.1** - Fixed installation issues
- **v1.1.0** - Initial PyPI release

## Links

- **PyPI**: https://pypi.org/project/articlay/1.1.4/
- **GitHub**: https://github.com/pappater/articlay
- **Gist**: https://gist.github.com/pappater/17c58ca69bfa6f204a353a76f21b7774

## Key Features

✅ Zero configuration required  
✅ Works out-of-the-box  
✅ Instant article access after install  
✅ Multiple category filters  
✅ Random article feature  
✅ Clean, formatted output  
✅ 100+ news sources  

## Perfect For

- Quick news browsing from terminal
- Developers who want instant access to curated articles
- Anyone who values simplicity
- First-time Python package users

## Summary

**Before v1.1.4:**
```bash
pip install articlay
export ARTICLAY_GIST_ID="..."  # ← Required!
articlay --all
```

**Now (v1.1.4):**
```bash
pip install articlay
articlay --all  # ← Just works! 🎉
```

---

**Installation**: `pip install articlay`  
**Usage**: `articlay --all`  
**That's it!** 🚀
