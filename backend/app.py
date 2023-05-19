from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "http://localhost:8080"}})

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/example_endpoint', methods=['POST'])
def example_endpoint():
    data = request.get_json()
    print(data)
    # perform your operations with the data
    return jsonify({'status': 'success'}), 200

if __name__ == '__main__':
    app.run(port=5000)
