
import sys
import typing


def write_error(error: str) -> None:
    sys.stderr.write("[STDERR] " + error + "\n")


def read_stdinput(message: str) -> str:
    sys.stdout.write(message)
    sys.stdout.flush()
    return sys.stdin.readline().removesuffix("\n")


if __name__ == "__main__":
    file: typing.IO[str] | None = None
    file2: typing.IO[str] | None = None
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} <file>\n")
    else:
        print("=== Cyber Archives Recovery & Preservation ===")
        print("Accessing file \'", sys.argv[1], "\'")
        try:
            file = open(sys.argv[1], "r")
            print("---\n")
            data: str = file.read()
            print(data)
            print("---")
            file.close()
            print(f"File \'{sys.argv[1]}\' closed.")
            print("")
            print("Transform data:")
            print("---\n")
            transformed: list[str] = []
            for line in data.split("\n"):
                line += "#"
                transformed.append(line)
                print(line)
            print("---")
            file_name: str = read_stdinput("Enter new file name (or empty):")
            if file_name != "":
                file2 = open(file_name, "w")
                print(f"Saving data to \'{file_name}\'")
                for line in transformed[:(len(transformed) - 1):]:
                    file2.write(line + '\n')
                file2.write(transformed[len(transformed) - 1])
                print(f"Data saved in file \'{sys.argv[1]}\'\n")
                file2.close()
            else:
                print("Not saving data.")

        except FileNotFoundError as error:
            write_error(f"Error opening file '{error.filename}': "
                        "[Errno 2] No such file"
                        f" or directory: \'{error.filename}\'")
            print("Data not saved")
        except PermissionError as error:
            write_error(f"Error opening file '{error.filename}': "
                        "[Errno 13] Permission"
                        f" denied: \'{error.filename}\'")
            print("Data not saved")
        except NotADirectoryError as error:
            write_error(f"Error opening file '{error.filename}': "
                        f"[Errno {error.errno}]"
                        f" A component from the path should be"
                        " a folder but it's a"
                        f" file: \'{error.filename}\'")
            print("Data not saved")
        except IsADirectoryError as error:
            write_error(f"Error opening file '{error.filename}': "
                        f"[Errno {error.errno}]"
                        f" The file is a folder: "
                        f"\'{error.filename}\'")
            print("Data not saved")
        except KeyboardInterrupt:
            write_error("\nInterrompido pelo utilizador!")
        except EOFError:
            write_error("\nFim da entrada!")
        except Exception as error:
            print(f"{error}")

        finally:
            if file is not None:
                file.close()
            if file2 is not None:
                file2.close()
