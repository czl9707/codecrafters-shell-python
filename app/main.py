import os
import pathlib
import sys
from typing import Optional

def find_path_executable(exe: str) -> Optional[str]:
    paths = (pathlib.Path(p) for p in os.environ["PATH"].split(":"))
    
    for path in paths:
        if path.exists() and  exe in os.listdir(path):
            return str(path.joinpath(exe))

    return None
        
        
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
        case "type":
            tgt_command = tokens[1]
            if tgt_command in ("type", "echo", "exit"):
                sys.stdout.write(f"{tgt_command} is a shell builtin")
            elif full_path := find_path_executable(tgt_command):
                sys.stdout.write(f"{tgt_command} is {full_path}")
            else:
                sys.stdout.write(f"{tgt_command} not found")
                
            sys.stdout.write("\n")
            sys.stdout.flush()                
        case _:
            if full_path := find_path_executable(command):
                os.system(cmd)
                return
            
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
