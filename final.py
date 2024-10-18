from flask import Flask, request, jsonify
from pymongo import MongoClient

app = Flask(__name__)

client = MongoClient('your_connection_string')
db = client['ghcc']
collection = db['hacktolearn']

# CREATE Operation (POST)
@app.route('/add', methods=['POST'])
def add_record():
    data = request.json
    collection.insert_one(data)
    return jsonify({
      "message": "Record added successfully!"
    }), 201

# READ Operation (GET)
@app.route('/records', methods=['GET'])
def get_records():
    records = collection.find()
    result = []
    for record in records:
        result.append({
            "name": record.get("name"),
            "age": record.get("age"),
            "cool_fact": record.get("cool_fact")
        })
    return jsonify(result), 200

# UPDATE Operation (PUT)
@app.route('/update/<name>', methods=['PUT'])
def update_record(name):
    data = request.json
    collection.update_many({"name": name}, {"$set": data})
    return jsonify({
      "message": "Record updated successfully!"
    }), 200

# DELETE Operation (DELETE)
@app.route('/delete/<name>', methods=['DELETE'])
def delete_record(name):
    collection.delete_one({"name": name})
    return jsonify({
      "message": "Record deleted successfully!"
    }), 200

if __name__ == '__main__':
    app.run(debug=True)
