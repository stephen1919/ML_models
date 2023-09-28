const { execSync } = require('child_process');

function callGreetMethod(name) {
  const command = `python -c "from precipitation_station1 import greet; print(greet('${name}'), end=' ')"`;

  try {
    const output = execSync(command).toString();
    console.log(output);
  } catch (error) {
    console.error(`Error executing Jupyter Notebook: ${error.message}`);
  }
}

function callAddNumbersMethod(a, b) {
  const command = `python -c "from my_module import add_numbers; print(add_numbers(${a}, ${b}), end=' ')"`;

  try {
    const output = execSync(command).toString();
    console.log(output);
  } catch (error) {
    console.error(`Error executing Jupyter Notebook: ${error.message}`);
  }
}