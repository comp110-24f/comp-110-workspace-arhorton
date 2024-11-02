"""Finding a max challenge question"""

__author__ = "730664552"


def find_and_remove_max(list1: list[int]) -> int:
    max: int = 0  # starts the max value at zero to be added to
    index: int = 0  # starts the index at zer0
    if len(list1) == 0:
        return -1  # the edge case problem
    while index < len(list1):  # a while loop
        if list1[index] > max:  # if the list[index] > max, replace
            max = list1[index]  # replaced that value
        index += 1  # scaled the index
    index = 0  # started the index over at zero to make sure scale is right
    while index < len(list1):
        if list1[index] == max:  # if they are equal, remove it
            list1.pop(index)
        else:
            index += 1  # otherwise, scale the index += 1
    return max  # return the removed max value
