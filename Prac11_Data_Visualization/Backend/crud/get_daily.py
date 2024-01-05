from sqlalchemy.orm import Session
from sqlalchemy.sql import cast
from sqlalchemy import Integer
from models.more_models import daily_solar_data
from schemas.schemas import DailyData
from datetime import datetime

def get_solar_day_history(db: Session, untid: str, ivtid: str, start_date: str, end_date: str):
    return db.query(daily_solar_data).filter(
        daily_solar_data.UNTID == untid,
        daily_solar_data.IVTID == ivtid,
        cast(daily_solar_data.EVTDATE, Integer) >= int(start_date),
        cast(daily_solar_data.EVTDATE, Integer) <= int(end_date)
    ).all()

def convert_to_daily_solar_data_model(data):
    return [daily_solar_data(**item.as_dict()) for item in data]