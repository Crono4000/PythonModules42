
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
        if show:
            self.show(beginning="Plant created: ")

    def show(self, beginning: str = "") -> None:
        print(f"{beginning}{self._name}: {round(self._height, 1)}cm, "
              f"{self._age} days old")

    def grow(self) -> None:
        self.set_height(self._height + self._growth, notification=False)

    def age(self, time: int) -> None:
        self.set_age(self._age + time, notification=False)

    def set_age(self, new_age: int, notification: bool = True) -> None:
        if new_age >= 0:
            self._age = new_age
            if notification:
                print(f"Age updated: {new_age} days")
        else:
            print(f"{self._name}: Error, age can't "
                  "be negative\nAge update rejected")

    def set_height(self, new_height: int, notification: bool = True) -> None:
        if new_height >= 0:
            self._height = new_height
            if notification:
                print(f"Height updated: {new_height}cm")
        else:
            print(f"{self._name}: Error, height can't be"
                  " negative\nHeight update rejected")

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


class Flower(Plant):
    _color: str = "green"
    _blooming: bool = False

    def __init__(self, name: str, height: float, age: int, growth: float, 
                 color: str) -> None:
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


class Tree(Plant):
    _trunk_diameter: float = 0.0

    def __init__(self, name: str, height: float, age: int, 
                 growth: float, trunk_diameter: float) -> None:
        super().__init__(name, height, age, growth, show=False)
        self._trunk_diameter = trunk_diameter

    def show(self, beginning: str = "") -> None:
        super().show()
        print(f" Trunk diameter: {self._trunk_diameter}")

    def produce_shade(self):
        # print(f"[asking the {self._name} to shade]")
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


if __name__ == "__main__":
    print("=== Garden Factory Types ===")
    rose: Flower = Flower("Rose", 15.0, 10, 0.5, "red")
    oak: Tree = Tree("Oak", 200.0, 365, 0.5, 200.0)
    tomato: Vegetable = Vegetable("Tomato", 5.0, 10, 1.1, "April", 0)

    print("=== Flower")
    rose.show()
    print("[asking the rose to bloom]")
    rose.bloom()
    rose.show()
    print("")

    print("=== Tree")
    oak.show()
    print("[asking the oak to shade]")
    oak.produce_shade()
    print("")

    print("=== Vegetable")
    tomato.show()
    print("[make tomato grow and age for 20 days]")
    tomato.pass_days(20, show=False)
    tomato.show()
