
import sys

if __name__ == "__main__":
    size: int = len(sys.argv)
    print("=== Command Quest ===")
    print("Program name: ft_command_quest.py")
    print("Arguments received:", size - 1)
    indice: int = 0
    for n in sys.argv:
        if indice == 0:
            indice += 1
            continue
        print(f"Argument {indice}:", n)
        indice += 1
    if size - 1 == 0:
        print("No arguments provided!")
    print("Total arguments:", size)
    print("")
