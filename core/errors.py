"""Error metrics for numerical differentiation and extrapolation.

All functions are pure (no IO, no globals) so they are trivially testable
and cacheable. Vectorised through NumPy where it makes sense.
"""

from __future__ import annotations

from dataclasses import dataclass

import numpy as np


@dataclass(frozen=True, slots=True)
class ErrorReport:
    """Bundle of error metrics for a single approximation."""

    exact: float
    approximation: float
    absolute: float
    relative: float | None
    relative_pct: float | None


def absolute_error(exact: float, approximation: float) -> float:
    """Return :math:`|f'(x) - A|`. Implementation pending."""
    raise NotImplementedError


def relative_error(exact: float, approximation: float, *, eps: float = 1e-15) -> float | None:
    """Return :math:`|f'(x) - A| / |f'(x)|`, or ``None`` if exact ≈ 0.

    The ``eps`` guard prevents division by (near-)zero. Implementation pending.
    """
    raise NotImplementedError


def build_error_report(exact: float, approximation: float) -> ErrorReport:
    """Compose a full :class:`ErrorReport` from the two scalars.

    Implementation pending.
    """
    raise NotImplementedError


def estimate_observed_order(
    errors: np.ndarray, step_sizes: np.ndarray
) -> float:
    """Estimate the empirical order of convergence ``p`` from a sequence of
    ``(h, error)`` pairs by least-squares fit on
    :math:`\\log|E| = \\log C + p\\,\\log h`.

    Implementation pending.
    """
    raise NotImplementedError
