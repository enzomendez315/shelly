import sys


class Shell():
    def __init__(self):
        self.builtins = set(["exit", "echo", "type"])

    def run(self):
        sys.stdout.write("$ ")
        sys.stdout.flush()

        while True:
            command = sys.stdin.readline().strip()
            line = command.split(" ")
            
            self.handle_command(line)
            
            sys.stdout.write("$ ")
            sys.stdout.flush()

    def handle_command(self, line: list[str]):
        if not line:
            return
        
        cmd = line[0]
        args = " ".join(line[1:])

        match cmd:
            case "exit":
                sys.exit()
            case "echo":
                sys.stdout.write(f"{args}\n")
            case "type":
                self.handle_type(args)
            case _:
                sys.stdout.write(f"{cmd}: command not found\n")

    def handle_type(self, type: str):
        if type in self.builtins:
            sys.stdout.write(f"{type} is a shell builtin\n")
        else:
            sys.stdout.write(f"{type}: not found\n")