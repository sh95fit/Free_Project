from fastapi import APIRouter, HTTPException, status, Depends, Path, Query

from models.more_models import daily_solar_data

from database.connection import more_db

from sqlalchemy.orm import Session
from sqlalchemy import and_, or_, desc
from typing import List

from schemas.schemas import DailyData, SolarDailyData, SolarDayData

from crud.get_daily import get_solar_day_history, convert_to_dict, get_solay_daily_history, get_solar_daily_data

from datetime import datetime

router = APIRouter(
    prefix="/more",
    tags=["MORE"]
)


@router.get("/daily/{untid}/{ivtid}", response_model=List[DailyData])
def read_solar_day_history(untid: str, ivtid: str, start_date: str = Query(..., description="시작일 양식 ex> 20240106"), end_date: str = Query(..., description="종료일 양식 ex> 20240107"), db: Session = Depends(more_db)):
    if int(start_date) > int(end_date):
        raise HTTPException(
            status_code=404, detail="Invaild date range. Start date should be less than or equal to end date.")

    solar_day_history = get_solar_day_history(
        db, untid, ivtid, start_date, end_date)
    if solar_day_history is None:
        raise HTTPException(
            status_code=404, detail="Solar Day History not found")
    return convert_to_dict(DailyData, solar_day_history)


@router.post("/daily/post", response_model=List[DailyData])
def read_solar_daily_history(data: SolarDailyData, db: Session = Depends(more_db)):
    untid = data.UNTID
    ivt_list = data.IVTID
    start_date = data.start_date
    end_date = data.end_date

    if int(start_date) > int(end_date):
        raise HTTPException(
            status_code=404, detail="Invaild date range. Start date should be less than or equal to end date.")

    solar_daily_history = get_solay_daily_history(
        db, untid, ivt_list, start_date, end_date)

    if solar_daily_history is None:
        raise HTTPException(
            status_code=404, detail="Solar Day History not found")

    return convert_to_dict(DailyData, solar_daily_history)


@router.post("/daily", response_model=List[DailyData])
def read_daily_solar_data(data: SolarDayData, db: Session = Depends(more_db)):
    untid = data.UNTID
    pwrid = data.PWRID
    start_date = data.start_date
    end_date = data.end_date

    if int(start_date) > int(end_date):
        raise HTTPException(
            status_code=404, detail="Invaild date range. Start date should be less than or equal to end date.")

    solar_hour_history = get_solar_daily_data(
        db, untid, pwrid, start_date, end_date)

    if solar_hour_history is None:
        raise HTTPException(
            status_code=404, detail="Solar Day History not found")

    return convert_to_dict(DailyData, solar_hour_history)
