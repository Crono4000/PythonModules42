
class Plant():
	def __init__(self, name: str, height: float, age: int, growth: float) -> None:
		self.name: str = name
		self.height: float = height
		self.plant_age: int = age
		self.growth: float = growth
		self.show(beginning="Created: ")

	def show(self, beginning: str = "") -> None:
		print(f"{beginning}{self.name}: {round(self.height, 1)}cm, {self.plant_age} days old")

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
	print("=== Garden Factory Output ===")
	rose: Plant = Plant("Rose", 25.0, 30, 0.5)
	oak: Plant = Plant("Oak", 200.0, 365, 0.5)
	cactus: Plant = Plant("Cactus", 5.0, 120, 0.5)
	sunflower: Plant = Plant("Sunflower", 80.0, 45, 0.5)
	fern: Plant = Plant("Fern", 15.0, 120, 0.5)
