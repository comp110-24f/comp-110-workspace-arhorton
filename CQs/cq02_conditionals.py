"""Challenge question #2 - practice with conditionals and a number guessing game."""

___author___ = "730664552"


def guess_a_number() -> None:
    """Guessing a number and seeing if it matches the secret number."""
    secret: int = 7  # defines the secret number
    x: int = int(input("Guess a number:"))  # defines the input of the guesses
    print("Your guess was " + str(x))
    if x == secret:  # if the guess is equal
        print("You got it!")
    elif x < secret:  # if the guess is less than the seven
        print("Your guess was too low! The secret number is", str(secret))
    else:  # if the guess is higher than the seven
        print("Your guess was too high! The secret number is", str(secret))


if __name__ == "__main__":
    """Calls the guess a number function."""
    guess_a_number()
