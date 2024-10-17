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

```
import pymongo
from pymongo import MongoClient

client = MongoClient('your_connection_string')

db = client['ghcc']
collection = db['hacktolearn']
```

## CRUD Operations

### CREATE Operation
To insert a new document into your collection:

```
collection.insert_one({
    "name": "YOUR_NAME",
    "age": 0,  # insert your age here
    "cool_fact": "I can bend my thumb backwards and touch my wrist"
})
```

### READ Operation
To read a new document from your collection:

```
records = collection.find()
for record in records:
    print(record)
```

### UPDATE Operation
To update a document from your collection:

```
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

```
collection.delete_one({
    "name": "YOUR_NAME"
})
```
