from fastapi import APIRouter, HTTPException, status, Depends, Path, Query

from models.more_models import hourly_solar_data

from database.connection import more_db

from sqlalchemy.orm import Session
from sqlalchemy import and_, or_, desc
from typing import List

from schemas.schemas import HourData, SolarHourData, SolarHourlyData

from crud.get_hourly import get_solar_hour_history, convert_to_dict, get_solar_hourly_history

from datetime import datetime

from typing import List, Optional


router = APIRouter(
    prefix="/more",
    tags=["MORE"]
)


@router.post("/hour", response_model=List[HourData])
def read_solar_hour_history(untid: str, ivt_list: List[str], start_date: str = Query(..., description="시작일 양식 ex> 20240106"), end_date: str = Query(..., description="종료일 양식 ex> 20240107"), db: Session = Depends(more_db)):
    if int(start_date) > int(end_date):
        raise HTTPException(
            status_code=404, detail="Invaild date range. Start date should be less than or equal to end date.")

    solar_hour_history = get_solar_hour_history(
        db, untid, ivt_list, start_date, end_date)

    if solar_hour_history is None:
        raise HTTPException(
            status_code=404, detail="Solar Day History not found")

    return convert_to_dict(HourData, solar_hour_history)


@router.post("/hourly/post", response_model=List[HourData])
def read_solar_hourly_history(data: SolarHourData, db: Session = Depends(more_db)):
    untid = data.UNTID
    ivt_list = data.IVTID
    start_date = data.start_date
    end_date = data.end_date

    if int(start_date) > int(end_date):
        raise HTTPException(
            status_code=404, detail="Invaild date range. Start date should be less than or equal to end date.")

    solar_hour_history = get_solar_hour_history(
        db, untid, ivt_list, start_date, end_date)

    if solar_hour_history is None:
        raise HTTPException(
            status_code=404, detail="Solar Day History not found")

    return convert_to_dict(HourData, solar_hour_history)


@router.post("/hourly", response_model=List[HourData])
def read_hourly_solar_data(data: SolarHourlyData, db: Session = Depends(more_db)):
    untid = data.UNTID
    pwrid = data.PWRID
    start_date = data.start_date
    end_date = data.end_date

    if int(start_date) > int(end_date):
        raise HTTPException(
            status_code=404, detail="Invaild date range. Start date should be less than or equal to end date.")

    solar_hour_history = get_solar_hourly_history(
        db, untid, pwrid, start_date, end_date)

    if solar_hour_history is None:
        raise HTTPException(
            status_code=404, detail="Solar Day History not found")

    return convert_to_dict(HourData, solar_hour_history)