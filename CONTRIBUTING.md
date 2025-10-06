# Contributing to Articlay

Thank you for considering contributing to Articlay! This document provides guidelines and instructions for contributing.

## How to Contribute

### Reporting Issues

- Check if the issue already exists in the issue tracker
- Provide a clear description of the problem
- Include steps to reproduce the issue
- Mention your environment (OS, Python version, etc.)

### Suggesting Enhancements

- Open an issue with a clear description of the enhancement
- Explain why this enhancement would be useful
- Provide examples if possible

### Pull Requests

1. Fork the repository
2. Create a new branch for your feature (`git checkout -b feature/amazing-feature`)
3. Make your changes
4. Run tests to ensure everything works (`python -m unittest test_articlay.py`)
5. Commit your changes (`git commit -m 'Add some amazing feature'`)
6. Push to the branch (`git push origin feature/amazing-feature`)
7. Open a Pull Request

## Development Setup

1. Clone your fork:
```bash
git clone https://github.com/YOUR_USERNAME/articlay.git
cd articlay
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run tests:
```bash
python -m unittest test_articlay.py
```

## Code Style

- Follow PEP 8 guidelines
- Use meaningful variable and function names
- Add docstrings to functions and classes
- Keep functions focused and concise

## Testing

- Add tests for new features
- Ensure all tests pass before submitting PR
- Maintain or improve code coverage

## Areas for Contribution

- Actual Magzter scraping implementation (requires authentication)
- Support for additional content sources
- Improved article selection algorithms
- Better error handling
- Performance optimizations
- Documentation improvements
- Additional output formats (CSV, HTML, etc.)
- Scheduling support (cron job examples)
- Web interface

## Questions?

Feel free to open an issue for any questions about contributing!
