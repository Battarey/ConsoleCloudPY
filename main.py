# import functions as f
# f.enterLoginAndPassword()


# Разработать функцию для закачки файлов в Mongo

# from workWithMongoDB import connectToMongoDB
# connectToMongoDB()


# db = client["newdb"]      # Создание/выбор БД
# collection = db["users"]        # Создание/выбор коллекции

# user = collection.find_one({"users": "first"})
# print(user)









# def get_binary_file(file_id, save_path, db_name="-"):
#     client = MongoClient("mongodb://localhost:27017/")
#     db = client[db_name]
#     fs = gridfs.GridFS(db)

#     with open(save_path, "wb") as f:
#         f.write(fs.get(file_id).read())

# # Пример использования
# # login = 'Vasya'
# # save_binary_file_to_mongodb("image.jpg", login)

# get_binary_file('67f3fc2c43d734010895f6b0')










from pymongo import MongoClient
import gridfs

def download_image_from_mongodb():
    # Подключение к MongoDB и выбор базы данных
    client = MongoClient("mongodb://localhost:27017/")
    db = client["newdb"]  # Используем базу данных newdb
    
    # Инициализация GridFS
    fs = gridfs.GridFS(db)

    try:
        # Поиск файла по имени
        file_data = fs.find_one({"filename": "image.jpg"})
        
        if file_data:
            # Сохранение файла на диск
            with open("downloaded_image.jpg", "wb") as f:
                f.write(file_data.read())
            print("Файл успешно выгружен и сохранён как 'downloaded_image.jpg'")
        else:
            print("Файл 'image.jpg' не найден в базе данных")

    except Exception as e:
        print(f"Ошибка: {str(e)}")
    finally:
        client.close()

# Запуск функции выгрузки
download_image_from_mongodb()