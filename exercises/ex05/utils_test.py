"""Unit tests for list utility functions."""

# TODO: Uncomment the below line when ready to write unit tests
# from exercises.ex05.utils import only_evens, sub, concat

__author__ = "730407005"

from exercises.ex05.utils import only_evens
from exercises.ex05.utils import sub
from exercises.ex05.utils import concat


def test_only_evens_empty() -> None:
    """Tests only_evens with empty list."""
    xs: list[int] = []
    assert only_evens(xs) == []


def test_only_evens_negatives() -> None:
    """Tests only_evens with negative numbers."""
    xs: list[int] = [-1, -2, -8, -11, -6]
    assert only_evens(xs) == [-2, -8, -6]


def test_only_evens_all() -> None:
    """Tests only_evens with a mix of positives, negatives, and 0."""
    xs: list[int] = [0, 5, 6, -3, 8, -4, -4, 9]
    assert only_evens(xs) == [0, 6, 8, -4, -4]


def test_sub_same_bound() -> None:
    """Tests sub with equal upper and lower bounds."""
    xs: list[int] = [4, 6, 9, 1, 9, 2, 0, 12]
    lower: int = 4
    upper: int = 4
    assert sub(xs, lower, upper) == []


def test_sub_negatives() -> None:
    """Tests sub with negative numbers."""
    xs: list[int] = [-10, -2, -3, -2, -5, -6]
    lower: int = 2
    upper: int = 4
    assert sub(xs, lower, upper) == [-3, -2]


def test_sub_all() -> None:
    """Tests sub with mix of positives, negatives, and 0."""
    xs: list[int] = [-10, 2, -3, 0, 0, 5, -6]
    lower: int = 2
    upper: int = 4
    assert sub(xs, lower, upper) == [-3, 0]


def test_concat_both_empty() -> None:
    """Tests concat with 2 empty lists."""
    xs: list[int] = []
    ys: list[int] = []
    assert concat(xs, ys) == []


def test_concat_1_empty() -> None:
    """Tests concat with 1 empty list and 1 full list."""
    xs: list[int] = [4, 3, 9, 2]
    ys: list[int] = []
    assert concat(xs, ys) == [4, 3, 9, 2]


def test_concat_both_full() -> None:
    """Tests concat with 2 full lists."""
    xs: list[int] = [9, 2, 0, 5]
    ys: list[int] = [0, 7, 8, 1]
    assert concat(xs, ys) == [9, 2, 0, 5, 0, 7, 8, 1]