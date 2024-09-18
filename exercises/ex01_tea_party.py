"""tea party exercise"""

# the author line keeps moving up when i save my code
__author__: str = "730664552"


def main_planner(guests: int) -> None:
    """planning for the party as a whole"""
    print(
        "A Cozy Tea Party for " + str(guests) + " People!"
    )  # prints the cozy tea party line
    # got this down relatively fast - had to change the type of the guests variable
    # didn't need to make the parameters equal to each other
    # print will print the two strings with the int concatenated
    # had to change the type of all of the function calls to concatenate right
    print(
        "Tea Bags: " + str(tea_bags(guests))
    )  # prints the result of tea bags function call
    print(
        "Treats: " + str(treats(guests))
    )  # prints the result of the treats function call
    # went to office hours, had to connect parameters across functions
    print("Cost: $" + str(cost(tea_bags(guests), treats(guests))))
    # struggled here with getting the functions to print variables (office hours)
    # had to call tea_bags and treats up higher to get output to print
    # struggled here with getting the spacing right - autograder issue
    # i was defining the parameter with the function(arg) before it existed
    return None  # only printing, no return value


# i can't figure out how to make it print the retun value
# how to get my functions defined down below to be called up here
# need to add the function call in here


# was not quite sure how to name the function and define it at the same time
def tea_bags(people: int) -> int:
    """Multiply two numbers together - 2 and number of guests for tea bags"""
    return people * 2  # returning parameter * 2


# took me a minute to realize that I didn't need to import the multiplication function
# why is the arrow giving me problems?
# I am not sure how to get it to multiply times 2


def treats(people: int) -> int:
    "for every 1 tea bag, 1.5 treats"
    return int(
        tea_bags(people=people) * 1.50
    )  # returning the int result of treats with calling tea_bags


# trying to figure out how to make this an int instead of a float - tried lots of things
# the float is working, i just need to figure out how to turn the output into an int
# had to change the type of the return value


def cost(tea_count: int, treat_count: int) -> float:
    """ "returns the total cost of the treats and teats combined"""
    return (tea_count * 0.50) + (treat_count * 0.75)


if __name__ == "__main__":
    main_planner(guests=int(input("How many guests are attending your tea party?")))
    # this was very easy to do, i just typed it in to the module
    # the return value is not correct - I fixed a spacing issue
