"""Tests for nonnegative and doubly nonnegative matrix check function."""

import numpy as np
import pytest

from toqito.matrix_props import is_nonnegative


@pytest.mark.parametrize(
    "mat, mat_type, expected",
    [
        # Identity matrix: nonnegative and doubly nonnegative
        (np.eye(3), "nonnegative", True),
        (np.eye(3), "doubly", True),
        (np.eye(3), "nonnegative", True),  # default case

        # Matrix with a negative entry: not nonnegative or doubly
        (np.array([[1, -1], [0, 1]]), "nonnegative", False),
        (np.array([[1, -1], [0, 1]]), "doubly", False),

        # Entrywise nonnegative but not PSD: fails "doubly"
        (np.array([[0, 10], [10, 0]]), "nonnegative", True),
        (np.array([[0, 10], [10, 0]]), "doubly", False),
    ]
)
def test_is_nonnegative(mat, mat_type, expected):
    """Parameterized tests for nonnegative and doubly nonnegative matrix cases."""
    assert is_nonnegative(mat, mat_type) is expected


@pytest.mark.parametrize("bad_type", ["l", "r", 1, (), "d"])
def test_invalid_type_raises(bad_type):
    """Check that invalid matrix types raise a TypeError."""
    with pytest.raises(TypeError):
        is_nonnegative(np.identity(3), bad_type)
