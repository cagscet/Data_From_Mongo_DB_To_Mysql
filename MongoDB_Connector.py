from pymongo import MongoClient
import os
import json

def get_all_Data(mongo_db, collection_name):
    try:
        collection = mongo_db[collection_name]
        print(f"{collection_name} koleksiyonundan veriler çekiliyor...")
        data = list(collection.find())
        print(f"{len(data)} adet veri çekildi.")
        return data
    except Exception as e:
        print("MongoDB'den veri çekerken hata oluştu:", e)
        return []

