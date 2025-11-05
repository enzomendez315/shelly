package main

import (
	"fmt"
	"os"
	"shelly/internal/shell"
)

func main() {
	if err := shell.Run(); err != nil {
		fmt.Fprintln(os.Stderr, "Shell error:", err)
		os.Exit(1)
	}
}
