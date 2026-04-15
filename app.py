from flask import Flask, request, jsonify
from processor import process_data
from db import init_db, get_all_data, update_data, delete_data


app = Flask(__name__)

@app.route('/process', methods=['POST'])
def process():
    data = request.json
    result = process_data(data)
    return jsonify(result)

@app.route('/data', methods=['GET'])
def get_data():
    records = get_all_data()

    result = []
    for row in records:
        result.append({
            "id": row[0],
            "name": row[1],
            "value": row[2]
        })

    return jsonify(result)

@app.route('/update/<int:record_id>', methods=['PUT'])
def update(record_id):
    data = request.json

    if "name" not in data or "value" not in data:
        return {"status": "error", "message": "Invalid data"}

    update_data(record_id, data["name"], data["value"])

    return {"status": "success", "message": "Record updated"}

@app.route('/delete/<int:record_id>', methods=['DELETE'])
def delete(record_id):
    delete_data(record_id)

    return {
        "status": "success",
        "message": "Record deleted"
    }

init_db()

if __name__ == '__main__':
    app.run(debug=True)
