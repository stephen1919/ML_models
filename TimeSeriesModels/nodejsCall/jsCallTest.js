//// method 1 ////

// const cp = require('child_process');
// const { execSync } = cp;
// const express = require('express');
// const app = express();
// const port = 5500;

// app.use(express.json());

// const pythonScript1 = 'python ./precipTest.py'; 
// const pythonScript1 = 'python /Users/stephenshaeffer/Desktop/TimeSeriesModels/nodejsCall/precipTest.py'; 

// app.get('/graph_1', (req, res) => {
// //                    /\
// // we arent using the req parameter in our code because it is used for accessing info about the upcoming HTTP request (such as query parameters, request headers, and request body)
//   try {
//     const command = `${pythonScript1} graph_1`; 
//     const output = execSync(command).toString().trim();
//     res.send(output);
//   } catch (error) {
//     return res.status(500).json({ error: `Error executing Python script: ${error.message}` });
//   }
// });

// app.get('/ARIMA_plot', (req, res) => {
//   //                    /\
//   // we arent using the req parameter in our code because it is used for accessing info about the upcoming HTTP request (such as query parameters, request headers, and request body)
//     try {
//       const command = `${pythonScript1} ARIMA_plot`; 
//       const output = execSync(command).toString().trim();
//       // send the image path as a response
//       res.send(output);
//     } catch (error) {
//       return res.status(500).json({ error: `Error executing Python script: ${error.message}` });
//     }
//   });

// app.listen(port, () => {
//   console.log(`API server listening on http://localhost:${port}`);
// });

// app.get('/ARIMA_plot', (req, res) => {
//     try {
//         const command = `${pythonScript1} ARIMA_plot`;
//         execSync(command);

//         // Assuming the plot image is saved as 'plot.png'
//         const imagePath = '/Users/stephenshaeffer/Desktop/test123321';
//         res.sendFile(imagePath);
//     } catch (error) {
//         return res.status(500).json({ error: `Error executing Python script: ${error.message}` });
//     }
// });

// app.listen(port, () => {
//     console.log(`API server listening on http://localhost:${port}`);
// });

//// method 2 //// 

// Import necessary Plotly.js libraries
// $(document).ready(function() {
//   // Define the API address
//   const apiAddress = 'YOUR_API_ADDRESS_HERE';

//   // Function to fetch forecast data from the API
//   function fetchForecastData(callback) {
//       $.ajax({
//           url: apiAddress,
//           type: 'GET',
//           dataType: 'json',
//           success: function(data) {
//               callback(data);
//           },
//           error: function(error) {
//               console.error('Error fetching forecast data:', error);
//           }
//       });
//   }

//   // Function to display graphs using Plotly
//   function displayGraphs(forecastData) {
//       // Display graph_1
//       Plotly.newPlot('graphContainer1', [
//           {
//               x: forecastData.ds,
//               y: forecastData.yhat,
//               type: 'scatter',
//               mode: 'lines',
//               name: 'yhat'
//           }
//       ]);

//       // Display graph_2 (if applicable)
//       // You can adjust this part based on the structure of your forecast data

//       // Display graph_3 (if applicable)
//       // You can adjust this part based on the structure of your forecast data

//       // Display graph_4 (if applicable)
//       // You can adjust this part based on the structure of your forecast data
//   }

//   // Attach click event to the "Fetch Forecast Data" button
//   $('#fetchData').click(function() {
//       fetchForecastData(displayGraphs);
//   });
// });






//// how to call code with API web address ////
// http://localhost:5500/graph_1 (method 1)
// http://127.0.0.1:5001/ (method 2 (flask))
