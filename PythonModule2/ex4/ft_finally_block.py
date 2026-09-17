
class GardenError(Exception):
    def __init__(self, message: str = "Unknown plant error"):
        super().__init__(message)


class PlantError(GardenError):
    def __init__(self, message: str = "Unknown plant error"):
        super().__init__(message)


def water_plant(plant_name: str) -> None:
    if plant_name.capitalize() != plant_name:
        raise PlantError(f"Invalid plant name to water: {plant_name}")
    print(f"Watering {plant_name}: [OK]")


def test_watering_plant():
    print("=== Garden Watering System ===\n\nTesting valid plants...\n"
          "Opening watering system")
    water_plant("Tomato")
    water_plant("Lettuce")
    water_plant("Carrots")
    print("Closing watering system\n")
    print("Testing valid plants...\nOpening watering system")
    try:
        water_plant("Tomato")
        water_plant("lettuce")
    except PlantError as er:
        print(f"Caught PlantError: {er}")
    finally:
        print(".. ending tests and returning to main")
        print("Closing watering system\n")
        print("Cleanup always happens, even with errors!")


if __name__ == "__main__":
    test_watering_plant()
