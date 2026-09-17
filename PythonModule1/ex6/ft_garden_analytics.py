

class Plant():
    _name: str = ""
    _height: float = 1
    _age: int = 0
    _growth: float = 0

    def __init__(self, name: str, height: float, age: int, growth: float,
                 show: bool = True) -> None:
        self._name = name
        self.set_height(height, notification=False)
        self.set_age(age, notification=False)
        self._growth = growth
        self._stats: Plant.Stats = self.Stats()
        if show:
            self.show(beginning="Plant created: ")

    @staticmethod
    def check_older_than_year(age: int) -> bool:
        if age > 356:
            return True
        else:
            return False

    def show(self, beginning: str = "") -> None:
        self._stats.increase_shows()
        print(f"{beginning}{self._name}: {round(self._height, 1)}cm,"
              f" {self._age} days old")

    def grow(self) -> None:
        self._stats.increase_grows()
        self.set_height(self._height + self._growth, notification=False)

    def age(self, time: int) -> None:
        self._stats.increase_ages()
        self.set_age(self._age + time, notification=False)

    def set_age(self, new_age: int, notification: bool = True) -> None:
        if new_age >= 0:
            self._age = new_age
            if notification:
                print(f"Age updated: {new_age} days")
        else:
            print(f"{self._name}: Error, age can't be"
                  " negative\nAge update rejected")

    def set_height(self, new_height: float, notification: bool = True) -> None:
        if new_height >= 0:
            self._height = new_height
            if notification:
                print(f"Height updated: {new_height}cm")
        else:
            print(f"{self._name}: Error, height can't be negative\n"
                  "Height update rejected")

    def get_height(self) -> float:
        return self._height

    def get_age(self) -> int:
        return self._age

    def get_name(self) -> str:
        return self._name

    def pass_days(self, days: int, period: str = "period",
                  show: bool = True) -> None:
        if show:
            self.show()
        for day in range(1, days):
            if show:
                print(f"=== Day {day} ===")
            self.age(1)
            self.grow()
            if show:
                self.show()
        if show:
            print(f"Growth this {period}: {round(self._growth * days, 1)}cm")

    @classmethod
    def anonymous_plant(cls) -> "Plant":
        return cls("Unknown plant", 0, 0, 0, show=False)

    class Stats():
        _grows: int = 0
        _ages: int = 0
        _shows: int = 0

        def increase_grows(self) -> None:
            self._grows += 1

        def increase_ages(self) -> None:
            self._ages += 1

        def increase_shows(self) -> None:
            self._grows += 1

        def get_grows(self) -> int:
            return self._grows

        def get_ages(self) -> int:
            return self._grows

        def get_shows(self) -> int:
            return self._grows

        def show(self) -> None:
            print(f"Stats: {self._grows} grow, {self._ages} age, "
                  f"{self._shows} show")

    def get_stats(self) -> Stats:
        return self._stats


class Flower(Plant):
    _color: str = "green"
    _blooming: bool = False

    def __init__(self, name: str, height: float, age: int,
                 growth: float, color: str) -> None:
        super().__init__(name, height, age, growth, show=False)
        self._color = color

    def show(self, beginning: str = "") -> None:
        super().show()
        print(f" Color: {self._color}")
        if self._blooming:
            print(f" {self._name} is blooming beautifully!")
        else:
            print(f" {self._name} has not bloomed yet")

    def bloom(self):
        # print(f"[asking the {self._name} to bloom]")
        self._blooming = True


class Seed(Flower):
    _seeds: int = 0
    _seeds_per_bloom: int = 0

    def __init__(self, name: str, height: float, age: int, growth: float,
                 color: str, seeds: int, seeds_per_bloom: int) -> None:
        super().__init__(name, height, age, growth, color)
        self._seeds = seeds
        self._seeds_per_bloom = seeds_per_bloom

    def bloom(self):
        super().bloom()
        self._seeds += self._seeds_per_bloom

    def show(self):
        super().show()
        print(f" Seeds: {self._seeds}")


class Tree(Plant):
    _trunk_diameter: float = 0.0

    class Stats(Plant.Stats):
        _shades: int = 0

        def increase_shades(self) -> None:
            self._shades += 1

        def show(self) -> None:
            super().show()
            print(f" {self._shades} shade")

    def __init__(self, name: str, height: float, age: int,
                 growth: float, trunk_diameter: float) -> None:
        super().__init__(name, height, age, growth, show=False)
        self._trunk_diameter = trunk_diameter

    def show(self, beginning: str = "") -> None:
        super().show()
        print(f" Trunk diameter: {self._trunk_diameter}")

    def produce_shade(self):
        # print(f"[asking the {self._name} to shade]")
        self._stats.increase_shades()
        print(f"Tree {self._name} now produces a shade of "
              f"{self._trunk_diameter}cm long and {self._height}cm wide.")


class Vegetable(Plant):
    _harvest_season: str = ""
    _nutritional_value: int = 0

    def __init__(self, name: str, height: float, age: int, growth: float,
                 harvest_season: str, nutritional_value: int) -> None:
        super().__init__(name, height, age, growth, show=False)
        self._harvest_season = harvest_season
        self._nutritional_value = nutritional_value

    def age(self, time: int) -> None:
        super().age(time)
        self._nutritional_value += 1

    def show(self, beginning: str = "") -> None:
        super().show()
        print(f" Harvest season: {self._harvest_season}")
        print(f" Nutritional value: {self._nutritional_value}")


def show_statistics(plant: Plant):
    print(f"[statistics for {plant.get_name()}]")
    plant.get_stats().show()


if __name__ == "__main__":
    print("=== Garden Statistics ===")
    rose: Flower = Flower("Rose", 15.0, 10, 8.0, "red")
    oak: Tree = Tree("Oak", 200.0, 365, 0.5, 200.0)
    sunflower: Seed = Seed("Sunflower", 5.0, 10, 1.1, "Yellow", 0, 42)
    anonymous: Plant = Plant.anonymous_plant()

    print("=== Check year-old")
    print("Is 30 days more than a year? -> ", Plant.check_older_than_year(30))
    print("Is 400 days more than a year? -> ",
          Plant.check_older_than_year(400))
    print("")

    print("=== Flower")
    rose.show()
    show_statistics(rose)
    print("[asking the rose to grow and bloom]")
    rose.bloom()
    rose.grow()
    rose.show()
    show_statistics(rose)
    print("")

    print("=== Tree")
    oak.show()
    show_statistics(oak)
    print("[asking the oak to produce shade]")
    oak.produce_shade()
    show_statistics(oak)
    print("")

    print("=== Seed")
    sunflower.show()
    show_statistics(sunflower)
    print("[make sunflower to grow, age and bloom]")
    sunflower.bloom()
    sunflower.grow()
    sunflower.age(1)
    sunflower.show()
    show_statistics(sunflower)
    print("")

    print("=== Anonymous")
    anonymous.show()
    show_statistics(anonymous)
