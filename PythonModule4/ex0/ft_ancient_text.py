
import sys
import typing


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: ft_ancient_text.py <file>\n")
    else:
        print("Accessing file \'", sys.argv[1], "\'")
        try:
            file: typing.IO[str] = open(sys.argv[1], "r")
            print("---\n")
            print(file.read())
            print("---")
            file.close()
            print(f"File \'{sys.argv[1]}\' closed.")

        except FileNotFoundError:
            print(f"Error opening file '{sys.argv[1]}': [Errno 2] No such file"
                  f" or directory: \'{sys.argv[1]}\'\n")
        except PermissionError:
            print(f"Error opening file '{sys.argv[1]}': [Errno 13] Permission"
                  f" denied: \'{sys.argv[1]}\'\n")
        except NotADirectoryError as error:
            print(f"Error opening file '{sys.argv[1]}': [Errno {error.errno}]"
                  f" A component from the path should be a folder but it's a"
                  f" file: \'{sys.argv[1]}\'\n")
        except IsADirectoryError as error:
            print(f"Error opening file '{sys.argv[1]}': [Errno {error.errno}]"
                  f" The file is a folder: "
                  f"\'{sys.argv[1]}\'\n")
