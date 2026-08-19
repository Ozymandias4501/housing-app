"""Smoke test: the package is installed and importable."""

import housing


def test_package_has_version():
    assert housing.__version__ == "0.1.0"
