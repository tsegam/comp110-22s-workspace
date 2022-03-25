"""Example of looping through all characters in a string."""

# user_string: str = input("Give me a string!")

# The variable i is a common counter variable name in programming. i is short for interator.
# i: int = 1

dict1: dict[int, str]
dict1 = dict()

dict1[2] = "b" 
dict1[3] = "a" 
dict1[4] = "c"

values: list[str] = []
keys: list[int] = []

print(dict1)
for i in dict1:
    keys.append(i)
    values.append(dict1[i])

for i in range(len(values)):
    for j in range(i + 1, len(values)):
        if values[i] == values[j]:
            raise KeyError("Dictionary cannot have the same key more than once. Please correct.")

new_dict = dict[str, int]
new_dict = {}

for i in range(len(values)):
    new_dict[values[i]] = keys[i]

return new_dict
# print(letters[2])
# print("Done!")