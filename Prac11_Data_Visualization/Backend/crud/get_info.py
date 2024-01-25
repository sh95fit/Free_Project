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

        # 방법1. batch 사이즈로 일정 크기만큼씩 리스트에 저장
        batch_size = 100
        for table in table_list:
            dynamic_model_class = create_dynamic_model_class(table)
            # dynamic_model_class = text(table)
            # db.bind_mapper(dynamic_model_class)

            query = db.query(dynamic_model_class).filter(
                dynamic_model_class.IVTID.in_(ivt_list))

            offset = 0
            while True:
                batch_result = query.offset(offset).limit(batch_size).all()
                if not batch_result:
                    break

                result_list.extend(batch_result)
                offset += batch_size
            db.close()
            db.expunge_all()    # SQLAlchemy의 세션에서 객체를 분리하여 메모리 해제

        return result_list

        # 방법2. 데이터 처리 시 생성된 결과를 즉시 처리 (100개씩 즉시 처리)
        # result_list = list(generate_results(db, table_list, ivt_list))

        # for table in table_list:
        #     dynamic_model_class = create_dynamic_model_class(table)
        #     # dynamic_model_class = text(table)
        #     # db.bind_mapper(dynamic_model_class)

        #     query = db.query(dynamic_model_class).filter(
        #         dynamic_model_class.IVTID.in_(ivt_list))

        # result = query.all()
        # result_list.extend(result)

        # return result_list

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

        # for table in table_list:
        #     dynamic_model_class = create_dynamic_model_class(table)
        #     # db.bind_mapper(dynamic_model_class)

        #     query = db.query(dynamic_model_class).filter(
        #         dynamic_model_class.IVTID.in_(ivt_list),
        #         dynamic_model_class.EVTDATME <= end_date
        #     )

        #     result = query.all()

        #     result_list.extend(result)

        # return result_list

        # 방법1. batch 사이즈로 일정 크기만큼씩 리스트에 저장
        batch_size = 100
        for table in table_list:
            dynamic_model_class = create_dynamic_model_class(table)

            query = db.query(dynamic_model_class).filter(
                dynamic_model_class.IVTID.in_(ivt_list),
                dynamic_model_class.EVTDATME <= end_date
            )

            offset = 0
            while True:
                batch_result = query.offset(offset).limit(batch_size).all()
                if not batch_result:
                    break

                result_list.extend(batch_result)
                offset += batch_size
            db.close()
            db.expunge_all()

        return result_list


# 데이터 처리 시 생성된 결과를 즉시 처리 (100개씩 즉시 처리)
# def generate_results(db, table_list, ivt_list):
#     for table in table_list:
#         dynamic_model_class = create_dynamic_model_class(table)
#         query = db.query(dynamic_model_class).filter(
#             dynamic_model_class.IVTID.in_(ivt_list))

#         for result in query.yield_per(100):  # 100은 적절한 일괄 크기
#             yield result


def convert_to_dict(crud_model, data):
    return [crud_model(**item.as_dict()) for item in data]
