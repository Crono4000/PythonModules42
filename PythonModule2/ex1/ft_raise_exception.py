
def input_temperature(temp_str: str) -> int:
    x: int = int(temp_str)
    if x > 40:
        raise ValueError(f"{x}°C is too hot for plants (max 40°C)")
    if x < 0:
        raise ValueError(f"{x}°C is too cold for plants (min 0°C)")
    return x


def test_temperature_individual(temp_str: str) -> None:
    print(f"Input data is \'{temp_str}\'")
    try:
        x: int = input_temperature(temp_str)
        print(f"Temperature is now {x}°C")
    except ValueError as e:
        print(f"Caught input_temperature error: {e}")


def test_temperature() -> None:
    print("=== Garden Temperature ===")
    print("")
    test_temperature("25")
    print("")
    test_temperature("abc")
    print("")
    test_temperature("100")
    print("")
    test_temperature("-50")
    print("")
    print("All tests completed - program didn't crash!")


if __name__ == "__main__":
    test_temperature()
