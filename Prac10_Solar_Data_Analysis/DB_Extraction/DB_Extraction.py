from Util import db, ivt_all_query, modem_query, pwr_all_query, cst_all_query, unt_all_query, period_query, all_day_query, save_csv, generate_monthly_first_date_list, connection_db


# UNTID = input("시공사 코드 (ex> 4098610941) : ")
PWRID = input("발전소 코드 (ex> PWR-2023060100017) : ")
PWR_NAME = input("발전소 이름 : ")

modem_info = modem_query(PWRID)

modem_id = list(modem_info[0].keys())[0]
IVTID = [ivt['IVTID'] for ivt in ivt_all_query(modem_id)]
modem_type = list(modem_info[0].values())[0]
select_range = input("전체 기간 추출 여부 (전체:y, 기간지정:n) : ")

if select_range == 'y':
    print("추출중...")
    save_csv(PWR_NAME, modem_type, IVTID)
else:
    start_date = input('시작일 (ex> 2024-01-16) : ')
    end_date = input('마지막일 (ex> 2024-01-17) : ')
    print("추출중...")
    save_csv(PWR_NAME, modem_type, IVTID, start_date, end_date)
