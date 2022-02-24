"""EX03 - Structured Wordle."""
__author__ = "730439223"


def contains_char(word1: str, char1: str) -> bool:   
    """Check if it contains char."""
    assert len(char1) == 1
    i: int = 0
    check: bool = False
    while (i < len(word1)):   # iterates through each character of input
        if (str(word1[i]) == str(char1)):   # evaluates if character exists in word
            i = i + 1   # increment counter
            return True                 
        else:
            check = False
            i = i + 1       
    return check


def emojified(answer: str, secret: str) -> str:
    """Returns a string of emojis."""
    assert len(answer) == len(secret)
    i: int = 0
    result: str = ""
    WHITE_BOX: str = "\U00002B1C"
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"
    while (i < len(secret)):   # iterates through each character of input or length of input
        if (secret[i] == answer[i]):
            result = result + GREEN_BOX   # if letters match input Green em
            i = i + 1
        elif (contains_char(secret, answer[i]) is True):  
            result = result + YELLOW_BOX
            i = i + 1
        elif (contains_char(secret, answer[i]) is False):
            result = result + WHITE_BOX
            i = i + 1
    return result        


def input_guess(expected: int) -> str:
    """Check input."""
    word: str = input(f"Enter a {expected} character word: ")
    while (int(len(word)) != expected):
        word = input(f"That wasn't {expected} chars! Try again: ")
    return word
  

def main() -> None:
    """The entrypoint of the program and main game loop."""
    answer: str = ""
    result: str = ""
    secret: str = "codes"
    i: int = 1
    GREEN_BOX: str = "\U0001F7E9"
    while (i < 7):
        print(f"=== Turn { i }/6 ===")
        answer = input_guess(5)
        result = emojified(answer, secret)
        if (str(result) == str(((int(len(secret))) * GREEN_BOX))):  # evaluates the result with length of secret * Green_Box
            print(result)
            print(f"You won in {i}/6 turns!")
            i = 7
        else:
            print(result)
            if (i == 6):
                print("X/6 - Sorry, try again tomorrow!")  
        i = i + 1
       

if (__name__ == "__main__"):
    main()