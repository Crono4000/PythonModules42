
def secure_archive(file: str, operation: int,
                   content: str) -> tuple[bool, str]:
    success: bool = False
    message: str = ""
    try:
        if operation == 0:
            with open(file, "w") as opened_file:
                opened_file.write(content)
            success = True
            message = "Content successfully written to file"
        elif operation == 1:
            with open(file, "r") as opened_file:
                message = opened_file.read()
        else:
            success = False
            message = "Operation not allowed"
    except FileNotFoundError as error:
        success = False
        message = (f"Error opening file '{error.filename}': [Errno 2] "
                   f"No such file or directory: \'{error.filename}\'")
    except PermissionError as error:
        success = False
        message = (f"Error opening file '{error.filename}': "
                   f"[Errno 13] Permission denied: \'{error.filename}\'")
    except NotADirectoryError as error:
        success = False
        message = f"Error opening file '{error.filename}': "
        f"[Errno {error.errno}] A component "
        "from the path should be a folder but it's a file: "
        f"\'{error.filename}\'"
    except IsADirectoryError as error:
        success = False
        message = f"Error opening file '{error.filename}': "
        f"[Errno {error.filename}] The file is a folder: "
        f"\'{error.filename}\'\n"
    return (success, message)


if __name__ == "__main__":
    print("=== Cyber Archives Security ===\n")

    print("Using 'secure_archive' to read from a nonexistent file:")
    print(secure_archive("/not/existing/file", 1, None), "\n")

    print("Using 'secure_archive' to read from an inaccessible file:")
    print(secure_archive("/etc/shadow", 1, None), "\n")

    print("Using 'secure_archive' to read from a regular file:")
    print(secure_archive("ft_vault_security.py", 1, None),
          "\n")

    print("Using 'secure_archive' to write previous content to a new file:")
    print(secure_archive("hello.txt", 0, "francesinha\n"),
          "\n")

