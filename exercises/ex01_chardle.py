""" EX01 - Chardle - A cute step toward Wordle."""

___author___ = "730439223"

user_input_word: str = input("Enter a 5-character word: ")
if len(user_input_word) >= 0:
    if len(user_input_word) < 5: 
        print("Error: Word must contain 5 characters")
        exit()
    elif len(user_input_word) > 5:
        print("Error: Word must contain 5 characters")
        exit()
    

user_input_letter: str = input("Enter a single character: ")
if len(user_input_letter) >= 0:
    if len(user_input_letter) < 1: 
        print("Error: Character must be a single character.")
        exit()
    elif len(user_input_letter) > 1:
        print("Error: Character must be a single character.")
        exit()

print("Searching for " + user_input_letter + " in " + user_input_word)
match: int = 0


if user_input_word[0] == user_input_letter:
    print(user_input_letter + " found at index 0")
    match = match + 1
if user_input_word[1] == user_input_letter:
    print(user_input_letter + " found at index 1")
    match = match + 1
if user_input_word[2] == user_input_letter:
    print(user_input_letter + " found at index 2")
    match = match + 1
if user_input_word[3] == user_input_letter:
    print(user_input_letter + " found at index 3")
    match = match + 1
if user_input_word[4] == user_input_letter:
    print(user_input_letter + " found at index 4")
    match = match + 1

if match >= 0:
    if match == 0: 
        print("No instances of " + user_input_letter + " found in " + user_input_word)
    elif match == 1:
        print("1 instance of " + user_input_letter + " found in " + user_input_word)
    elif match > 1:
        print(str(match) + " instances of " + user_input_letter + " found in " + user_input_word)


