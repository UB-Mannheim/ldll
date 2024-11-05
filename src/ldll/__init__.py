"""
ldll - A Python package for ldll
"""

from importlib.metadata import version
from .ldll import main

try:
    __version__ = version("ldll")
except Exception:  # pragma: no cover
    # package is not installed
    __version__ = "unknown"
