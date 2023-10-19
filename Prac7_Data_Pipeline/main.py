from fastapi import FastAPI, Depends, Path
from models import main_models
from datetime import datetime
from database.connection import main_db, gsrems_db
from sqlalchemy.orm import Session


app = FastAPI()


now = datetime.now()
now_date = now.strftime('%Y%m%d')
# print(now_date)

# GSREMS 데이터 가져오기 테스트


@app.get("/select_data/{rtu_id}")
async def select_data(rtu_id: int = Path(..., title='rtu_id'), db: Session = Depends(gsrems_db)):
    result = db.execute(
        f"SELECT * FROM gsmon_solar_data where save_time_id={now_date} and rtu_id={rtu_id} order by id desc")
    data = [dict(row) for row in result]

    if not data:
        return {"message": "Raw data not found"}

    return {"data": data}
