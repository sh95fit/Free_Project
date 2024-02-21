from sqlalchemy.orm import Session
from sqlalchemy.sql import cast
from sqlalchemy import Integer
from models.more_models import hourly_solar_data
from schemas.schemas import HourData
from datetime import datetime

from typing import List, Optional


def get_solar_hour_history(db: Session, untid: str, ivt_list: List[str], start_date: str, end_date: str):
    return db.query(hourly_solar_data).filter(
        hourly_solar_data.UNTID == untid,
        hourly_solar_data.IVTID.in_(ivt_list),
        cast(hourly_solar_data.EVTDATE, Integer) >= int(start_date),
        cast(hourly_solar_data.EVTDATE, Integer) <= int(end_date)
    ).all()


def convert_to_dict(crud_model, data):
    return [crud_model(**item.as_dict()) for item in data]
