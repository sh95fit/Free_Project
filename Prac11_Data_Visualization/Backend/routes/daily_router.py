from fastapi import APIRouter, HTTPException, status, Depends, Path, Query

from models.more_models import daily_solar_data

from database.connection import more_db

from sqlalchemy.orm import Session
from sqlalchemy import and_, or_, desc
from typing import List

from schemas.schemas import DailyData

from crud.get_daily import get_solar_day_history, convert_to_daily_solar_data_model

from datetime import datetime

router = APIRouter(
    prefix="/more",
    tags=["MORE"]
)


@router.get("/daily/{untid}/{ivtid}", response_model=List[DailyData])
def read_solar_day_history(untid: str, ivtid: str, start_date: str = Query(..., description="시작일 양식 ex> 20240106"), end_date: str = Query(..., description="종료일 양식 ex> 20240107"), db: Session = Depends(more_db)):
    if int(start_date) > int(end_date) :
        raise HTTPException(status_code=404, detail="Invaild date range. Start date should be less than or equal to end date.")

    solar_day_history = get_solar_day_history(db, untid, ivtid, start_date, end_date)
    if solar_day_history is None:
        raise HTTPException(status_code=404, detail="Solar Day History not found")
    return convert_to_daily_solar_data_model(solar_day_history)