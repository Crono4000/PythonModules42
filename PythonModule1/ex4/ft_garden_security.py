
class Plant():
	_name: str = ""
	_height: float = 1
	_age: int = 0
	_growth: float = 0

	def __init__(self, name: str, height: float, age: int, growth: float) -> None:
		self._name = name
		self.set_height(height, notification=False)
		self.set_age(age, notification=False)
		self._growth = growth
		self.show(beginning="Plant created: ")

	def show(self, beginning: str = "") -> None:
		print(f"{beginning}{self._name}: {round(self._height, 1)}cm, {self._age} days old")

	def grow(self) -> None:
		self.set_height(self._height + self._growth)

	def age(self, time: int) -> None:
		self.set_age(self._age + time)

	def set_age(self, new_age: int, notification: bool = True) -> None:
		if new_age >= 0:
			self._age = new_age
			if notification:
				print(f"Age updated: {new_age} days")
		else:
			print(f"{self._name}: Error, age can't be negative\nAge update rejected")
	
	def set_height(self, new_height: int, notification: bool = True) -> None:
		if new_height >= 0:
			self._height = new_height
			if notification:
				print(f"Height updated: {new_height}cm")
		else:
			print(f"{self._name}: Error, height can't be negative\nHeight update rejected")
	
	def get_height(self) -> float:
		return self._height

	def get_age(self) -> int:
		return self._age

	def get_name(self) -> str:
		return self._name

	def pass_days(self, days: int, period: str = "period") -> None:
		print("=== Garden Plant Growth ===")
		self.show()
		for day in range(1, days):
			print(f"=== Day {day} ===")
			self.age(1)
			self.grow()
			self.show()
		print(f"Growth this {period}: {round(self._growth * days, 1)}cm")

if __name__ == "__main__":
	print("=== Garden Factory Output ===")
	rose: Plant = Plant("Rose", 15.0, 10, 0.5)
	print("")
	rose.set_height(25.0)
	rose.set_age(30)
	print("")
	rose.set_height(-2.0)
	rose.set_age(-1000)
	print("")
	rose.show(beginning="Current state: ")
