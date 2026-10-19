
import sys

if __name__ == "__main__":
    print("=== Inventory System Analysis ===")

    inventory: dict[str, int] = {}
    indice: int = 0

    for arg in sys.argv:
        if indice == 0:
            indice += 1
            continue
        arg_split: list[str] = arg.split(":")
        if len(arg_split) != 2:
            print(f"Error - invalid parameter \'{arg}\'")
            continue
        if arg_split[0] in inventory:
            print(f"Redundant item \'{arg_split[0]}\' - discarding")
            continue
        try:
            quantity: int = int(arg_split[1])
        except ValueError:
            print(f"Quantity error for \'{arg_split[0]}\': invalid literal for"
                  f" int() with base 10: \'{arg_split[1]}\'")
            continue
        inventory[arg_split[0]] = quantity
    print("Got inventory:", inventory)

    total: int = sum(inventory.values())
    print(f"Total quantity of the {len(inventory.keys())} "
          f"items: {total}")
    if total != 0:
        for key in inventory.keys():
            print(f"Item {key} represents"
            f"{round((inventory[key]/total)*100, 1)}%")

    key_current: str = ""
    for key in inventory.keys():
        if key_current == "":
            key_current = key
            continue
        if inventory[key] > inventory[key_current]:
            key_current = key
    if key_current != "":
        print(f"Item most abundant: {key_current} with quantity"
              f" {inventory[key_current]}")
    for key in inventory.keys():
        if inventory[key] < inventory[key_current]:
            key_current = key
    if key_current != "":
        print(f"Item least abundant: {key_current} with quantity"
              f" {inventory[key_current]}")

    inventory.update({"magic_item": 1})
    print("Updated inventory:", inventory)
