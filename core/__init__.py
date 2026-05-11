"""Pure logic layer.

This package contains the mathematical core (parsing, differentiation,
extrapolation, error analysis and figure generation). It must remain free of
Streamlit imports so it can be reused from notebooks, scripts and tests.
"""

from __future__ import annotations

__all__ = [
    "parser",
    "differentiation",
    "richardson",
    "errors",
    "visualization",
]
