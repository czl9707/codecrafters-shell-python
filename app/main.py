import sys

def cmd_handler(cmd: str) -> None:
    tokens = [t for t in cmd.split(" ") if len(t) > 0]
    if not tokens:
        return
    
    command = tokens[0]
    match command:
        case "exit":
            code = int(tokens[1]) if len(tokens) > 1 else 0
            exit(code)
        case "echo":
            msg = cmd[4:].strip()
            sys.stdout.write(msg)
            sys.stdout.write("\n")
            sys.stdout.flush()            
        case _:
            sys.stdout.write(f"{command}: command not found\n")
            sys.stdout.flush()
        
def main():
    # Uncomment this block to pass the first stage
    while True:
        sys.stdout.write("$ ")
        sys.stdout.flush()

        # Wait for user input
        cmd = input()
        cmd_handler(cmd)


if __name__ == "__main__":
    main()
