"""Examples of using lists in a 'game'."""


from random import randint

rolls: list[int] = list()

while len(rolls) == 0 or (rolls[len(rolls) - 1] != 1):
    rolls.append(randint(1, 6))
print(rolls)

# Remove an item from list by its ("pop")
rolls.pop(len(rolls) - 1)
print(rolls)

# Sum the values of our rolls!

i: int = 0
sum: int = 0
while (i < len(rolls)):
    sum = sum + rolls[i]
    i = i + 1 
print(f"Total score: { sum }")

# rolls.append(randint(1, 6))
# rolls.append(randint(1, 6))
# rolls.append(randint(1, 6))
# print(rolls)
 
# # Access an individual item
# print(rolls[0])
# print(rolls[1])
# print(rolls[2])

# # Accesss the length of a list (number of item)
# last_index: int = len(rolls) - 1
# print(last_index)