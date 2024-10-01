"""Basic syntax - lists"""

my_numbers: list[float] = []  # literal

# add a number to the list
my_numbers.append(1.5)
my_numbers.append(2.3)
my_numbers.append(2.3)
print(my_numbers)


# create an already populated list
game_points: list[int] = [102, 86, 94]
game_points[1] = 72
len(game_points)
game_points.pop(1)


def display(input: list[int]) -> None:
    index: int = 0
    while index < len(input):
        print(input[index])
        index += 1
    return None


display(input=game_points)
