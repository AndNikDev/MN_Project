"""Plotly figure builders.

Each function returns a ``plotly.graph_objects.Figure`` so the Streamlit layer
can simply call ``st.plotly_chart(fig, use_container_width=True)`` and stays
free of plotting concerns.
"""

from __future__ import annotations

from typing import Callable, Sequence

import plotly.graph_objects as go


def plot_function_with_tangent(
    func: Callable[[float], float],
    x0: float,
    derivative_value: float,
    *,
    x_range: tuple[float, float] = (-5.0, 5.0),
    samples: int = 400,
) -> go.Figure:
    """Render ``f(x)`` together with its tangent line at ``x0``.

    Implementation pending — will sample ``func`` on ``x_range`` and overlay
    the line ``y = f(x0) + derivative_value * (x - x0)``.
    """
    raise NotImplementedError


def plot_stencil_nodes(
    func: Callable[[float], float],
    nodes: Sequence[float],
    *,
    x_range: tuple[float, float] | None = None,
) -> go.Figure:
    """Highlight the three nodes used by the stencil on top of ``f(x)``.

    Implementation pending.
    """
    raise NotImplementedError


def plot_error_convergence(
    step_sizes: Sequence[float],
    errors: Sequence[float],
    *,
    reference_order: int | None = None,
) -> go.Figure:
    """Log–log plot of error vs. step size, optionally overlaying the
    theoretical slope ``h^p``. Implementation pending.
    """
    raise NotImplementedError
