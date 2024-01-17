import pymysql.cursors
from dotenv import load_dotenv
import os
import csv

from datetime import datetime
from dateutil.relativedelta import relativedelta


def connection_db():
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

    return connection


TABLE_TYPE = {0: 'tb_slalteloghis',
              1: 'tb_slaloraloghis',
              3: 'tb_slagsremsloghis'}


def generate_monthly_first_date_list(type, start_date, end_date):
    table_list = []
    start_date = datetime.strptime(start_date, '%Y-%m-%d').date()
    end_date = datetime.strptime(end_date, '%Y-%m-%d').date()

    current_date = start_date.replace(day=1)  # 시작 날짜의 1일로 설정

    while current_date <= end_date:
        table_list.append(
            f"{TABLE_TYPE[type]}_{current_date.strftime('%Y_%m_%d')}")
        current_date += relativedelta(months=1)  # 매월 1일로 이동

    table_list.append(f"{TABLE_TYPE[type]}")

    return table_list


def save_csv(pwr_name, modem_type, ivt_id, start_date=None, end_date=None):
    if start_date is None or end_date is None:
        data = db(modem_type, ivt_id)
    else:
        data = db(modem_type, ivt_id, start_date, end_date)

    user_name = os.getlogin()
    desktop_path = os.path.join("C:\\Users", user_name, "Desktop")
    csv_file_path = os.path.join(
        desktop_path, f"MORE_{pwr_name}_report.csv")

    timestamp = datetime.now().strftime('%Y%m%d%H%M%S')
    new_csv_file_path = os.path.join(
        desktop_path, f"{timestamp}_MORE_{pwr_name}_report.csv")

    if not data:
        print("No data to save...")
        return
    else:
        if os.path.isfile(csv_file_path):
            with open(new_csv_file_path, 'w', newline='') as csvfile:
                fieldnames = data[0].keys()
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

                writer.writeheader()

                writer.writerows(data)
        else:
            with open(csv_file_path, 'w', newline='') as csvfile:
                fieldnames = data[0].keys()
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

                writer.writeheader()

                writer.writerows(data)

    print(f"CSV 파일이 생성되었습니다 : {csv_file_path}")


def db(modem_type, ivt_id, start_date=None, end_date=None):
    connection = connection_db()

    if start_date is None or end_date is None:
        if modem_type == 1 or modem_type == 2:
            start_date = '2023-06-01'
            table_list = generate_monthly_first_date_list(
                modem_type, '2023-06-01', datetime.now().strftime('%Y-%m-%d'))
        else:
            start_date = '2023-07-01'
            table_list = generate_monthly_first_date_list(
                modem_type, start_date, datetime.now().strftime('%Y-%m-%d'))
        sql = all_day_query(modem_type, ivt_id, table_list)
    else:
        if modem_type == 1 or modem_type == 2:
            if datetime.strptime(start_date, '%Y-%m-%d') <= datetime.strptime('2023-06-01', '%Y-%m-%d'):
                start_date = '2023-06-01'
                table_list = generate_monthly_first_date_list(
                    modem_type, start_date, end_date)
            else:
                table_list = generate_monthly_first_date_list(
                    modem_type, start_date, end_date)
        else:
            if datetime.strptime(start_date, '%Y-%m-%d') <= datetime.strptime('2023-07-01', '%Y-%m-%d'):
                start_date = '2023-07-01'
                table_list = generate_monthly_first_date_list(
                    modem_type, start_date, end_date)
            else:
                table_list = generate_monthly_first_date_list(
                    modem_type, start_date, end_date)
        sql = period_query(modem_type, ivt_id, start_date,
                           end_date, table_list)

    try:
        with connection:
            with connection.cursor() as cursor:
                sql = sql
                cursor.execute(sql)
                result = cursor.fetchall()
                # print(result)
                return result
    except:
        result = "Query Faild..."
        print(result)
    return result


def all_day_query(modem_type, ivt_ids, table_list):
    ivt_ids_str = ', '.join(f"'{ivt_id}'" for ivt_id in ivt_ids)
    query = " UNION ".join(
        f"select * from {table} where IVTID in ({ivt_ids_str})" for table in table_list)

    return query


def period_query(modem_type, ivt_ids, start_date, end_date, table_list):
    ivt_ids_str = ', '.join(f"'{ivt_id}'" for ivt_id in ivt_ids)
    query = " UNION ".join(
        f"select * from {table} where IVTID in ({ivt_ids_str}) and DATE_FORMAT(EVTDATME, '%Y-%m-%d') >= DATE_FORMAT('{start_date}', '%Y-%m-%d') and DATE_FORMAT(EVTDATME, '%Y-%m-%d') <= DATE_FORMAT('{end_date}', '%Y-%m-%d')" for table in table_list)

    return query


def unt_all_query():
    connection = connection_db()

    with connection:
        with connection.cursor() as cursor:
            sql = "select UNTID, UNTNM from tb_untmstinfo"
            cursor.execute(sql)
            res = cursor.fetchall()
            # print(res)

    result_list = []

    for r in res:
        result_dict = {r['UNTID']: r['UNTNM']}
        result_list.append(result_dict)

    # print(result_list)

    return result_list


def cst_all_query(unt_id):
    connection = connection_db()

    with connection:
        with connection.cursor() as cursor:
            sql = f"select CSTID, CSTNM from tb_cstmstinfo where UNTID = '{unt_id}'"
            cursor.execute(sql)
            res = cursor.fetchall()

    result_list = []
    for r in res:
        result_dict = {r['CSTID']: r['CSTNM']}
        result_list.append(result_dict)

    return result_list


def pwr_all_query(unt_id, cst_id):
    connection = connection_db()

    with connection:
        with connection.cursor() as cursor:
            sql = f"select c.PWRID, i.PWRNM from tb_cstpwrmap as c \
                    inner join tb_pwrmstinfo as i \
                    on c.PWRID=i.PWRID \
                    where c.UNTID = '{unt_id}' and c.CSTID = '{cst_id}'"
            cursor.execute(sql)
            res = cursor.fetchall()

    result_list = []
    for r in res:
        result_dict = {r['PWRID']: r['PWRNM']}
        result_list.append(result_dict)

    # print(result_list)
    return result_list


def modem_query(pwr_id):
    connection = connection_db()

    with connection:
        with connection.cursor() as cursor:
            sql = f"select MODEMID, MODTYPE from tb_rtumodmap where RTUID in (SELECT RTUID FROM tb_pwrrtuinfo WHERE PWRID in ('{pwr_id}'))"
            cursor.execute(sql)
            res = cursor.fetchall()

    result_list = []
    for r in res:
        result_dict = {r['MODEMID']: r['MODTYPE']}
        result_list.append(result_dict)

    # print(list(result_list[0])[0])
    return result_list


def ivt_all_query(modem_id):
    connection = connection_db()

    with connection:
        with connection.cursor() as cursor:
            sql = f"select IVTID from tb_modivtmap where MODEMID in ('{modem_id}')"
            cursor.execute(sql)
            res = cursor.fetchall()

    # print(res)

    # ivt_list = [item['IVTID'] for item in res]
    # print(ivt_list)
    return res


# IVTID = ['IVT-2024011200002', 'IVT-2024011200003']

# db(1, IVTID)
# db(1, IVTID, '2022-01-01', '2024-01-14')
# unt_all_query()
# cst_all_query('0519413381')
# pwr_all_query('0519413381', 'CST-2023072500001')
# modem_query('PWR-2023072500071')
# ivt_all_query('REMS-20230724000001')


# # 입력된 날짜
# input_date = datetime(2023, 7, 11)
# print(input_date)

# # 현재 날짜
# current_date = datetime.now()
# print(current_date)

# table_list = generate_monthly_first_date_list(
#     0, input_date, current_date)

# print(table_list)

# save_csv('TEST 발전소', 1, IVTID, '2022-01-01', '2024-01-16')
