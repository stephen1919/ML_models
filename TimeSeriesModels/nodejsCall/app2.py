from flask import Flask, render_template, jsonify
import subprocess
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate_graphs')
def generate_graphs():
    # Run the Python script to generate graphs
    subprocess.run(['python', 'precipTest2.py'], cwd=os.getcwd())
    
    # Load the generated graph data
    with open('forecast_data.json', 'r') as file:
        graph_data = file.read()
    
    return jsonify(graph_data)

if __name__ == '__main__':
    app.run(debug=True)
