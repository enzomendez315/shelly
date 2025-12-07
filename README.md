# 🐍 Simple Python Shell

A minimal implementation of a Unix-like shell written entirely in Python. This project provides an interactive command-line interface (CLI) with support for several built-in commands and the ability to execute external system programs via the system's `PATH`.

---

## ✨ Features

* **Interactive REPL:** Continuously reads commands, executes them, and prints results with a standard shell prompt (`$ `).
* **Core Built-ins:** Includes robust implementations for essential commands: `exit`, `echo`, `type`, `pwd`, and `cd`.
* **External Command Execution:** Executes any program found in the system's `PATH` using `subprocess.run()`.
* **Robust Parsing:** Utilizes Python's `shlex` module for accurate command-line argument splitting, handling quotes and spaces correctly.

---

## 🛠️ Project Structure

Certainly! Here is the complete README content formatted as plain text using standard Markdown for easy copying into a README.md file.

Markdown

# 🐍 Simple Python Shell

A minimal implementation of a Unix-like shell written entirely in Python. This project provides an interactive command-line interface (CLI) with support for several built-in commands and the ability to execute external system programs via the system's `PATH`.

---

## ✨ Features

* **Interactive REPL:** Continuously reads commands, executes them, and prints results with a standard shell prompt (`$ `).
* **Core Built-ins:** Includes robust implementations for essential commands: `exit`, `echo`, `type`, `pwd`, and `cd`.
* **External Command Execution:** Executes any program found in the system's `PATH` using `subprocess.run()`.
* **Robust Parsing:** Utilizes Python's `shlex` module for accurate command-line argument splitting, handling quotes and spaces correctly.

---

## 🛠️ Project Structure

The project code is organized into two files, separating the core logic from the execution entry point:

. ├── shelly/ │ └── main.py # Entry point (initializes and runs the Shell) └── shell.py # Contains the Shell class definition and all command logic


---

## 🚀 Getting Started

### 1. Requirements

You only need Python 3.x installed on your system.

### 2. Running the Shell

The entry point for the application is `shelly/main.py`. Execute this file from the project's root directory:

```bash
python shelly/main.py
```

## 🚀 Installation & Usage
To run the shell, you need to execute the entry point file, which is located at shelly/main.py.
Ensure Files are Correctly Placed: Make sure your Shell class is in shell.py and the execution logic is in shelly/main.py.
Run the Script: Execute the main file using the Python interpreter. You should run the command from the directory containing the shelly folder and the shell.py file.Bashpython shelly/main.py
Example Session
Upon starting, the shell will display a prompt ($ ):Bash$ echo Hello from the shell
Hello from the shell
$ pwd
/home/user/simple-python-shell
$ type cd
cd is a shell builtin
$ ls -a
.  ..  shell.py  shelly
$ exit
📝 Code OverviewThe shell is implemented using a single Shell class (in shell.py) to manage its state and functionality. The main() function (in shelly/main.py) serves as the basic driver for the program.File/MethodDescriptionshelly/main.pyThe main execution script. It imports the Shell class and calls shell.run().shell.py: Shell.run()The core Read-Eval-Print Loop (REPL) that continuously reads commands.shell.py: Shell.handle_command()Dispatches the command to the correct handler (built-in or external).shell.py: Shell.handle_navigation()Implements the pwd and cd built-in commands.shell.py: Shell.handle_external()Executes external programs using the subprocess module.💡 Future EnhancementsPiping and Redirection: Add support for |, >, >>, and <.Environment Variables: Support variable assignment and substitution.
