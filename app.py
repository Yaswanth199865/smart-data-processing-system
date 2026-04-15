from flask import Flask, request, jsonify
from processor import process_data
from db import init_db

app = Flask(__name__)

@app.route('/process', methods=['POST'])
def process():
    data = request.json
    result = process_data(data)
    return jsonify(result)

init_db()

if __name__ == '__main__':
    app.run(debug=True)