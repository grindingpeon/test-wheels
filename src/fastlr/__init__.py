from typing import Literal
from numpy import float64, asfortranarray
from numpy.typing import NDArray

from ._fastlr import irls as irls_cpp
from fastlr.logreg import irls as estimate_simple
from fastlr.logreg import generate_data, IRLSResult


def estimate_cpp(
    X: NDArray[float64],
    y: NDArray[float64],
    tol: float = 1e-8,
    max_iter: int = 1000,
):
    """Estimates logistic regression using cpp IRLS implementation."""
    # armadillo assumes column-major order (fortran)
    if not X.flags["F_CONTIGUOUS"]:
        X = asfortranarray(X)
    if not y.flags["F_CONTIGUOUS"]:
        y = asfortranarray(y)
    return IRLSResult(**irls_cpp(X, y, tol, max_iter))


def fastlr(
    X: NDArray[float64],
    y: NDArray[float64],
    tol: float = 1e-8,
    max_iter: int = 1000,
    method: Literal["cpp", "python"] = "cpp",
) -> IRLSResult:
    """Estimate logistic regression"""
    match method:
        case "cpp":
            return estimate_cpp(X, y, tol=tol, max_iter=max_iter)
        case "python":
            return estimate_simple(X, y, tol=tol, max_iter=max_iter)
        case _:
            raise ValueError(f"Unknown method: {method}. Use 'cpp' or 'python'.")


__all__ = [
    "estimate_simple",
    "estimate_cpp",
    "fastlr",
    "generate_data",
]
