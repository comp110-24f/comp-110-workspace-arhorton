my_list: list[int] = list()
my_list.append(8)
my_list.append(0)
my_list.append(3)
my_list.append(-1)
my_list.pop(2)
my_list[0] = 0


my_dict: dict[int, str] = {}
my_dict[8] = "eight"
my_dict[0] = "zero"
my_dict[3] = "three"
my_dict[-1] = "negative one"
my_dict.pop(3)
my_dict[0] = "cat"
my_dict[8] = "zero"


my_dict1: dict[int, str] = {0: "dog", 1: "cat", 2: "mouse", 3: "bird", 4: "whale"}


my_dict3: dict[str, str] = {
    "cat": "dog",
    "dog": "cat",
    "bird": "mouse",
    "mouse": "bird",
    "while": "whale",
}


list1 = "yay", "awesome", "cool", "fun"


def size(list1: list[str]) -> list[int]:
    newlist: list[int] = []
    for x in list1:
        newlist.append(len(x))
    return newlist


def sum1(list1: list[str]) -> int:
    total: int = 0
    for x in list1:
        total += len(x)
    return total


def exclamation(list1: list[str]) -> None:
    for i in range(len(list1)):
        list1[i] += "!"


def separator(string: list[str]) -> list[str]:
    newlist: list[str] = []
    index: int = 0
    while index < len(string):
        print(newlist.append(f"{string[index]},"))
        index += 1
    return newlist


def listsize(size: int) -> list[int]:
    newlist: list[int] = []
    for x in range(0, size):
        newlist.append(x)
    return newlist


list_size: list[int] = listsize(4)


def floatinsert(list2: list[float], where: int, value: float) -> None:
    list2.append(list2[len(list2) - 1])
    index = len(list2) - 2
    while index > where:
        list2[index] = list2[index - 1]
        index -= 1
    list2[where] = value
    return None


def evens(list3: list[int]) -> list[int]:
    index: int = 0
    newlist: list[int] = []
    while index < len(list3):
        if index % 2 == 0:
            newlist.append(index)
            index += 1
        else:
            index += 1
    return newlist


def ass(list_1: list[str]) -> list[str]:
    newlist: list[str] = []
    for x in list_1:
        if "a" in x:
            newlist.append(x)
    return newlist


def largest(list_2: list[int]) -> None:
    index: int = 0
    max: int = 0
    while index < len(list_2):
        if list_2[index] > max:
            max = list_2[index]
            index += 1
        else:
            index += 1
    return None


def charcount(string: str) -> dict[str, int]:
    """Return a dictionary with the counts of each vowel in the string"""
    result: dict[str, int] = {"a": 0, "e": 0, "i": 0, "o": 0, "u": 0}
    for x in range(0, len(string)):
        if string[x] in result:
            result[string] += 1
    return result


def common(list_11: list[int], list_22: list[int]) -> list[int]:
    idx: int = 0
    listresult: list[int] = []
    if list_11[idx] == list_22[idx]:
        listresult.append(idx)
        idx += 1
    else:
        idx += 1
    return listresult


def sorting(strings: list[str]) -> None:
    idx: int = 0
    sort: list[str] = []
    while idx < len(strings):
        if len(strings[idx]) > len(strings[idx - 1]):
            sort.append(idx)
        else:
            idx += 1
    return None
