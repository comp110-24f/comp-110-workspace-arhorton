"""while, for in loops, and for in range loops"""

__author__ = "730664552"

x: list[int] = [9, -1, 8, 5]
y: list[str] = ["cat", "dog", "turtle", "elephant", "fish"]
z: list[str] = ["z"]


def xwhile1(x: list[int]) -> None:
    index: int = 0
    while index < len(x):
        print(f"Here is: {x[index]}")
        print(index)
        index += 1
    return None


def ywhile1(y: list[str]) -> None:
    index: int = 0
    while index < len(y):
        print(f"This is an animal, {y[index]}!")
        print(index)
        index += 1
    else:
        print("NOPE!")
    return None


def zwhile1(z: list[str]) -> None:
    index: int = 0
    while index < len(z):
        print(f"Only one element this time: {z[index]}")
        print(index)
        index += 1
    else:
        print("Haha you're done!")
    return None


def xfor(x: list[int]) -> None:
    for x in x:
        print(f"This is the value at {x}!")
    return None


def yfor(y: list[str]) -> None:
    for y in y:
        print(f"This is an animal: {y}!")
    return None


def zfor(z: list[str]) -> None:
    for z in z:
        print(f"There is only one element: {z}")
    return None


def xforrange(x: list[int]) -> None:
    index: int = 0
    for index in range(0, len(x)):
        print(f"Holy cow it's a {x[index]}")
        print(index)
    return None


def yforrange(y: list[str]) -> None:
    index: int = 0
    for index in range(0, len(y)):
        print(f"Holy moly it's a {y[index]}! Run away!")
        print(index)
    return None


def zforrange(z: list[str]) -> None:
    index: int = 0
    for index in range(0, len(z)):
        print(f"Uh oh, there's only one {z[index]}!")
        print(index)
    return None


numbers: dict[int, float] = {2: 2.0, 3: 3.0, 4: 4.0}

updated = (
    {2: 2.0, 3: 3.0, 4: 4.0},
    {5: 5.0, 6: 6.0},
)

numbers[3] = numbers.pop(6)

mydictionary: dict[str, float] = {}

msg: dict[str, int] = {"Hello": 1, "Yall": 2}
msg["Yall"] += 3
print(msg)

ids: dict[int, str] = {100: "Alyssa", 200: "Carmine"}
ids.pop(100)
print(ids)

ids1: dict[int, str] = {100: "Alyssa", 200: "Carmine"}
print(len(ids1))

inventory: dict[str, int] = {"pens": 10, "notebooks": 5, "erasers": 8}
inventory["markers"] = 15

prices: dict[str, float] = {"bread": 2.99, "milk": 1.99, "eggs": 3.49}
prices["milk"] = 2.50

scores: dict[str, int] = {"Alice": 85, "Bob": 90, "Charlie": 88}
for x in scores:
    print(x)

scores1: dict[str, int] = {"Alice": 85, "Bob": 90, "Charlie": 88}
total_score = sum(scores)
total_score = sum(inp_dict=scores)

first_dict: dict[str, int] = {"a": 1, "b": 2}
second_dict: dict[str, int] = {"c": 3, "d": 4}
combo_dict: dict[str, int] = {"a": 1, "b": 2, "c": 3, "d": 4}


fruit_count: dict[str, int] = {"apples": 5, "bananas": 8}
for elem in fruit_count:
    new = fruit_count[index]
    print(f"{elem}: {new}")

    stats: list[int] = [7, 8, 9]
    index: int = 0
    total: int = 100
    while index < len(stats):
        total -= stats[index]
        index += 1

    stats: list[int] = [7, 8, 9]
    total: int = 100
    for index in stats:
        total -= index

    stats: list[int] = [7, 8, 9]
    total: int = 100
    for index in range(0, len(stats)):
        total -= stats[index]


x37 = "python is annoying"


def scope() -> None:
    x37 = "I love comp 110"
    x37 == global x37
    print(x37)
