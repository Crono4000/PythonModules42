
class Plant():
    def __init__(self, name: str, height: float, 
                 age: int, growth: float) -> None:
        self.name: str = name
        self.height: float = height
        self.plant_age: int = age
        self.growth: float = growth

    def show(self) -> None:
        print(f"{self.name}: {round(self.height, 1)}cm, "
              f"{self.plant_age} days old")

    def grow(self) -> None:
        self.height += self.growth

    def age(self, time: int) -> None:
        self.plant_age += time

    def pass_days(self, days: int, period: str = "period") -> None:
        print("=== Garden Plant Growth ===")
        self.show()
        for day in range(1, days):
            print(f"=== Day {day} ===")
            self.age(1)
            self.grow()
            self.show()
        print(f"Growth this {period}: {round(self.growth * days, 1)}cm")


if __name__ == "__main__":
    rose = Plant("Rose", 25, 30, 0.8)
    rose.pass_days(7, period="week")
