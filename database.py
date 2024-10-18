import pymongo
from pymongo import MongoClient

client = MongoClient('connection_string')

db = client['ghcc']

collection = db['hacktolearn']

#CREATE operation
collection.insert_one({
    "name": "YOUR_NAME",
    "age": 0, #insert your age here
    "cool_fact": "I can bend my thumb backwards and touch my wrist"
})

#READ
records = collection.find()
for record in records:
    print(record)

#UPDATE
collection.update_many({
    "name": "YOUR_NAME"  #The record you wanna change
},
{
    "$set": {
        "cool_fact": "I dont have any :(" #The change to be made
    }
})

#DELETE
collection.delete_one({
    "name": "YOUR_NAME"
})