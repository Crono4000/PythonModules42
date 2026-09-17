
class GardenError(Exception):
    def __init__(self, message: str = "Unknown plant error"):
        super().__init__(message)


class PlantError(GardenError):
    def __init__(self, message: str = "Unknown plant error"):
        super().__init__(message)


class WaterError(GardenError):
    def __init__(self, message: str = "Unknown plant error"):
        super().__init__(message)


def raise_garden_error(caught: str, error: GardenError,
                       ini: bool = True) -> None:
    if ini:
        print(f"Testing {caught}...")
    try:
        raise error
    except GardenError as error:
        print(f"Caught {caught}: ", error)


if __name__ == "__main__":
    print("=== Custom Garden Errors Demo ===")
    print("")
    raise_garden_error("GardenError",
                       GardenError("The tomato plant is wilting!"))
    print("")
    raise_garden_error("WaterError",
                       WaterError("Not enough water in the tank!"))
    print("\nTesting catching all garden errors...")
    raise_garden_error("GardenError", GardenError("The tomato plant "
                                                  "is wilting!"), ini=False)
    raise_garden_error("GardenError", GardenError("Not enough water in"
                                                  " the tank!"), ini=False)
    print("\nAll custom error types work correctly!")
