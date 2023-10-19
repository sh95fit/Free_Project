from fastapi import FastAPI, Depends
from models import Test, Local
from datetime import datetime
from database import SessionLocal
from sqlalchemy.orm import Session


app = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


test_raw = Test(company='UGS', api_key='serial_0000',
                create_date=datetime.now())

local_raw = Local(data_type='error', protocol='lte', identifier='grandsun_0000',
                  station_number=1, raw_data="1401010000011c0008087c00e10009082903e80258000000000004a1cc0000")


@app.post("/test")
def create_table(db: Session = Depends(get_db)):
    db.add(test_raw)
    db.commit()

    return test_raw


@app.post("/local")
def create_local_table(db: Session = Depends(get_db)):
    db.add(local_raw)
    db.commit()

    return local_raw
