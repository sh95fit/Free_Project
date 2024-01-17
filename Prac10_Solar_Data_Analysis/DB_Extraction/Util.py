import pymysql.cursors
from dotenv import load_dotenv
import os

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
              2: 'tb_slagsremsloghis'}


def generate_monthly_first_date_list(type, start_date, end_date):
    table_list = []
    current_date = start_date.replace(day=1)  # 시작 날짜의 1일로 설정

    while current_date <= end_date:
        table_list.append(
            f"{table_type[type]}_{current_date.strftime('%Y_%m_%d')}")
        current_date += relativedelta(months=1)  # 매월 1일로 이동

    table_list.append(f"{table_type[type]}")

    return table_list


def db(modem_type, ivt_id, start_date=None, end_date=None):
    connection = connection_db()

    if start_date is None or end_date is None:
        sql = all_day_query(modem_type, ivt_id)
    else:
        sql = period_query(modem_type, ivt_id, start_date, end_date)

    with connection:
        with connection.cursor() as cursor:
            sql = sql
            cursor.execute(sql)
            result = cursor.fetchall()
            print(result)

    return result


def all_day_query(modem_type, ivt_ids):
    ivt_ids_str = ', '.join(f"'{ivt_id}'" for ivt_id in ivt_ids)
    query = f"select * from {TABLE_TYPE[modem_type]} where IVTID in ({ivt_ids_str})"

    return query


def period_query(modem_type, ivt_ids, start_date, end_date):
    ivt_ids_str = ', '.join(f"'{ivt_id}'" for ivt_id in ivt_ids)
    query = f"select * from {TABLE_TYPE[modem_type]} where IVTID in ({ivt_ids_str}) and DATE_FORMAT(EVTDATME, '%Y-%m-%d') >= '{start_date}' and DATE_FORMAT(EVTDATME, '%Y-%m-%d') <= '{end_date}'"

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

    print(result_list)

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

    print(result_list)
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
# db(1, IVTID, '2024-01-14', '2024-01-15')
# unt_all_query()
# cst_all_query('0519413381')
# pwr_all_query('0519413381', 'CST-2023072500001')
# modem_query('PWR-2023072500071')
ivt_all_query('REMS-20230724000001')
