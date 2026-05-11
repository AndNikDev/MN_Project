"""Three-point numerical differentiation contracts.

This module defines the *interface* (Protocol + dataclasses) for any
finite-difference scheme. The actual three-point formulas — forward, centered
and backward — will be implemented later, plugged into the same protocol so
the UI code never has to know which stencil it is dealing with.

Why a Protocol?
    The course will likely grow to include 5-point and Romberg schemes.
    Programming against a contract keeps the UI and the orchestration code
    untouched when new methods are added (Open/Closed Principle).
"""

from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum
from typing import Callable, Protocol, runtime_checkable


class Stencil(str, Enum):
    """Three-point stencil variants from Burden & Faires (2011)."""

    FORWARD = "forward"
    CENTERED = "centered"
    BACKWARD = "backward"


@dataclass(frozen=True, slots=True)
class DifferentiationInput:
    """All the data a differentiation method needs to run.

    Attributes
    ----------
    func:
        Callable representing :math:`f(x)`.
    x0:
        Point at which the derivative is approximated.
    h:
        Step size between consecutive nodes.
    stencil:
        Which of the three-point variants to use.
    """

    func: Callable[[float], float]
    x0: float
    h: float
    stencil: Stencil = Stencil.CENTERED


@dataclass(frozen=True, slots=True)
class DifferentiationResult:
    """Outcome of a single differentiation evaluation."""

    approximation: float
    stencil: Stencil
    h: float
    nodes: tuple[float, ...] = field(default_factory=tuple)
    function_values: tuple[float, ...] = field(default_factory=tuple)
    formula_latex: str = ""


@runtime_checkable
class DifferentiationMethod(Protocol):
    """Any object able to approximate a first derivative."""

    name: str
    order: int

    def compute(self, data: DifferentiationInput) -> DifferentiationResult: ...


class ThreePointMethod:
    """Three-point finite-difference scheme (order 2).

    Selects the appropriate stencil at runtime. Implementation pending —
    see ``compute`` below.
    """

    name: str = "Three-point formula"
    order: int = 2

    def compute(self, data: DifferentiationInput) -> DifferentiationResult:
        """Apply the requested stencil. Implementation pending."""
        raise NotImplementedError(
            "Three-point computation will be added in the next iteration."
        )
