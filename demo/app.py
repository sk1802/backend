from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Initial data for the table entries
data = {
    1: {'name': 'John', 'age': 30},
    2: {'name': 'Jane', 'age': 25},
    3: {'name': 'Doe', 'age': 40},
}

@app.route('/api/add', methods=['POST'])
def add_data():
    req_data = request.json
    print(req_data)
    component_key = req_data.get('component_key')
    print(component_key[-1])
    print(data)
    print(type(component_key[-1]))
    # Clear out previous data
    # data.pop(int(component_key[-1]), None)
    # Add new data
    for key, value in req_data['data'].items():
        data[int(component_key[-1])][key] = value

    return jsonify(data[int(component_key[-1])]), 201

@app.route('/api/update', methods=['POST'])
def update_data():
    req_data = request.json
    component_key = req_data.get('component_key')
    # Update existing data
    for key, value in req_data['data'].items():
        if int(key) in data:
            data[int(component_key[-1])][key] = value
    return jsonify(data[int(component_key[-1])]), 200

@app.route('/api/count', methods=['GET'])
def get_counts():
    return jsonify({'message': 'Counts are not tracked in this version.'})


@app.route('/')
def index():
    return 'Hello, World!'
if __name__ == '__main__':
    app.run(debug=False)
