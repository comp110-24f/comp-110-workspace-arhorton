"""tea party exercise"""

___author___ = "730664552"


def main_planner(guests: int) -> None:
    """ "how the function is getting going - the entryway"""
    return None


# how to get my functions referenced down below to work up here
# need to add the function call in here


# was not quite sure how to name the function and define it at the same time
def tea_bags(people: int) -> int:
    """Multiply two numbers together - 2 and number of guests for tea bags"""
    return people * 2


# took me a minute to realize that I didn't need to import the multiplication function
# why is the arrow giving me problems?
# I am not sure how to get it to multiply times 2


def treats(people: int) -> float:
    "for every 1 tea bag, 1.5 treats"
    return int(tea_bags(people) * 1.5)


# trying to figure out how to make this an int instead of a float - tried lots of things
# the float is working, i just need to figure out how to turn the output into an int


def cost(tea_count: int, treat_count: int) -> float:
    """ "returns the total cost of the treats and teats combined"""
    return (tea_count * 0.50) + (treat_count * 0.75)
