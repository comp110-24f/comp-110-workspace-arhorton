"""Making a Wordle game!"""

__author__ = "730664552"  # author variable


def input_guess(
    inputword_len: int,
) -> str:  # function checking the length of the input guess function
    """Input guess length"""
    word: str = input(
        f"Enter a {str(inputword_len)} character word: "
    )  # changing the character # based on the input length
    # f-string (you don't need extra quotation marks in there, the f string does it all)
    while (
        len(word) != inputword_len
    ):  # kept running an infinite loop; changed it to evaluate without the ==
        word = input(f"That wasn't {inputword_len} chars! Try again: ")
    return word  # only returns word if the while loop condition evaluates to False


def contains_char(secret_word: str, char_guess: str) -> bool:
    """Searching for a character within an input string"""
    assert len(char_guess) == 1  # want our char guess to only be 1
    index: int = 0  # starts the index at zero
    while index < len(secret_word):  # had to change this to avoid index errors
        if secret_word[index] == char_guess:  # if they are the same, I want True
            return True
        index += 1  # moving the index analyzed along to compare again
    index += 1  # when they exit, go to the next index to compare
    return False  # return False if the char_guess isn't present at all


def emojified(guess: str, secret: str) -> str:
    """Using emojis to represent the placement of letters in your guess"""
    assert len(guess) == len(secret)
    WHITE_BOX: str = "\U00002B1C"  # the emoji box characters
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"
    index: int = 0
    answer: str = ""  # concatenates the boxes together - was very confused about this
    while index < len(guess):
        if guess[index] == secret[index]:
            answer += GREEN_BOX  # if they are the same, we want a green box
        elif contains_char(
            secret, guess[index]
        ):  # calling our contains_char function which cycles through all characters
            answer += YELLOW_BOX  # present but not in the right spot
        else:
            answer += WHITE_BOX  # not present at all
        index += 1  # scales the index up by one to enter the while loop again
    return answer  # returns the line of boxes


def main(
    secret: str,
) -> None:  # had to come to office hours to get this function straightened out
    """The entrypoint of the program and main game loop."""
    N: int = 1  # starting at turn 1, not turn zero
    index: int = 0
    while (
        index < 6
    ):  # will always only have six turns, regardless of the length of the word
        print(f"=== Turn {N}/6 ===")  # prints the turn number before the guess is made
        guess: str = input_guess(
            inputword_len=len(secret)
        )  # defines the guess variable as the input guess
        if guess == secret:  # if they are equal, print all green and they won
            print(emojified(guess, secret))
            print(f"You won in {N}/6 turns!")
            return None  # exiting the function when correct guess is made
        else:  # if they are not equal, print the result of emojified
            print(emojified(guess, secret))
        index += 1  # why is it stopping only at 3 turns? - was scaling by 2 each time
        N += 1  # this I think is working? - is scaling correctly
    print(
        "X/6 - Sorry, try again tomorrow!"
    )  # wanted this to print at the end, once the while loop had evaluated
    return None  # matches the return type of the main function


if (
    __name__ == "__main__"
):  # allows for the function to be called with just the main keyword
    main(secret="codes")
