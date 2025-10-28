import { createInterface } from 'readline';

const rl = createInterface({
  input: process.stdin,
  output: process.stdout,
});

function run() {
  rl.question('$ ', (command: string) => {
    command = command.trim();
    const [cmd, ...args] = command.split(/\s+/);

    switch(cmd) {
      case 'exit':
        if (args[0] === '0') process.exit(0);
        else console.log('Usage: exit 0');
        break;
      case 'echo':
        const message = args.join(' ');
        console.log(message);
        break;
      case 'type':
        const target = args[0];
        const builtins = ['exit', 'echo', 'type'];
        if (builtins.includes(target)) {
          console.log(`${target} is a shell builtin`);
        } else {
          console.log(`${target || command}: not found`)
        }
        break;
      default:
        console.log(`${command}: command not found`);
    }

    run();
  });
}

run();