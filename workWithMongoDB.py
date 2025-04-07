# MongoDB, stores user files
from pymongo import MongoClient
from config import MongoDB_Local
import gridfs

def connectToMongoDB():
    client = MongoClient(MongoDB_Local)

    try:
        client.admin.command("ping")
        print("✅ Connection successful")
    except Exception as e:
        print(f"❌ Error: {e}")

def save_binary_file_to_mongodb(file_path, login, db_name="-"):
    # Подключение к MongoDB
    client = MongoClient("mongodb://localhost:27017/")
    db = client[db_name]
    fs = gridfs.GridFS(db)

    try:
        # Чтение файла в бинарном режиме
        with open(file_path, "rb") as f:
            # Сохранение файла в GridFS
            file_id = fs.put(
                f,
                filename=file_path.split("/")[-1],
                userLogin = login,
                content_type="application/octet-stream"  # Для произвольных файлов
            )
            print(f"Файл сохранён с ID: {file_id}")

    except Exception as e:
        print(f"Ошибка: {str(e)}")
    finally:
        client.close()