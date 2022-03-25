"""Unit tests for EX06."""
___author___ = "730439223"


from exercises.ex06.dictionary import invert, favorite_color, count
import pytest


def test_invert_1() -> None:
    """Edge case to test whether duplicate key exists."""
    assert invert({'a': 'z', 'b': 'y', 'c': 'x'}) == {'z': 'a', 'y': 'b', 'x': 'c'}


def test_invert_2() -> None:
    """Edge case to test whether duplicate key exists."""
    assert invert({'sd': 'aw', 'fd': 'zs', 'iu': 'ys'}) == {'aw': 'sd', 'zs': 'fd', 'ys': 'iu'}


def test_invert_keyerror() -> None:
    """Edge case to test whether duplicate key exists."""
    with pytest.raises(KeyError):
        my_dictionary = {'kris': 'jordan', 'michael': 'jordan'}
        invert(my_dictionary)


def test_favorite_color_1() -> None:
    """Use case to test whether duplicate key exists."""
    assert favorite_color({"Marc": "yellow", "Ezri": "blue", "Kris": "blue"}) == 'blue'


def test_favorite_color_2() -> None:
    """Use case to test whether duplicate key exists."""
    assert favorite_color({"Merc": "yellow", "Bsdff": "yellow", "Tsega": "blue"}) == 'yellow'


def test_favorite_color_3() -> None:
    """Edge case to test whether duplicate key exists."""
    assert favorite_color({"Kids": "black", "Aman": "black", "Natan": "blue"}) == 'black'


def test_count_1() -> None:
    """Use case to test whether duplicate key exists."""
    assert count(["s", "b", "d", "d"]) == {"s": 1, "b": 1, "d": 2}


def test_count_2() -> None:
    """Use case to test whether duplicate key exists."""
    assert count(["c", "b", "e", "e"]) == {"c": 1, "b": 1, "e": 2}


def test_count_3() -> None:
    """Use case to test whether duplicate key exists."""
    assert count(["j", "a", "d", "d"]) == {"j": 1, "a": 1, "d": 2}