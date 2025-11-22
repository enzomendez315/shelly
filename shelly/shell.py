import os
import shutil
import subprocess
import sys


class Shell():
    def __init__(self):
        self.builtins = set(["exit", "echo", "type", "pwd", "cd"])

    def run(self):
        """Starts the interactive shell REPL.

        Continuously reads commands from stdin and executes 
        them until the user exits the shell.
        """
        sys.stdout.write("$ ")
        sys.stdout.flush()

        while True:
            command = sys.stdin.readline().strip()
            line = command.split(" ")
            
            self.handle_command(line)
            
            sys.stdout.write("$ ")
            sys.stdout.flush()

    def handle_command(self, line: list[str]):
        """Executes a single command from the user.

        Processes the input line, determines the appropriate action, 
        and executes built-in or external commands. Can be extended 
        to support additional functionality in the future.
        """
        if not line:
            return
        
        cmd = line[0]
        args = line[1:]

        match cmd:
            case "exit":
                sys.exit()
            case "echo":
                self.handle_echo(args)
            case "type":
                self.handle_type(args)
            case "pwd" | "cd":
                self.handle_navigation(cmd, args)
            case _:
                if not self.handle_external(cmd, args):
                    sys.stdout.write(f"{cmd}: command not found\n")

    def handle_echo(self, args: list[str]):
        sys.stdout.write(f"{" ".join(args)}\n")

    def handle_type(self, args: list[str]):
        """Checks the type of a command.

        Determines whether the given name corresponds to a shell 
        builtin, an external executable, or is not found.
        """
        type = " ".join(args)
        if type in self.builtins:
            sys.stdout.write(f"{type} is a shell builtin\n")
        elif path := shutil.which(type):
            sys.stdout.write(f"{type} is {path}\n")
        else:
            sys.stdout.write(f"{type}: not found\n")

    def handle_external(self, cmd: str, args: list[str]):
        """Attempts to execute an external command.

        Runs the specified command with the provided arguments if it 
        exists on the system. Returns True if executed successfully, 
        False otherwise.
        """
        if shutil.which(cmd):
            tokens = [cmd] + args
            subprocess.run(tokens)
            return True
        
        return False
    
    def handle_navigation(self, cmd: str, args: list[str]):
        if cmd == "pwd":
            sys.stdout.write(f"{os.getcwd()}\n")
        else:
            if len(args) > 1:
                sys.stdout.write(f"{cmd}: too many arguments\n")
                return
            
            if len(args) == 1:
                path = args[0]
                if path == "~":
                    path = os.getenv("HOME")
            else:
                path = os.getenv("HOME")
            
            try:
                os.chdir(path)
            except FileNotFoundError:
                sys.stdout.write(f"{cmd}: {args[0]}: No such file or directory\n")