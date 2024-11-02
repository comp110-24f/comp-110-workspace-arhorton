"""Dictionary utils"""

__author__ = "730664552"


def invert(
    dict1: dict[str, str]
) -> dict[str, str]:  # will return a dictionary of two strings
    """Inverting a dictionary"""
    invert: dict[str, str] = {}  # makes an empty dictionary
    for key in dict1:
        if dict1[key] in invert:  # if the key is already found
            raise KeyError("These are duplicate keys!")
        val = dict1[key]  # reverses the value and the key
        invert[val] = key
    return invert  # returns the new dictionary


def favorite_color(dict2: dict[str, str]) -> str:  # returns the collor name
    """Returning the count of the duplicate favorite colors"""
    favorite_color: str = ""  # an empty string to add the color name to
    result: dict[str, int] = {}  # an empty dict to work with
    max: int = 0  # the count of the number of favorite colors
    for x in dict2:  # for each element in dict2
        if dict2[x] not in result:  # if it is not present,
            result[dict2[x]] = 1  # set equal to one
        else:
            result[dict2[x]] += 1  # if it is present, increment by 1
    for x in result:  # now that we have made the new dictionary
        if result[x] > max:  # if the current value > max
            max = result[x]  # then it is the new max
    for x in result:  # for x in result again
        if result[x] == max:  # if they are equal
            return x  # then just return x as the final
    return favorite_color  # return the string of the most popular favorite color


def count(list1: list[str]) -> dict[str, int]:
    """Counts instances of characters in a string and returns a dict with counts"""
    result1: dict[str, int] = {}  # instantiates an empty dictionary
    for x in list1:  # iterates through the list
        if x in result1:  # if x is present
            result1[x] += 1  # increment the count by 1
        else:  # if it is not present
            result1[x] = 1  # assign it the value 1
    return result1


def alphabetizer(list2: list[str]) -> dict[str, list[str]]:
    """Categorizing the elements in the dictionary by the first letter"""
    dict_1: dict[str, list[str]] = {}  # starts an empty dictionary
    for x in list2:  # iterates through all elements in list2
        letter = x[0].lower()  # makes all uppercase lower
        if letter in dict_1:  # if the letter is in the dictionary,
            dict_1[letter].append(x)  # append the value at that letter
        else:  # if it is not present,
            dict_1[letter] = [x]  # then assign it with the current value
    return dict_1  # returns the new dictionary


def update_attendance(
    attendance_log: dict[str, list[str]], day: str, student: str
) -> None:  # returns the mutated dictionary
    """Updates the attendance log daily"""
    if day in attendance_log:  # if the day is in the log
        if student not in attendance_log[day]:  # if the student isn't in the log
            attendance_log[day].append(student)  # add it to the list
    else:  # if day is not in the list
        attendance_log[day] = [student]  # start a new day with that student
    return None  # returns None
