import pymysql.cursors
from dotenv import load_dotenv
import os


def db():
    load_dotenv()

    host = os.getenv("db_host")
    user = os.getenv("db_user")
    password = os.getenv("db_password")
    port = int(os.getenv("db_port"))
    database = os.getenv("db_database")

    connection = pymysql.connect(host=host,
                                 user=user,
                                 password=password,
                                 database=database,
                                 port=port,
                                 cursorclass=pymysql.cursors.DictCursor)

    with connection:
        with connection.cursor() as cursor:
            sql = "select * from tb_slalteloghis where SERIALNO=%s"
            cursor.execute(sql, ('3030303030333538313232303835303133393434'))
            result = cursor.fetchone()
            print(result)

    return result


db()
