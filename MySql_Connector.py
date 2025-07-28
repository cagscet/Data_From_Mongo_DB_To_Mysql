import mysql.connector
import os
import json

def write_all_data(mysql_conn, data):
    cursor = mysql_conn.cursor()

    mongo_id = str(data.get("_id"))  # MongoDB'den gelen _id, string'e çevrilmeli
    imei = data.get("imei")
    info = data.get("INFORMATION", {})
    version = info.get("version")
    ip = info.get("IP")
    mac = info.get("mac")
    cpu_serial = info.get("cpu_serial")
    hw_version = info.get("hw_version")

    sql = """
        INSERT INTO information (id, imei, version, IP, mac, cpu_serial, hw_version)
        VALUES (%s, %s, %s, %s, %s, %s, %s)
    """

    try:
        cursor.execute(sql, (mongo_id, imei, version, ip, mac, cpu_serial, hw_version))
        mysql_conn.commit()
        print(f"Veri yazıldı: IMEI = {imei}")
    except mysql.connector.Error as err:
        print(f"Yazma hatası (IMEI={imei}):", err)
    finally:
        cursor.close()
