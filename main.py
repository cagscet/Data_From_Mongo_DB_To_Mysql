from flask import Flask, jsonify
from pymongo import MongoClient
import json
import mysql.connector
import os
from MongoDB_Connector import get_all_Data
from MySql_Connector import write_all_data

def get_mysql_connection():
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="yourPassword",
            database="YourDatabase"
        )
        print("MySQL Bağlantısı Başarılı")
        return connection

    except mysql.connector.Error as e:
        print("Hata Oluştu")
        return None

def get_mongoDB_connection():
    try:
        client = MongoClient("Your mongo url")
        db = client["database"]
        # bağlantı testş
        client.admin.command('ping')
        print("MongoDB bağlantısı başarılı")
        return db
    except Exception as e:
        print("MongoDB bağlantı hatası:", e)
        return None

def connections_db():
  mysql_conn = get_mysql_connection()
  mongoDB_conn = get_mongoDB_connection()

  if mysql_conn is not None and mongoDB_conn is not None:
      print("MongoDB ve MySQL bağlantıları başarılı")
  else: print("Bağlantılardan en az biri hatalı")

  return mysql_conn, mongoDB_conn

if __name__ == "__main__":
    mysql_conn, mongoDB_conn = connections_db()

    if mysql_conn is not None and mongoDB_conn is not None:
        # Mongo'dan veri çek
        documents = get_all_Data(mongoDB_conn, "datas")

        count = 0
        for doc in documents:
            write_all_data(mysql_conn, doc)
            count += 1

        print(f"Toplam {count} veri başarıyla yazıldı ")
