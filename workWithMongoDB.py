# MongoDB, stores user files
from pymongo import MongoClient
from config import MongoDB_Local

def connectToMongoDB():
    client = MongoClient(MongoDB_Local)

    try:
        client.admin.command("ping")
        print("✅ Connection successful")
    except Exception as e:
        print(f"❌ Error: {e}")



# db = client["newdb"]      # Создание/выбор БД
# collection = db["users"]        # Создание/выбор коллекции

# user = collection.find_one({"users": "first"})
# print(user)