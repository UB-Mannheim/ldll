# ldll

A Python package for ldll.

## Installation

```bash
pip install ldll
```

## Usage

```python
from ldll import example_function

result = example_function("example")
```

## Development

To set up the development environment:

1. Clone the repository
2. Create a virtual environment
3. Install development dependencies:
   ```bash
   pip install -e ".[dev]"
   ```

### Build Package

Update the version in `pyproject.toml` before running the following commands.
```
# Remove relicts from previous builds.
rm -rvf dist
# Build package.
python -m build
# Upload package to test.pypi.org.
python3 -m twine upload --repository testpypi dist/*
```

## Testing

Run tests with pytest:

```bash
pytest
```

## License

MIT License - see LICENSE file for details.
