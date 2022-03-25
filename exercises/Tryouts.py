"""EX06 - function skeletons and implementations."""

___author___ = "730439223"

dictn: dict[str, str] 
dictn = dict({'a': 'z', 'b': 'y', 'c': 'x'})

list = []
i = 1
for key in dictn.keys():
    'creates a list of keys.'
    list.append(key)     

if len(list) == len(set(list)):
    'evaluates for duplicates of keys.'
    raise KeyError("Dictionary cannot have the same key more than once. Please correct.")
     
new_dictn = {
    newV: newK for newK, newV in dictn.items()
}
print(new_dictn)



"""EX06 - function skeletons and implementations."""

___author___ = "730439223"

import pytest 


def invert(dictn: dict[str, str]):
    list = []
    # i = 1
    for key in dictn.keys():
        'creates a list of keys.'
        list.append(key)     
    # for x in list:
    #     'evaluates for duplicates of keys.'
    #     if x == list[i]:
    #         raise KeyError("Dictionary cannot have the same key more than once. Please correct.")
    #     i = i + 1
    if len(list) == len(set(list)):
        'evaluates for duplicates of keys.'
        raise KeyError("Dictionary cannot have the same key more than once. Please correct.")
    else:   
        new_dictn = {
            newV: newK for newK, newV in dictn.items()
        }
        return(new_dictn)
