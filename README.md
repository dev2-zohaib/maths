# maths

## Current status

This repository now contains a small foundational Python maths module with tests.

## Implemented features

- Basic arithmetic helpers: `add`, `subtract`, `multiply`, and `divide`.
- Utility functions: `factorial`, `mean`, `is_prime`, and `gcd`.
- Pytest-based test coverage for the implemented public API and key error cases.

## Files

- `maths.py` – main implementation module.
- `test_maths.py` – test coverage for the module.
- `requirements-dev.txt` – developer test dependency.

## Run tests

```bash
python -m pip install -r requirements-dev.txt
pytest
```

## Notes

The original task did not specify an exact feature request. Because the repository was an empty placeholder, these additions establish a reasonable, minimal starting point for future maths-related feature development.
