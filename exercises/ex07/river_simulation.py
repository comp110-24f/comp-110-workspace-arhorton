from exercises.ex07.fish import Fish
from exercises.ex07.bear import Bear
from exercises.ex07.river import River


class my_river:
    fish: list[Fish]
    bear: list[Bear]
    day: int

    def __init__(self, num_fish: int, num_bear: int):
        self.num_bear = 2
        self.num_fish = 10
        self.day = 0

    def view_river(self):
        day = 0
        print(f"~~~ Day {day}: ~~~")
        print(f"Fish population: {self.num_fish}")
        print(f"Bear population: {self.num_bear}")
        return None


my_river.view_river()
