
import sys
import typing


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: ft_ancient_text.py <file>\n")
    else:
        print("=== Cyber Archives Recovery & Preservation ===")
        print("Accessing file \'", sys.argv[1], "\'")
        try:
            file: typing.IO[str] = open(sys.argv[1], "r")
            print("---\n")
            data: str = file.read()
            print(data)
            print("---")
            file.close()
            print(f"File \'{sys.argv[1]}\' closed.")
            print("")
            print("Transform data:")
            print("---\n")
            transformed: list[str] = data.split("\n")
            for indice in range(len(transformed)):
                transformed[indice] += "#"
                print(transformed[indice])
            print("---")
            file_name: str = input("Enter new file name (or empty):")
            if file_name != "":
                file2: typing.IO[str] = open(file_name, "w")
                print(f"Saving data to \'{file_name}\'")
                for indice in range(len(transformed)):
                    file2.write(transformed[indice] + '\n')
                print(f"Data saved in file \'{sys.argv[1]}\'\n")
            else:
                print("Not saving data.")

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
        except KeyboardInterrupt:
            print("\nInterrompido pelo utilizador!")
        except EOFError:
            print("\nFim da entrada!")
