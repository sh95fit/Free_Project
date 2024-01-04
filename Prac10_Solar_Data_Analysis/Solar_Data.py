import pymysql.cursors
from dotenv import load_dotenv
import os

load_dotenv()

host = os.getenv("db_host")
user = os.getenv("db_user")
password = os.getenv("db_password")
port = os.getenv("db_port")
database = os.getenv("db_database")


connection = pymysql.connect(host=host,
                             user=user,
                             password=password,
                             database=database,
                             cursorclass=pymysql.cursors.DictCursor)

with connection:
    with connection.cursor() as cursor:
        sql = "select * from gs_regen_maindb where SERIALNO=%s"
        cursor.excute(sql, ('3030303030333538313232303835303133393434'))
        result = cursor.fetchone()
        print(result)
