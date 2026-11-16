
import sys
import typing


if __name__ == "__main__":
    file: typing.IO[str] | None = None
    if len(sys.argv) != 2:
        print("Usage: ft_ancient_text.py <file>\n")
    else:
        print("=== Cyber Archives Recovery ===")
        print("Accessing file \'", sys.argv[1], "\'")
        try:
            file = open(sys.argv[1], "r")
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
        except Exception as error:
            print(f"{error}")
        finally:
            if file is not None:
                file.close()
