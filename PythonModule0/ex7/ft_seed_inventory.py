
def ft_seed_inventory(seed_type: str, quantity: int, unit: str) -> None:
    seed: str = seed_type.capitalize()
    if unit == "grams":
        print(seed, "seeds:", quantity, "grams total")
    elif unit == "area":
        print(seed, "seeds: covers", quantity, "square meters")
    elif unit == "packets":
        print(seed, "seeds:", quantity, "packets available")
    else:
        print("Unknown unit type")
