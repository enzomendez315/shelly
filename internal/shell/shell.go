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

		parts := strings.Split(strings.TrimSpace(command), " ")
		cmd := parts[0]

		switch cmd {
		case "exit":
			os.Exit(0)
		case "echo":
			fmt.Println(strings.Join(parts[1:], " "))
		case "":
			continue
		default:
			fmt.Println(cmd + ": command not found")
		}
	}
}
