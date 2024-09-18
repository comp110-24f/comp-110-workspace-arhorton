"""practicing my conditionals"""


def less_than_10(num: int) -> None:
    """Tells us if num is less than 10"""
    dub: int = num * 2  # 14
    dub = dub - 1  # subtracting one, giving us 13
    print(dub)
    if num < 10:
        print("Small number!")
    else:
        print("Big number!")
    print("This is the end of the function!")


less_than_10(num=10)


def wake_up(alarm: bool) -> str:
    """Return a message based on if alarm is going off"""
    if alarm is False:
        return "Wake up! Go to Comp 110!"
    else:
        return "Keep sleeping. You deserve it. :)"


print(wake_up(alarm=True))


def check_first_letter(word: str, letter: str) -> str:
    if word[0] == letter:
        return "match!"
    else:
        return "no match!"


print(check_first_letter(word="happy", letter="h"))


def get_weather_report() -> str:
    """A function to identify the weather in this area"""
    weather: str = input("What is the weather?")
    if weather == "rainy" or weather == "cold":
        print("Bring a jacket!")
    elif weather == "hot":
        print("Keep cool out there!")
    else:
        "I don't recognize this weather."
    return weather


get_weather_report()

age: int = 11
age = age + 1
