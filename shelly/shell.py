import shutil
import subprocess
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
        args = line[1:]

        match cmd:
            case "exit":
                sys.exit()
            case "echo":
                sys.stdout.write(f"{" ".join(args)}\n")
            case "type":
                self.handle_type(" ".join(args))
            case _:
                if not self.handle_external(cmd, args):
                    sys.stdout.write(f"{cmd}: command not found\n")


    def handle_type(self, type: str):
        if type in self.builtins:
            sys.stdout.write(f"{type} is a shell builtin\n")
        elif path := shutil.which(type):
            sys.stdout.write(f"{type} is {path}\n")
        else:
            sys.stdout.write(f"{type}: not found\n")

    def handle_external(self, cmd, args):
        if shutil.which(cmd):
            tokens = [cmd] + args
            subprocess.run(tokens)
            return True
        
        return False