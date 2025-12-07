# Shelly

A minimal Python-based shell implementation featuring a simple REPL, built-in commands, and external command execution. This project consists of two files — `main.py` and `shell.py` — within the `shelly/` directory.

## Features

Shelly currently supports:

* **Interactive REPL** prompting with `$`.
* **Built-in commands:**

  * `exit` — Exit the shell.
  * `echo` — Print text.
  * `type` — Display whether a command is built-in or an external executable.
  * `pwd` — Print current working directory.
  * `cd` — Change directories.
* **External command execution** using your system's `$PATH`.
* **Basic shell parsing** via Python's `shlex`.

## Project Structure

```
shelly/
├── main.py
└── shell.py
```

### `main.py`

Entry point for the shell. Creates a `Shell` instance and starts the REPL.

### `shell.py`

Contains the `Shell` class implementing all built-in commands, parsing logic, directory navigation, and invocation of external commands.

## Installation

Clone the repository:

```
git clone https://github.com/enzomendez315/shelly.git
cd shelly
```

(Optional) Create and activate a virtual environment:

```
python3 -m venv venv
source venv/bin/activate
```

No external dependencies are required — Shelly uses only Python standard library modules.

## Usage

Run the shell with:

```
python3 main.py
```

You'll see the prompt:

```
$
```

Then you can begin entering commands.

### Examples

```
$ echo hello world
hello world

$ pwd
/Users/enzo/projects/shelly

$ cd ~
$ pwd
/Users/enzo

$ type echo
echo is a shell builtin

$ ls
# (system ls output)
```

## Code Overview

### REPL Loop

* Reads input from stdin.
* Parses with `shlex.split()`.
* Dispatches to built-in handlers or external commands.

### Built-in Command Handlers

* **Echo:** Joins arguments with a space.
* **Type:** Checks against the built-in set or system `PATH`.
* **pwd/cd:** Uses `os.getcwd()` and `os.chdir()`.

### External Commands

Executed using `subprocess.run()` only if found via `shutil.which()`.

## Roadmap / Ideas

Potential future improvements:

* Support for pipes (`|`)
* Environment variables
* Command history
* Redirects (`>`, `<`)
* Background execution (`&`)
* Better error messages and exit codes

## Contributing

Pull requests are welcome! Feel free to open issues for bugs, suggestions, or enhancements.

## License

MIT License. Feel free to use and modify Shelly as you wish.
