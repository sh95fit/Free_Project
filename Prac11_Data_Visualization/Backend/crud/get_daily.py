from sqlalchemy.orm import Session
from sqlalchemy.sql import cast
from sqlalchemy import Integer
from models.more_models import daily_solar_data
from schemas.schemas import DailyData
from datetime import datetime

from typing import Optional, List


def get_solar_day_history(db: Session, untid: str, ivtid: str, start_date: str, end_date: str):
    return db.query(daily_solar_data).filter(
        daily_solar_data.UNTID == untid,
        daily_solar_data.IVTID == ivtid,
        cast(daily_solar_data.EVTDATE, Integer) >= int(start_date),
        cast(daily_solar_data.EVTDATE, Integer) <= int(end_date)
    ).all()


def get_solay_daily_history(db: Session, untid: str, ivt_list: List[str], start_date: str, end_date: str):
    return db.query(daily_solar_data).filter(
        daily_solar_data.UNTID == untid,
        daily_solar_data.IVTID.in_(ivt_list),
        cast(daily_solar_data.EVTDATE, Integer) >= int(start_date),
        cast(daily_solar_data.EVTDATE, Integer) <= int(end_date)
    )


def convert_to_dict(crud_model, data):
    return [crud_model(**item.as_dict()) for item in data]
