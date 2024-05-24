import sys

def cmd_handler(cmd: str) -> None:
    command = cmd.split(" ")[0]
    sys.stdout.write(f"{command}: command not found")
    sys.stdout.flush()

def main():
    # Uncomment this block to pass the first stage
    sys.stdout.write("$ ")
    sys.stdout.flush()

    # Wait for user input
    cmd = input()
    cmd_handler(cmd)


if __name__ == "__main__":
    main()
