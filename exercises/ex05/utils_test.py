"""Tests for EX05 - utils assignment."""
__author__ = "730439223"

from exercises.ex05.utils import only_evens, sub, concat


def test_only_evens_empty() -> None:
    """Edge case to test whether or not empty list is accepted."""
    assert only_evens([]) == []

 
def test_utiltest_only_evens_one() -> None:
    """Use case to test whether functil will return a list of number 2."""
    xs: list[int] = [1, 2, 3]
    assert only_evens(xs) == [2]


def test_utiltest_only_evens_two() -> None:
    """Use case to test whether functil will return a list of number 4s."""
    xs: list[int] = [4, 4, 4]
    assert only_evens(xs) == [4, 4, 4]


def test_utiltest_sub_empty() -> None:
    """Edge case to test whether or not empty list is accepted."""
    assert only_evens([]) == []


def test_utiltest_sub_one() -> None:
    """Edge case to test whether or not first usecase is accepted."""
    a_list = [10, 20, 30, 40]
    assert sub(a_list, 1, 3) == [20, 30]


def test_utiltest_sub_two() -> None:
    """Edge case to test whether or not second usecase is accepted."""
    a_list = [0, 10, 30, 40, 50]
    assert sub(a_list, 1, 4) == [10, 30, 40]


def test_concat_empty() -> None:
    """Edge case to test whether or not empty list is accepted."""
    assert concat([], []) == []


def test_concat_empty_just_one() -> None:
    """Edge case 2, given a list witn one valye and list empty."""
    xs: list[int] = []
    xt: list[int] = [1]
    assert concat(xs, xt) == [1]


def test_concat_one() -> None:
    """Use case 1, given a list concatenate all elements with second list."""
    xs: list[int] = [1, 2]
    xt: list[int] = [3]
    assert concat(xs, xt) == [1, 2, 3]


def test_concat_two() -> None:
    """Use case 2, given a list concatenate all elements with second list."""
    xs: list[int] = [1, 4]
    xt: list[int] = [2]
    assert concat(xs, xt) == [1, 4, 2]