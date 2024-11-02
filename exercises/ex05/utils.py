"""List utility functions"""

__author__ = "730664552"


def only_evens(
    list1: list[int],
) -> list[int]:  # returns a new list of only the even values in the list
    """Will take an input list and only return the even values"""
    newlist: list[int] = []  # the starting empty list to assign the values to
    for index in list1:  # a for loop
        if index % 2 == 0:  # if they are even (divided by 2 equals no remainder)
            newlist.append(index)  # then they append to the newlist
        index += 1  # scale the index
    return newlist  # return the newest list


def sub(
    a_list: list[int], start: int, end: int
) -> list[int]:  # returns a new list of int
    """Will take out a subset of a list from the list overall"""
    newlist: list[int] = []
    if start < 0:  # if the list start is negative, push it to zero
        start = 0
    if end > len(
        a_list
    ):  # if the end index is greater than the list length, make it equal
        end = len(a_list)
    for index in range(start, end):  # if both start and end are within the range
        newlist.append(a_list[index])  # append the value at index to the empty list
    return newlist  # return the newly made list with the subs


def add_at_index(
    list_1: list[int], value: int, where: int
) -> None:  # return value is None
    """Shifts the list down, opening up a new index where a value is inserted"""
    if (
        len(list_1) == where
    ):  # if the length of the list == index where the value is inserted
        list_1.append(value)  # append the value if this is the case
        return None  # return None
    list_1.append(list_1[len(list_1) - 1])  # append value on end (the dummy value)
    index = len(list_1) - 2  # starting the index at the index two from the end
    while (
        index > where
    ):  # if the current index is greater than where inserting the value should happen
        list_1[index] = list_1[
            index - 1
        ]  # the value at that index should be assigned the one from the index before
        index -= 1  # subtract the index by one each time
    list_1[where] = value  # then place the value in at the appropriate index
    if (
        where > len(list_1) or where < 0
    ):  # if the index is larger than the length of the list or negative
        raise IndexError(
            "Index is out of bounds for the input list"
        )  # raise index error
    return None  # return value is none
