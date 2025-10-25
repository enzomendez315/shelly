import { createInterface } from "readline";

const rl = createInterface({
  input: process.stdin,
  output: process.stdout,
});

function run() {
  rl.question("$ ", (command) => {
    command = command.trim()

    if (command === "exit 0") {
      process.exit(0);
    }
    else if (command.startsWith("echo")) {
      const message = command.slice(4).trim();
      console.log(message);
    }
    else {
      rl.write(`${command}: command not found\n`);
    }

    run();
  });
}

run();