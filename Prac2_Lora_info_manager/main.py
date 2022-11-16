'''
# Lora DB테이블에 장비 정보 입력, 수정, 삭제, 조회 프로그램 만들기
---------------------------------
1.입력 2.수정 3.삭제 4.조회 0.종료
'''

import sqlite3
from csvtodb import Loading
from Path import DB_path, CSV_path

def create() :
    conn = sqlite3.connect(DB_path)
    cursor = conn.cursor()
    dev_name = input("모뎀 이름 >>> ")
    dev_eui = input("DEV EUI >>> ")
    dev_app_key = input("DEV APP KEY >>> ")
    dev_app_eui = input("DEV_APP_EUI >>> ")
    sql = "INSERT INTO Lora_info(DEV_NAME, DEV_EUI, DEV_APP_KEY, DEV_APP_EUI) VALUES(?, ?, ?, ?)"
    cursor.execute(sql, (dev_name, dev_eui, dev_app_key, dev_app_eui))
    conn.commit()
    conn.close()
    print("디바이스 등록이 완료되었습니다.")


def update() :
    while True :
        post = []
        conn = sqlite3.connect(DB_path)
        cursor = conn.cursor()
        sql = "SELECT DEV_ID FROM Lora_info"
        cursor.execute(sql)
        for row in cursor.fetchall() :
            post.append(row[0])
        print("어떤 디바이스 내용을 수정하시겠습니까? (디바이스 넘버 입력, 0. 돌아가기)")
        dev_num = int(input(">>> "))
        if dev_num == 0 :
            break
        elif dev_num not in post :
            print("선택한 디바이스가 존재하지 않습니다.")
        else :
            print("어떤 항목을 수정하시겠습니까?")
            print("1.전체 2.DEV_NAME 3.DEV_EUI 4.DEV_APP_KEY 5.DEV_APP_EUI 0.돌아가기")
            try :
                select = int(input(">>> "))
                if select == 0 :
                    break
                elif select == 1 :
                    conn = sqlite3.connect(DB_path)
                    cursor = conn.cursor()
                    dev_name = input("모뎀 이름 >>> ")
                    dev_eui = input("DEV EUI >>> ")
                    dev_app_key = input("DEV APP KEY >>> ")
                    dev_app_eui = input("DEV_APP_EUI >>> ")
                    sql = "UPDATE Lora_info SET DEV_NAME = ?, DEV_EUI = ?, DEV_APP_KEY = ?, DEV_APP_EUI = ? WHERE DEV_ID= ?"
                    cursor.execute(sql, (dev_name, dev_eui, dev_app_key, dev_app_eui, dev_num))
                    conn.commit()
                    conn.close()
                    break
                elif select == 2 :
                    conn = sqlite3.connect(DB_path)
                    cursor = conn.cursor()
                    dev_name = input("모뎀 이름 >>> ")
                    sql = "UPDATE Lora_info SET DEV_NAME = ? WHERE DEV_ID= ?"
                    cursor.execute(sql, (dev_name, dev_num))
                    conn.commit()
                    conn.close()
                    break
                elif select == 3 :
                    conn = sqlite3.connect(DB_path)
                    cursor = conn.cursor()
                    dev_eui = input("DEV EUI >>> ")
                    sql = "UPDATE Lora_info SET DEV_EUI = ? WHERE DEV_ID= ?"
                    cursor.execute(sql, (dev_eui, dev_num))
                    conn.commit()
                    conn.close()
                    break
                elif select == 4 :
                    conn = sqlite3.connect(DB_path)
                    cursor = conn.cursor()
                    dev_app_key = input("DEV APP KEY >>> ")
                    sql = "UPDATE Lora_info SET DEV_APP_KEY = ? WHERE DEV_ID= ?"
                    cursor.execute(sql, (dev_app_key, dev_num))
                    conn.commit()
                    conn.close()
                    break
                elif select == 5 :
                    conn = sqlite3.connect(DB_path)
                    cursor = conn.cursor()
                    dev_app_eui = input("DEV_APP_EUI >>> ")
                    sql = "UPDATE Lora_info SET DEV_APP_EUI = ? WHERE DEV_ID= ?"
                    cursor.execute(sql, (dev_app_eui, dev_num))
                    conn.commit()
                    conn.close()
                    break         
            except ValueError :
                print("해당하는 항목이 없습니다.")

def delete() :
    while True :
        print("디바이스 삭제 방식을 선택하세요.")
        print("1.전체 2.선택 0.돌아가기")
        select = int(input(">>> "))
        if select == 0 :
            break
        elif select == 1 :
            while True :
                cnt = 0
                print("정말 디바이스 전체 정보를 삭제하시겠습니까?")
                choice = int(input("1.네 2.아니오\n>>> "))
                if choice == 1 :
                    conn = sqlite3.connect(DB_path)
                    cursor = conn.cursor()
                    sql = "DELETE FROM Lora_info"
                    cursor.execute(sql)
                    conn.commit()
                    conn.close()
                    cnt += 1
                    break
                elif choice == 2 :
                    break
                else :
                    print("1번과 2번 조건 중 선택해주세요.")
            if cnt == 1 :
                break
        elif select == 2 :
            print("어떤 디바이스 내용을 삭제하시겠습니까? (디바이스 넘버 입력, 0. 돌아가기)")
            try :    
                dev_num = int(input(">>> "))
                if dev_num == 0 :
                    break
                conn = sqlite3.connect(DB_path)
                cursor = conn.cursor()
                sql = "DELETE FROM Lora_info WHERE DEV_ID = ?"
                cursor.execute(sql, (dev_num, ))
                conn.commit()
                conn.close()
                break
            except ValueError :
                print("선택하신 디바이스 항목이 없습니다.")
        else :
            print("선택한 항목이 존재하지 않습니다.")

def select() :
    while True :
        print("디바이스 정보 조회 방식을 선택하세요.")
        print("1.전체 2.선택 0.돌아가기")
        try :
            choice = int(input(">>> "))
            if choice == 0 :
                break
            elif choice == 1 :        
                conn = sqlite3.connect(DB_path)
                cursor = conn.cursor()
                sql = "SELECT * FROM Lora_info"
                cursor.execute(sql)
                for row in cursor.fetchall() :
                    print("%s %s %s %s %s"%(row[0], row[1], row[2], row[3], row[4]))
                cursor.close()
                break
            elif choice == 2 :
                while True :
                    cnt = 0
                    post = []
                    print("디바이스 장비 번호를 입력하세요.")
                    dev_num = int(input(">>> "))
                    conn = sqlite3.connect(DB_path)
                    cursor = conn.cursor()
                    sql = "SELECT * FROM Lora_info"
                    cursor.execute(sql)
                    for row in cursor.fetchall() :
                        post.append(row[0])
                    if dev_num in post :
                        sql = "SELECT * FROM Lora_info WHERE DEV_ID = ?"
                        cursor.execute(sql, (dev_num, ))
                        for row in cursor.fetchall() :
                            print("%d %s %s %s %s"%(row[0], row[1], row[2], row[3], row[4]))
                        cursor.close()
                        cnt += 1
                        break 
                    else :
                        print("선택한 디바이스가 존재하지 않습니다.")
                if cnt == 1 :
                    break
        except ValueError :
            print("선택한 항목이 존재하지 않습니다!")


Loading.csvtodb()

while True :
    print("-----Lora 정보 관리 프로그램------")
    print("1.입력 2.수정 3.삭제 4.조회 0.종료")
    try :
        sel = int(input("항목을 선택하세요. >>> "))
        if sel == 1 : 
            create()
        elif sel == 2 :
            update()
        elif sel == 3 :
            delete()
        elif sel == 4 :
            select()
        elif sel == 0 :
            break
    except ValueError :
        print("선택한 항목이 존재하지 않습니다!")