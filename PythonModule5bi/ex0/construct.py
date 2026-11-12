
import sys


if __name__ == "__main__":
    is_venv: bool = (sys.prefix == sys.base_prefix)
    if is_venv:
        print("\nLABORATORY STATUS: You are working in the open\n\n")
        print("Current Python:", sys.executable)
        print("Virtual Environment: None detected")
        print("")
        print("WARNING: You are in the global environment!")
        print("Every reagent you install here leaks into the whole system.")
        print("")
        print("To seal the laboratory, run:")
        print("python3 -m venv lab_env")
        print("source lab_env/bin/activate # On Unix")
        print("lab_env\Scripts\activate # On Windows")
        print("")
        print("Then run this program again.")
        print("")
    else:
