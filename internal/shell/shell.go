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

		command = strings.TrimSpace(command)

		if command == "exit" {
			os.Exit(0)
		}

		fmt.Println(command + ": command not found")
	}
}
