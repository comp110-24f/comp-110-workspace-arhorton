"""Mutating functions."""

___author___ = "730664552"


def manual_append(list: list[int], number: int) -> None:
    list.append(number)  # adds the number parameter to the end of a list


def double(list: list[int]) -> None:  # doubles each of the values in my list
    index: int = 0
    while index < len(list):  # iterates over each value in the list and multiplies by 2
        list[index] = list[index] * 2
        index += 1  # scales the index + 1 every time the loop completes
    return None  # no return value


list1: list[int] = [1, 2, 3]  # global variables
list2: list[int] = list1  # makes list2 equal to list1
print(list1)  # functional call for list1
print(list2)  # function call for list2
