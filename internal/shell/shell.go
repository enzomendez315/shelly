package shell

import (
	"bufio"
	"fmt"
	"os"
	"strings"
)

func Run() error {
	reader := bufio.NewReader(os.Stdin)

	for {
		fmt.Fprint(os.Stdout, "$ ")

		command, err := reader.ReadString('\n')
		if err != nil {
			return fmt.Errorf("error reading input: %w", err)
		}

		parts := strings.Fields(command)
		if err := handleCommand(parts); err != nil {
			return fmt.Errorf("error parsing command: %w", err)
		}
	}
}

func handleCommand(parts []string) error {
	if len(parts) == 0 {
		return nil
	}

	cmd := parts[0]
	args := parts[1:]

	switch cmd {
	case "exit":
		os.Exit(0)
	case "echo":
		fmt.Println(strings.Join(args, " "))
	default:
		fmt.Println(cmd + ": command not found")
	}

	return nil
}
