"""Smoke tests — verify the package layout imports cleanly.

These tests do *not* exercise the (still unimplemented) numerical methods.
They simply guarantee that adding new modules will not break the import graph.
"""

from __future__ import annotations


def test_core_imports() -> None:
    from core import differentiation, errors, parser, richardson, visualization  # noqa: F401


def test_ui_imports() -> None:
    from ui import latex_renderer, sidebar, tables  # noqa: F401


def test_stencil_enum_values() -> None:
    from core.differentiation import Stencil

    assert {s.value for s in Stencil} == {"forward", "centered", "backward"}


def test_latex_formulas_exist() -> None:
    from core.differentiation import Stencil
    from ui.latex_renderer import formula_for, richardson_formula

    for stencil in Stencil:
        assert formula_for(stencil)
    assert richardson_formula(p=2)
    assert richardson_formula(p=4)
