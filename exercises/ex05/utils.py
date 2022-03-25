"""EX05 - `list` Utility Functions, implementation of function skeletons."""
__author__ = "730439223"


def only_evens(evens: list[int]) -> list[int]:
    """Returns a list of even or in the edge where empty list will be returned."""
    newlst: list[int] = []
    if len(evens) == 0.0:
        return []
    else:
        for number in evens:
            if ((number % 2) == 0):
                newlst.append(number)
        return newlst


def sub(x: list[int], i_start: int, i_end: int) -> list[int]:
    """Check is it's an empty string if not, evluates and returns the values in the range of the start and end index parameters given the list."""
    y: list[int] = []
    #  i_start = 0
    #  i_end = len(y) - 1
    
    if (len(x) == 0.0) and (i_start > i_end):
        return []
    if i_start < 1:
        i_start = 0
    if len(x) < i_end:
        i_end = len(x) 
  
    while i_start < i_end:
        y.append(x[i_start])
        i_start += 1                    
    return y


def concat(x: list[int], y: list[int]) -> list[int]:
    """Generate a new List which contains all of the elements of the first list followed by all of the elements of the second list."""
    z: list[int] = []

    if len(x) == 0 and len(y) == 1:
        z.append(y[0])
    if len(y) == 0 and len(x) == 1:
        z.append(x[0])
    if len(x) & len(y) == 0.0:
        return []
    for number in x:
        z.append(number)
    for number in y:
        z.append(number)
    return z