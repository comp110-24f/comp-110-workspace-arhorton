"""function writing questions, studying for quiz 2"""


def odd_and_even(list_1: list[int]) -> list[int]:
    newlist: list[int] = []
    for index in range(0, len(list_1)):
        if index % 2 == 0 and list_1[index] % 2 != 0:
            newlist.append(list_1[index])
            index += 1
    return newlist


def short_words(list_1: list[str]) -> list[str]:
    """Return a list of words that are shorter than 5 characters"""
    newlist: list[str] = []
    for index in range(0, len(list_1)):
        if len(list_1[index]) < 5:
            newlist.append(list_1[index])
            index += 1
        else:
            print(f"{list_1[index]} is too long!")
    return newlist


def multiples(list_1: list[int]) -> list[bool]:
    newlist: list[bool] = []
    newlist.append(list_1[0] % list_1[len(list_1) - 1] == 0)
    index: int = 1
    while index < len(list_1):
        newlist.append(list_1[index] % list_1[index - 1] == 0)
        index += 1
    return newlist


def reverse_multiply(list_1: list[int]) -> list[int]:
    newlist: list[int] = []
    index: int = len(list_1) - 1
    while index >= 0:
        newlist.append(list_1[index] * 2)
        index -= 1
    return newlist


xman = "awesome"


def myfunc():
    print("Python is", xman)


def population() -> None:
    index: int = 0
    xman = "yo mamas"
    while index < len(xman):
        print(f"Hi, {xman[index]}!")
        index += 1
    if index == len(xman):
        print("All done with letters!")
    return None
