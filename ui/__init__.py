"""Presentation layer.

Streamlit-only widgets, tables, and LaTeX renderers. Anything that touches
``st.*`` belongs here so the ``core`` package stays UI-agnostic.
"""

from __future__ import annotations

__all__ = ["sidebar", "tables", "latex_renderer"]
