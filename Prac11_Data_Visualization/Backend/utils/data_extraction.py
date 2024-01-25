from datetime import datetime
from dateutil.relativedelta import relativedelta
from core.config import TABLE_TYPE


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
