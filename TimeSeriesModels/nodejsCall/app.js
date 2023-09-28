//// method 1 ////
// // app.js
// const { PythonShell } = require('python-shell');

// // Specify the path to your Python script
// const pythonScriptPath = '/Users/stephenshaeffer/Desktop/TimeSeriesModels/nodejsCall/my_module.py';

// // Function to call the greet() method from the Python file
// function callGreetMethod(name) {
//   // Provide the path to the Python script
//   let pyshell = new PythonShell(pythonScriptPath);

//   // Call the greet() method with the provided name as an argument
//   pyshell.send('from my_module import greet\ngreeting = greet("' + name + '")');

//   // Receive the output from the Python script
//   pyshell.on('message', function (message) {
//     console.log(message); // Output the result to the console
//   });

//   // Handle errors, if any
//   pyshell.on('error', function (error) {
//     console.error(error);
//   });
// }

// // Function to call the add_numbers() method from the Python file
// function callAddNumbersMethod(a, b) {
//     // Provide the path to the Python script
//     let pyshell = new PythonShell(pythonScriptPath);
  
//     // Call the add_numbers() method with the provided numbers as arguments
//     pyshell.send('from my_module import add_numbers\nresult = add_numbers(' + a + ', ' + b + ')');
  
//     // Receive the output from the Python script
//     pyshell.on('message', function (message) {
//       console.log(message); // Output the result to the console
//     });
  
//     // Handle errors, if any
//     pyshell.on('error', function (error) {
//       console.error(error);
//     });
//   }

// callGreetMethod('Alice');
// callAddNumbersMethod(5, 7);

//// method 2 ////
const { execSync } = require('child_process');

function callPythonFunction(moduleName, functionName, args) {
  try {
    const pythonScript = `
      import sys
      import ${moduleName}

      result = ${moduleName}.${functionName}(*${JSON.stringify(args)})
      sys.stdout.write(str(result))
    `;

    const command = `python -c "${pythonScript}"`;
    const output = execSync(command);

    return output.toString().trim();
  } catch (error) {
    throw new Error(`Failed to call Python function: ${error.message}`);
  }
}

module.exports = {
  callPythonFunction,
};