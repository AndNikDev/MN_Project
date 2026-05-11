"""Pandas table builders for the iteration / results panel.

These helpers transform domain objects (DifferentiationResult, RichardsonResult)
into nicely formatted DataFrames that Streamlit can render with ``st.dataframe``.
"""

from __future__ import annotations

from typing import Iterable

import pandas as pd

from core.differentiation import DifferentiationResult
from core.richardson import RichardsonResult


def build_iteration_table(results: Iterable[DifferentiationResult]) -> pd.DataFrame:
    """Tabulate one row per differentiation evaluation.

    Columns: ``Iteration``, ``Stencil``, ``h``, ``Nodes``, ``f(nodes)``,
    ``Approximation``. Implementation pending.
    """
    raise NotImplementedError


def build_richardson_table(result: RichardsonResult) -> pd.DataFrame:
    """Two-row table comparing ``A(h)``, ``A(h/2)`` and the extrapolated ``R``.

    Implementation pending.
    """
    raise NotImplementedError


def style_results(df: pd.DataFrame) -> pd.io.formats.style.Styler:
    """Apply numeric formatting & subtle highlighting. Implementation pending."""
    raise NotImplementedError
