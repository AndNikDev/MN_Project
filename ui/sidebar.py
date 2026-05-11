"""Streamlit sidebar — input widgets & global configuration.

Returns a typed :class:`SidebarConfig` so the rest of the app consumes a
single, immutable, well-typed object instead of scattered ``st.session_state``
keys.
"""

from __future__ import annotations

from dataclasses import dataclass

import streamlit as st

from core.differentiation import Stencil


@dataclass(frozen=True, slots=True)
class SidebarConfig:
    """Snapshot of every user-controllable parameter."""

    expression: str
    x0: float
    h: float
    stencil: Stencil
    use_richardson: bool
    show_table: bool
    show_plot: bool


def render_sidebar() -> SidebarConfig:
    """Draw the sidebar widgets and return the user's selection.

    Defaults are tuned for a clean first-launch demo.
    """
    st.sidebar.title("Configuración")
    st.sidebar.caption("Parámetros del método numérico")

    expression = st.sidebar.text_input(
        "f(x)",
        value="sin(x)",
        help="Expresión simbólica en notación SymPy. Ej: x**2 + sin(x), exp(-x**2).",
    )

    x0 = st.sidebar.number_input(
        "Punto x₀",
        value=1.0,
        step=0.1,
        format="%.4f",
        help="Punto donde se aproxima la derivada.",
    )

    h = st.sidebar.number_input(
        "Paso h",
        value=0.1,
        min_value=1e-8,
        max_value=10.0,
        step=0.01,
        format="%.6f",
        help="Distancia entre nodos consecutivos.",
    )

    stencil_label = st.sidebar.radio(
        "Estencil",
        options=[s.value for s in Stencil],
        index=1,  # centered by default — most accurate
        format_func=lambda v: {
            "forward": "Adelante",
            "centered": "Centrado",
            "backward": "Atrás",
        }[v],
    )
    stencil = Stencil(stencil_label)

    st.sidebar.divider()

    use_richardson = st.sidebar.toggle(
        "Aplicar extrapolación de Richardson",
        value=True,
        help="Combina A(h) y A(h/2) para reducir el error de truncamiento.",
    )

    st.sidebar.divider()
    st.sidebar.subheader("Visualización")
    show_table = st.sidebar.checkbox("Mostrar tabla de iteraciones", value=True)
    show_plot = st.sidebar.checkbox("Mostrar gráfica", value=True)

    return SidebarConfig(
        expression=expression.strip(),
        x0=float(x0),
        h=float(h),
        stencil=stencil,
        use_richardson=use_richardson,
        show_table=show_table,
        show_plot=show_plot,
    )
