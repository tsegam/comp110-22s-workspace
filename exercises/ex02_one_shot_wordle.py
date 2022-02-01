"""EX02 - One Shot Wordle."""
___author___ = "730439223"

secret: str = "pere"
answer: str = input(f"What is your {len(secret)}-letter guess? ")
i: int = 0
result: str = ""

alt_i: int = 0

WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"

while (len(secret) > len(answer)):
    answer = input(f"That was not {len(secret)} letters! Try again: ")
while (len(secret) < len(answer)):
    answer = input(f"That was not {len(secret)} letters! Try again: ")

while (i < len(secret)):
    if (secret[i] == answer[i]):
        result = result + GREEN_BOX
    else:
        exists: bool = False
        while (exists and i < len(secret)):
            if (secret[alt_i] == answer[i]): 
                exists = True
            else:               
                alt_i = alt_i + 1                              
        if (exists):
            result = result + YELLOW_BOX
        else:
            result = result + WHITE_BOX
    i = i + 1
print(result)

if str(secret) == str(answer):
    print("Woo! You got it!")
else:
    print("Not quite. Play again soon!")
