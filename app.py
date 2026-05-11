"""Streamlit entry point.

Run with:
    streamlit run app.py

Responsibilities:
    * Page configuration & global layout.
    * Wire the sidebar (input) with the core layer (logic) and the rendering
      helpers (output).
    * Hold cross-page session state.

This file stays *thin* on purpose — all the math lives in ``core/`` and all
the widgets live in ``ui/``.
"""

from __future__ import annotations

import streamlit as st

from ui.latex_renderer import formula_for, richardson_formula
from ui.sidebar import SidebarConfig, render_sidebar


PAGE_TITLE = "Tres Puntos & Richardson"
PAGE_ICON = "∂"


def configure_page() -> None:
    """Apply the global ``st.set_page_config`` once per session."""
    st.set_page_config(
        page_title=PAGE_TITLE,
        page_icon=PAGE_ICON,
        layout="wide",
        initial_sidebar_state="expanded",
        menu_items={
            "About": (
                "Aplicación didáctica para el curso MA-0322 Métodos Numéricos. "
                "Diferenciación por fórmula de tres puntos y extrapolación de Richardson."
            ),
        },
    )


def render_header() -> None:
    """Top banner with title and short description."""
    st.title("Diferenciación numérica · Fórmula de tres puntos & Richardson")
    st.markdown(
        "Aplicación interactiva para el curso **MA-0322 Métodos Numéricos** "
        "(Universidad de Costa Rica). Calcula derivadas aproximadas con la "
        "fórmula de tres puntos y mejora la precisión mediante extrapolación de "
        "Richardson."
    )
    st.divider()


def render_theory_tab(config: SidebarConfig) -> None:
    """Static theory panel — useful for the in-class presentation."""
    st.subheader("Fundamento teórico")
    st.markdown(
        "**Fórmula seleccionada (estencil _{}_):**".format(config.stencil.value)
    )
    st.latex(formula_for(config.stencil))

    if config.use_richardson:
        st.markdown("**Extrapolación de Richardson (orden p = 2):**")
        st.latex(richardson_formula(p=2))


def render_results_tab(config: SidebarConfig) -> None:
    """Numerical results — currently a placeholder."""
    st.subheader("Resultados numéricos")
    st.info(
        "Los métodos numéricos se implementarán en la siguiente iteración. "
        "Esta vista está reservada para la tabla de iteraciones, el valor "
        "aproximado y los reportes de error."
    )

    cols = st.columns(3)
    cols[0].metric("f(x)", config.expression or "—")
    cols[1].metric("x₀", f"{config.x0:.4f}")
    cols[2].metric("h", f"{config.h:.6f}")


def render_plot_tab(config: SidebarConfig) -> None:
    """Visualisation panel — currently a placeholder."""
    st.subheader("Visualización")
    if not config.show_plot:
        st.caption("Habilita 'Mostrar gráfica' en la barra lateral para ver el plot.")
        return
    st.info("Las gráficas Plotly se renderizarán aquí cuando los métodos estén listos.")


def main() -> None:
    """Application bootstrap."""
    configure_page()
    render_header()

    config = render_sidebar()

    tab_theory, tab_results, tab_plot = st.tabs(
        ["Teoría", "Resultados", "Visualización"]
    )
    with tab_theory:
        render_theory_tab(config)
    with tab_results:
        render_results_tab(config)
    with tab_plot:
        render_plot_tab(config)


if __name__ == "__main__":
    main()
