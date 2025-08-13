from pymongo import MongoClient
from config import Config

# 1. Connect to MongoDB
client = MongoClient(Config.MONGODB_URI)  # For local MongoDB
# Example for cloud: "mongodb+srv://username:password@cluster.mongodb.net/"

# 2. Choose the database
db = client["ecommerce"]

# 3. Choose the collection
collection = db["users"]

#result = collection.delete_many({})

#print(f"{result.deleted_count} documents deleted.")

# 4. Fetch and print all documents
for document in collection.find():
    print(document)
