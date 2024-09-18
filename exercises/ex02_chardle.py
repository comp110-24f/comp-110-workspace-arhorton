"""EX02 - Chardle - A cute step towards Wordle."""

__author__ = "730664552"


def input_word() -> str:
    """The function that will check the input word"""
    # struggled with getting the length function to work
    word: str = str(input("Enter a 5-character word: "))
    # the local variable word, for the five letter word
    if len(word) == 5:
        return word  # prints the result if the word given has five letters
    elif len(word) > 5:  # returns the result if the word doesn't have five letters
        print("Error: Word must contain 5 characters.")
        exit()  # the exit function that leaves when character # > 5
    return word


def input_letter() -> str:
    """The function that will check the input letter"""
    letter: str = str(input("Enter a single character: "))
    if len(letter) == 1:  # if the input is only one character
        return letter  # prints the result of the input if only one character
    else:  # if the input is more than one character
        print("Error: Character must be a single character.")
        exit()  # allows the function to exit if the chacter is longer than 1
    return letter


def contains_char(input_word: str, input_letter: str) -> None:
    print("Searching for " + str(input_letter) + " in " + str(input_word))
    # prints the "searching for" message
    count: int = 0
    # starts the count at 0 for the index, local variable
    if input_letter == input_word[0]:
        print(str(input_letter) + " found at index " + str(0))
        count += 1
        # defines the word and letter at index 0
        # had to go to office hours to work this out - I was making it too complicated
    if input_letter == input_word[1]:
        print(input_letter + " found at index " + str(1))
        count += 1
        # print the word and letter at index 1
    if input_letter == input_word[2]:
        print(input_letter + " found at index " + str(2))
        # prints the word and letter at index 2
        count += 1
    if input_letter == input_word[3]:
        print(input_letter + " found at index " + str(3))
        count += 1
        # prints the word and letter at index 3
    if input_letter == input_word[4]:
        print(input_letter + " found at index " + str(4))
        count += 1
        # prints the word and letter at index 4, the last index
    if count == 0:  # the condition when count = 0
        print("No instances of " + input_letter + " found in " + input_word)
        # changed this to be "found in"
    elif count == 1:  # prints when the count only equals 1
        print("1 instance of " + input_letter + " found in " + input_word)
    else:  # prints this if the count is any greater than 1
        print(str(count) + " instances of " + input_letter + " found in " + input_word)
    return None  # no return type - returned statements print


def main() -> None:
    contains_char(input_word=input_word(), input_letter=input_letter())
    # calls the contain_char function into one big main function
    # struggled a little with this, finally just used the syntax from earlier


if __name__ == "__main__":
    main()
    # allows for the main function to be run with just main()
