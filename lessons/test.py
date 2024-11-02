x: list[int] = [9, -1, 8, 5]
y: list[str] = ["cat", "dog", "turtle", "elephant", "fish"]
z: list[str] = ["z"]


def x_list(x: list[int]) -> None:
    index: int = 0
    while index < len(x):
        print(f"{x[index]} is at index {index}")
        print(index)
        index += 1
    return None


def y_list(y: list[str]) -> None:
    index: int = 0
    while index < len(y):
        print(f"{y[index]} is at index {index}")
    return None


def z_list(z: list[str]) -> None:
    index: int = 0
    while index < len(z):
        print(f"{z[index]} is at index {index}")
        print(index)
        index += 1
    return None


def x_list1(x: list[int]) -> None:
    index: int = 0
    for index in x:
        print(f"Howdy, {index}!")
        print(index)
        index += 1
    return None


def y_list1(y: list[str]) -> None:
    for index in y:
        print("Howdy", index, "!")
    return None


def z_list1(z: list[str]) -> None:
    for index in z:
        print("Howdy", index, "!")
    return None


def x_list2(x: list[str]) -> None:
    for index in range(len(x)):
        print(f"Heyo, {x[index]}! You are at {index}!")
        index += 1
    return None


def y_list2(y: list[str]) -> None:
    for index in range(len(y)):
        print(f"Heyo, {y[index]}! You are at {index}!")
        index += 1
    return None


def z_list2(z: list[str]) -> None:
    for index in range(len(z)):
        print(f"Heyo, {z[index]}! You are at {index}!")
        index += 1
    return None


stats: list[int] = [7, 8, 9]
index: int = 0
total: int = 100
while index < len(stats):
    total -= stats[index]
    index += 1

for index in stats:
    total -= index

for index in range(0, len(stats)):
    total -= stats[index]
