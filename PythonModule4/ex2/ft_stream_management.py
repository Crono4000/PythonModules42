
import sys
import typing


def write_error(error: str) -> None:
    sys.stderr.write("[STDERR] " + error + "\n")


def read_stdinput(message: str) -> str:
    sys.stdout.write(message)
    sys.stdout.flush()
    return sys.stdin.readline().removesuffix("\n")


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
            file_name: str = read_stdinput("Enter new file name (or empty):")
            if file_name != "":
                file2: typing.IO[str] = open(file_name, "w")
                print(f"Saving data to \'{file_name}\'")
                for indice in range(len(transformed)):
                    file2.write(transformed[indice] + '\n')
                print(f"Data saved in file \'{sys.argv[1]}\'\n")
            else:
                print("Not saving data.")

        except FileNotFoundError as error:
            write_error(f"Error opening file '{error.filename}': "
                        "[Errno 2] No such file"
                        f" or directory: \'{error.filename}\'\n")
        except PermissionError as error:
            write_error(f"Error opening file '{error.filename}': "
                        "[Errno 13] Permission"
                        f" denied: \'{error.filename}\'\n")
        except NotADirectoryError as error:
            write_error(f"Error opening file '{error.filename}': "
                        f"[Errno {error.errno}]"
                        f" A component from the path should be"
                        " a folder but it's a"
                        f" file: \'{error.filename}\'\n")
        except IsADirectoryError as error:
            write_error(f"Error opening file '{error.filename}': "
                        f"[Errno {error.filename}]"
                        f" The file is a folder: "
                        f"\'{error.filename}\'\n")
        except KeyboardInterrupt:
            write_error("\nInterrompido pelo utilizador!")
        except EOFError:
            write_error("\nFim da entrada!")
