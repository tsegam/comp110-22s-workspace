"""Example of writing a function to search a list."""


def main() -> None:
    guess: str = input("What is the code word?")
    possible_answers: list[str] = ["pokemon", "wordle"]
    if contains(guess, possible_answers):
        print("We're letting you into the secret club...")
    else:
        print("Go back to Davis")


def contains(needle: str, haystack: list[str]) -> bool:
    """Search and check if string is in list."""
    for x in haystack:
        if x == needle:
            return True
    return False     


print(__name__)
if __name__ == "__main__":
    main()