"""The fourth file for studying for quiz 02!"""


def odd_and_even(list1: list[int]) -> list[int]:
    count: list[int] = []
    for x in range(0, len(list1)):
        if list1[x] % 2 != 0 and x % 2 == 0:
            count.append(list1[x])
        else:
            x += 1
    return count


def short_words(list2: list[str]) -> list[str]:
    newlist: list[str] = []
    for x in list2:
        if len(x) < 5:
            newlist.append(x)
        else:
            print(f"{x} is too long!")
    return newlist


my_dictionary: dict[str, float] = {}

msg: dict[str, int] = {"Hello": 1, "Yall": 2}
msg["Yall"] += 3
print(msg)

ids: dict[int, str] = {100: "Alyssa", 200: "Carmine"}
ids.pop(100)
print(len(ids))

inventory: dict[str, int] = {"pens": 10, "notebooks": 5, "erasers": 8}
inventory["markers"] = 15
print(inventory)

prices: dict[str, float] = {"bread": 2.99, "milk": 1.99, "eggs": 3.49}
prices["milk"] = 2.50
print(prices)

scores: dict[str, int] = {"Alice": 85, "Bob": 90, "Charlie": 88}
keys: list[str] = []
for x in scores:
    keys.append(x)
print(keys)

scores1: dict[str, int] = {"Alice": 85, "Bob": 90, "Charlie": 88}


fruit_count: dict[str, int] = {"apples": 5, "bananas": 8}
for x in fruit_count:
    print(f"{x}: {fruit_count[x]}")

first_dict: dict[str, int] = {"a": 1, "b": 2}
second_dict: dict[str, int] = {"c": 3, "d": 4}

stats: list[int] = [7, 8, 9]
total: int = 100
for index in stats:
    total -= index

stats: list[int] = [7, 8, 9]
total: int = 100
for index in range(0, len(stats)):
    total -= stats[index]
