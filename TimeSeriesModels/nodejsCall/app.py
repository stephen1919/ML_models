from flask import Flask, render_template, jsonify, request, Response
import subprocess
import os
import json  
import traceback

app = Flask(__name__)
#      /\      /\
#      |       |    
#      |    special python variable that is set to the 
#      |    name of the current module (app.py) 
#   the class provided by the flask library 
@app.route('/', methods=["GET", "POST"]) # a decorator provided by the flask frame work, its placed above a function definition to specify that the function will handle requests to a particular URL route.
#           /\
#           This is the URL route that we're 
#           associating with the decorated function. 
def index():# this funciton is associated with the root route ("/")
    return render_template('index.html')
#               /\              /\
#               |               name of the HTML template file we want to render
#               |
#              used to render an HTML template

@app.route('/generate_graphs', methods=["GET", "POST"])
#                   /\
#                   the URL route that the decorator is 
#                   associating with the view function that follows it
def generate_graphs():
    timeframe = request.args.get('timeframe')  # Get the requested timeframe from the query parameter

    # Load the appropriate forecast data based on the timeframe
    if timeframe == 'day':
        filename = 'forecast_data_day.json'
    elif timeframe == 'week':
        filename = 'forecast_data_week.json'
    elif timeframe == '2week':
        filename = 'forecast_data_2week.json'
    else:
        return jsonify({'error': 'Invalid timeframe'})
# Checking if the json data is good with a try catch
    try:
        with open(filename, 'r') as file:
            graph_data = json.load(file)
    except Exception as e:
        traceback.print_exc()  # Print the traceback in case of an exception
        return jsonify({'error': 'Error loading data'})

    # Load the forecast data from the file
    with open(filename, 'r') as file:
        graph_data = json.load(file)

    # print("Graph data:", graph_data)  # Add this line to print the graph_data
# Checking the server response
    response = jsonify(graph_data)
    response.headers['Content-Type'] = 'application/json'
    return response

# app.run(debug=True)
if __name__ == '__main__':
    app.run(debug=True, port=5001)
