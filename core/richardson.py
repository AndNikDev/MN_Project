"""Richardson extrapolation contracts.

For a base method of order :math:`p`,

.. math::
    R = \\frac{2^{p}\\,A(h/2) - A(h)}{2^{p} - 1}.

With the centered three-point formula (``p = 2``) this collapses to the
familiar form

.. math::
    R = \\tfrac{4}{3}\\,A(h/2) - \\tfrac{1}{3}\\,A(h).

The actual numerical work is delegated to a :class:`DifferentiationMethod`
instance so Richardson stays method-agnostic and trivially reusable when more
schemes (5-point, Romberg) are introduced.
"""

from __future__ import annotations

from dataclasses import dataclass

from core.differentiation import (
    DifferentiationInput,
    DifferentiationMethod,
    DifferentiationResult,
)


@dataclass(frozen=True, slots=True)
class RichardsonResult:
    """Outcome of a Richardson extrapolation step."""

    extrapolated: float
    coarse: DifferentiationResult
    fine: DifferentiationResult
    p: int
    formula_latex: str = ""


class RichardsonExtrapolator:
    """Apply Richardson extrapolation on top of any differentiation method."""

    def __init__(self, base_method: DifferentiationMethod) -> None:
        self._base = base_method

    @property
    def base(self) -> DifferentiationMethod:
        return self._base

    def extrapolate(self, data: DifferentiationInput, p: int | None = None) -> RichardsonResult:
        """Run the base method with steps ``h`` and ``h/2`` and combine them.

        Implementation pending. Will:
            1. Compute ``A(h)``  with ``data.h``.
            2. Compute ``A(h/2)`` with ``data.h / 2``.
            3. Return ``R`` using the formula above.
        """
        raise NotImplementedError(
            "Richardson extrapolation will be implemented in the math iteration."
        )
