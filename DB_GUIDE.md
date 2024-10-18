# MongoDB Atlas Setup and CRUD Operations with PyMongo

## 1. MongoDB Atlas Setup
To get started with MongoDB Atlas, follow these steps:

1. **Create a MongoDB Atlas Account**
   - Go to [MongoDB Atlas](https://www.mongodb.com/cloud/atlas).
   - Sign up for an account if you don't have one.

2. **Create a New Cluster**
   - After logging in, click on "Build a Cluster."
   - Choose your preferred cloud provider and region.
   - Click "Create Cluster" to set it up.

3. **Configure Database Access**
   - Go to the "Database Access" tab.
   - Click "Add New Database User."
   - Create a user with appropriate permissions (e.g., read and write).

4. **Configure Network Access**
   - Go to the "Network Access" tab.
   - Click "Add IP Address."
   - Allow access from your current IP or set it to allow access from anywhere (0.0.0.0/0) for development purposes.

5. **Get Connection String**
   - Navigate to your cluster and click "Connect."
   - Choose "Connect your application."
   - Copy the provided connection string (replace `<password>` with your user password).

## 2. Installing PyMongo
To install PyMongo, use pip:

```bash
pip install pymongo
```

## CONNECT TO MONDODB ATLAS

```python
import pymongo
from pymongo import MongoClient

client = MongoClient('your_connection_string')

db = client['ghcc']
collection = db['hacktolearn']
```

## CRUD Operations

### CREATE Operation
To insert a new document into your collection:

```python
collection.insert_one({
    "name": "YOUR_NAME",
    "age": 0,  # insert your age here
    "cool_fact": "I can bend my thumb backwards and touch my wrist"
})
```

### READ Operation
To read a new document from your collection:

```python
records = collection.find()
for record in records:
    print(record)
```

### UPDATE Operation
To update a document from your collection:

```python
collection.update_many({
    "name": "YOUR_NAME"  #The record you wanna change
},
{
    "$set": {
        "cool_fact": "I dont have any :(" #The change to be made
    }
})
```

### DELETE Operation
To delete a new document from your collection:

```python
collection.delete_one({
    "name": "YOUR_NAME"
})
```

Got it! Here’s an addition to your existing markdown that includes CRUD operation snippets within a basic Flask app structure, mirroring the format you provided for the PyMongo operations.

---

## 3. Basic Flask App with CRUD Operations

You can integrate the CRUD operations into a Flask app as follows:

### Flask App Setup

First, ensure you have Flask and PyMongo installed:

```bash
pip install Flask pymongo
```

Then, create a basic Flask application with the following structure:

```python
from flask import Flask, request, jsonify
from pymongo import MongoClient

app = Flask(__name__)

# Connect to MongoDB Atlas
client = MongoClient('your_connection_string')
db = client['ghcc']
collection = db['hacktolearn']
```

### Running the Flask App
To run your Flask application, add the following code at the end of your `app.py`:

```python
if __name__ == '__main__':
    app.run(debug=True)
```

### CREATE Operation (POST)
To add a new document using a POST request:

```python
@app.route('/add', methods=['POST'])
def add_record():
    data = request.json
    collection.insert_one(data)
    return jsonify({"message": "Record added successfully!"}), 201
```

### READ Operation (GET)
To retrieve documents using a GET request:

```python
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
```

### UPDATE Operation (PUT)
To update an existing document using a PUT request:

```python
@app.route('/update/<name>', methods=['PUT'])
def update_record(name):
    data = request.json
    collection.update_many({"name": name}, {"$set": data})
    return jsonify({"message": "Record updated successfully!"}), 200
```

### DELETE Operation (DELETE)
To delete a document using a DELETE request:

```python
@app.route('/delete/<name>', methods=['DELETE'])
def delete_record(name):
    collection.delete_one({"name": name})
    return jsonify({"message": "Record deleted successfully!"}), 200
```
