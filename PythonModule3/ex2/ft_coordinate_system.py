
import math


def get_player_pos() -> tuple[float, float, float]:
    parts: str = ""
    coordinates: list[float] = []
    continu: bool = True
    while continu:
        parts = input("Enter new coordinates as "
                      "floats in format 'x,y,z':").split(",")
        if len(parts) != 3:
            print("Invalid syntax")
            continue
        continu = False
        for part in parts:
            try:
                coordinates.append(float(part))
            except ValueError:
                print(f"Error on parameter '{part}': could not convert string "
                      f"to float: '{part}'")
                continu = True
    return (coordinates[0], coordinates[1], coordinates[2])


def calculate_distance_positions(p1: tuple[float, float, float],
                                 p2: tuple[float, float, float]) -> float:
    return math.sqrt(((p1[0] - p2[0])**2) + ((p1[1] - p2[1])**2) +
                     ((p1[1] - p2[1])**2))


if __name__ == "__main__":
    print("=== Game Coordinate System ===\n")
    print("Get a first set of coordinates")
    pos1: tuple[float, float, float] = get_player_pos()
    print(f"Got a first tuple: {pos1}")
    print(f"It includes: X={pos1[0]}, Y={pos1[1]}, Z={pos1[2]}")
    print(f"Distance to center: "
          f"{calculate_distance_positions(pos1, (0.0, 0.0, 0.0))}")
    print("")
    print("Get a second set of coordinates")
    pos2: tuple[float, float, float] = get_player_pos()
    print(f"Distance between the 2 sets of coordinates: "
          f"{calculate_distance_positions(pos1, pos2)}")
