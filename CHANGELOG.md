# Changelog

All notable changes to this project are documented here.

## 1.1.0

- Update supported range to Python 3.8+, Django 4.2 / 5.x / 6.0, and Cheroot 10+.
- Drop the legacy `django>=2.2.24` and Python `>=3.5` floors.
- Migrate packaging from `setup.py` to `pyproject.toml` (PEP 621).
- Fix command argument defaults so they match the documented values (`--minthreads` now defaults to 30, not 20) and apply via `argparse` defaults.
- Refactor the management command around a testable `build_cheroot_server()` helper and add a pytest suite.
- Convert the PyPI publish workflow to OIDC trusted publishing (no API token).
- Point the README "Documentation" link at https://modbender.in/django-cheroot/.

## 1.0.2

- Fixes to command discovery and default arguments.

## 1.0.0

- Initial release: `cheroot` management command to serve Django via the Cheroot WSGI server.
