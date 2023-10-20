from fastapi import APIRouter, HTTPException, status, Depends, Path
from models.gsrems_models import gsmon_solar_data
from models.main_models import GsmonSolarData

from schemas.schemas import GsremsData

from database.connection import main_db, gsrems_db

from sqlalchemy.orm import Session
from sqlalchemy import and_, or_, desc
from typing import List

from datetime import datetime


now = datetime.now()
now_date = now.strftime('%Y%m%d')


router = APIRouter(
    prefix="/gsrems",
    tags=["gsrems"],
)


@router.get("/today", response_model=List[GsremsData])
async def today_data(rtu_id: int, db: Session = Depends(gsrems_db)):
    result = db.query(gsmon_solar_data).filter(
        and_(gsmon_solar_data.c.rtu_id == rtu_id, gsmon_solar_data.c.save_time_id == now_date)).order_by(desc(gsmon_solar_data.c.save_time)).all()

    return result


@router.get("/transfer_data", response_model=List[GsremsData])
async def transfer_data(rtu_id: int, gs_db: Session = Depends(gsrems_db), main_db: Session = Depends(main_db)):

    # GSREMS 서버에서 데이터 가져오기
    gsrems_data = gs_db.query(gsmon_solar_data).filter(
        and_(gsmon_solar_data.c.rtu_id == rtu_id, gsmon_solar_data.c.save_time_id == now_date)).order_by(desc(gsmon_solar_data.c.save_time)).all()

    main_data = []
    for gs_data in gsrems_data:
        main_data.append(GsmonSolarData(**gs_data))

    main_db.add_all(main_data)
    main_db.commit()

    return main_data


# # GSREMS 데이터 가져오기 테스트


# @router.get("/today/{rtu_id}")
# async def select_data(rtu_id: int = Path(..., title='rtu_id'), db: Session = Depends(gsrems_db)):
#     result = db.execute(
#         f"SELECT * FROM gsmon_solar_data where save_time_id={now_date} and rtu_id={rtu_id} order by id desc")
#     data = [dict(row) for row in result]

#     if not data:
#         return {"message": "Raw data not found"}

#     return {"data": data}


# # GSREMS 정의된 테이블 활용하기
# @router.get("/today_table/{rtu_id}")
# async def gsrems_data(rtu_id: int = Path(..., title='rtu_id'), db: Session = Depends(gsrems_db)):
#     result = db.query(gsmon_solar_data).filter(
#         and_(gsmon_solar_data.c.rtu_id == rtu_id, gsmon_solar_data.c.save_time_id == now_date)).order_by(desc(gsmon_solar_data.c.save_time)).all()

#     return result
