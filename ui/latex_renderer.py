"""LaTeX rendering helpers.

Centralises every formula string used in the app so the templates live in
one place and can be reused from any tab. Streamlit renders them via
``st.latex(...)`` — these functions just *return* the string, the caller
decides where to display it.
"""

from __future__ import annotations

from core.differentiation import Stencil


THREE_POINT_FORMULAS: dict[Stencil, str] = {
    Stencil.FORWARD: r"f'(x) \approx \frac{-3\,f(x) + 4\,f(x+h) - f(x+2h)}{2h}",
    Stencil.CENTERED: r"f'(x) \approx \frac{f(x+h) - f(x-h)}{2h}",
    Stencil.BACKWARD: r"f'(x) \approx \frac{3\,f(x) - 4\,f(x-h) + f(x-2h)}{2h}",
}

RICHARDSON_GENERAL = (
    r"R = \frac{2^{p}\,A(h/2) - A(h)}{2^{p} - 1}"
)

RICHARDSON_ORDER_2 = (
    r"R = \tfrac{4}{3}\,A(h/2) - \tfrac{1}{3}\,A(h)"
)


def formula_for(stencil: Stencil) -> str:
    """Return the LaTeX string for the requested three-point variant."""
    return THREE_POINT_FORMULAS[stencil]


def richardson_formula(p: int = 2) -> str:
    """Return the Richardson formula. Uses the simplified form when ``p == 2``."""
    return RICHARDSON_ORDER_2 if p == 2 else RICHARDSON_GENERAL
