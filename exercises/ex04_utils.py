"""Utils exercise!"""  # docstring describing what the exercise is about

__author__ = "730664552"


def all(list: list[int], number: int) -> bool:  # return type is a boolen
    """Tests if all of the ints in a list are the same as the number input"""
    index: int = 0  # starting the index at 0 so that it can scale
    if len(list) == 0:
        return False
    while index < len(list):
        if number != list[index]:  # if they don't equal each other
            return False  # return value - helps the function exit early
        index += 1
    index += 1  # scales the while loop
    return True  # if all conditions are met, return True


def max(list: list[int]) -> int:
    """Finds the max number in a list"""
    if len(list) == 0:  # empty list error
        raise ValueError("max() arg is an empty list")
    index: int = 0  # starting the index at zero
    max: int = list[index]  # starting the max value at one so that it can be added to
    while index < len(list):
        if list[index] > max:  # if the value at index is less than the original
            max = list[index]  # concetanate the new value to the max list
        else:
            index += 1  # scale the index
    return max


def is_equal(list1: list[int], list2: list[int]) -> bool:  # returns a boolean
    """Tests if all of the values in two lists are exactly equal"""
    index: int = 0  # starting the index at zero
    if len(list1) != len(list2):
        return False
    while index < len(list2):
        if list1[index] != list2[index]:
            return False  # lets the function exit early
        index += 1
    index += 1  # scales the index by one to evaluate the while loop again
    return True  # if the while loop is fine, exit and return True


def extend(list1: list[int], list2: list[int]) -> None:  # return type is none
    """Appends list2 to the end of list1"""
    index: int = 0
    while index < len(list2):
        list1.append(list2[index])
        index += 1
    return None
