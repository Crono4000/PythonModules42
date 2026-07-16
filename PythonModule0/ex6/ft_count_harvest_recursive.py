
def recursive_days(day: int, final: int):
    print("day", day)
    if day == final:
        return
    recursive_days(day + 1, final)


def ft_count_harvest_recursive():
    days: int = int(input("Days until harvest: "))
    recursive_days(1, days)
    print("Harvest time!")
