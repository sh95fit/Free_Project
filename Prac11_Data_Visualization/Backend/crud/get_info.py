from sqlalchemy.orm import Session
from sqlalchemy.sql import cast
from sqlalchemy import Integer, text
from models.more_models import get_untmstinfo, get_cstpwrmap, create_dynamic_model_class
from schemas.schemas import UntInfo
from datetime import datetime
from typing import List, Optional

from utils.data_extraction import generate_monthly_first_date_list


def get_unt_info(db: Session):
    return db.query(get_untmstinfo).all()


def get_cst_info(db: Session, untid: str):
    return db.query(get_cstpwrmap).filter(
        get_cstpwrmap.UNTID == untid
    ).all()


def get_raw_data(db: Session, modem_type: int, ivt_list: List[str], start_date: Optional[str] = None, end_date: Optional[str] = None):
    result_list = []
    if start_date is None or end_date is None:
        if modem_type == 1 or modem_type == 2:
            start_date = '2023-06-01'
            table_list = generate_monthly_first_date_list(
                modem_type, '2023-06-01', datetime.now().strftime('%Y-%m-%d'))
        else:
            start_date = '2023-07-01'
            table_list = generate_monthly_first_date_list(
                modem_type, start_date, datetime.now().strftime('%Y-%m-%d'))
        for table in table_list:
            dynamic_model_class = create_dynamic_model_class(table)
            # dynamic_model_class = text(table)
            # db.bind_mapper(dynamic_model_class)

            query = db.query(dynamic_model_class).filter(
                dynamic_model_class.IVTID.in_(ivt_list))

            result = query.all()

            result_list.extend(result)

        return result_list

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
        for table in table_list:
            dynamic_model_class = create_dynamic_model_class(table)
            # db.bind_mapper(dynamic_model_class)

            query = db.query(dynamic_model_class).filter(
                dynamic_model_class.IVTID.in_(ivt_list),
                dynamic_model_class.EVTDATME <= end_date
            )

            result = query.all()

            result_list.extend(result)

        return result_list


def convert_to_dict(crud_model, data):
    return [crud_model(**item.as_dict()) for item in data]
