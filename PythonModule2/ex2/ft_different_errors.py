
def garden_operations(operation_number: int) -> None:
    if operation_number == 0:
        print(f"{int("value")}")
    elif operation_number == 1:
        print(f"result: {2 / 0}")
    elif operation_number == 2:
        open("phineas")
    elif operation_number == 3:
        print("fi" + 0)
    elif operation_number == 4:
        xxxx: int = 0
        xxxx += 1


def test_error_individual(op: int):
    print(f"Testing operation {op}...")
    try:
        garden_operations(op)
        print("Operation completed successfully")
    except ValueError as e:
        print(f"Caught ValueError: {e}")
    except ZeroDivisionError as e:
        print(f"Caught ZeroDivisionError: {e}")
    except FileNotFoundError as e:
        print(f"Caught FileNotFoundError: {e}")
    except TypeError as e:
        print(f"Caught TypeError: {e}")


def test_error_types() -> None:
    test_error_individual(0)
    test_error_individual(1)
    test_error_individual(2)
    test_error_individual(3)
    test_error_individual(4)
    print("\n\nAll error types tested successfully!")


if __name__ == "__main__":
    test_error_types()
