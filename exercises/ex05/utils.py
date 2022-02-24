"""EX05 - `list` Utility Functions, implementation of function skeletons."""
__author__ = "730439223"


def only_evens(x: list[int]) -> list:
    """Returns a list of even or in the edge where empty list will be returned"""
    y: list = []
    if len(x) == 0.0:
        return []
    else:
        for number in x:
            if ((number % 2) == 0):
                y.append(number)
        return y


def sub(x: list[int], i_start: int, i_end: int) -> list:
    """Check is it's an empty string if not, evluates and returns the values in the range of the start and end index parameters given the list."""
    y: list = []
    i_start = 0
    i_end = len(y) - 1
    
    if len(y) == 0.0:
        return []
    else:
        while i_start < i_end:
            y.append(x[i_start])
            i_start += 1         
        return y


def concat(x: list[int], y: list[int]) -> list:
    """Generate a new List which contains all of the elements of the first list followed by all of the elements of the second list."""
    z: list = []
    if len(x) & len(y) == 0.0:
        return []
    for number in x:
        z.append(number)
    for number in y:
        z.append(number)
    return z