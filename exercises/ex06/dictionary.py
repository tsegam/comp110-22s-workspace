"""EX06 - function skeletons and implementations."""

___author___ = "730439223"


def invert(dictn: dict[str, str]) -> dict[str, str]:
    """Inverts case the jsdg nskjdgnkj n.""" 
    values: list[str] = []
    keys: list[str] = []
    i = 1

    for i in dictn:
        keys.append(i)
        values.append(dictn[i])

    for i in range(len(values)):
        for j in range(i + 1, len(values)):
            if values[i] == values[j]:
                raise KeyError("Dictionary cannot have the same key more than once. Please correct.")

    new_dict = dict[str, str]
    new_dict = {}

    for i in range(len(values)):
        new_dict[values[i]] = keys[i]

    return new_dict


def favorite_color(colors: dict[str, str]) -> str:
    """Inverts case the jsdg nskjdgnkj n.""" 
    values: list[str] = []
    count: list[int] = []

    for i in colors:
        values.append(colors[i])    

    for i in range(len(values)):
        count.append(0)
        for j in range(i + 1, len(values)):
            if values[i] == values[j]:
                count[i] += 1

    return values[count.index(max(count))]


def count(values: list[str]) -> dict[str, int]:
    """Inverts case the jsdg nskjdgnkj n.""" 
    num: list[int] = []

    no_duplicates = []

    for i in values:
        if i not in no_duplicates:
            no_duplicates.append(i)

    for i in no_duplicates:
        num.append(0)

        for j in values:
            if i == j:
                num[no_duplicates.index(i)] += 1

    output: dict[str, int] = {}

    for i in range(len(no_duplicates)):
        output[no_duplicates[i]] = num[i]

    return output