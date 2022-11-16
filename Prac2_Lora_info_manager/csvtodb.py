import csv
import os
import sqlite3
from Path import DB_path, CSV_path

class Loading :
    def csvtodb() : 
        list = []

        if os.path.exists(CSV_path) :
            print("데이터 업로드 중 ...")
            file = open(CSV_path, "r", encoding="UTF-8-SIG")
            reader = csv.reader(file)
            for data in reader :
                list.append(data)
            conn = sqlite3.connect(DB_path)
            cursor = conn.cursor()
            sql = "SELECT DEV_ID FROM Lora_info"
            cursor.execute(sql)
            if not cursor.fetchone() :
                sql = "INSERT INTO Lora_info(DEV_NAME, DEV_EUI, DEV_APP_KEY, DEV_APP_EUI) VALUES(?, ?, ?, ?)"
                for data in list[1:] :
                    cursor.execute(sql, (data[1], data[2], data[3], data[4]))
                conn.commit()
                conn.close()
                file.close()
        else :
            file = open(CSV_path, "w", encoding = "UTF-8", newline="")
            file.close()