from fastapi import FastAPI, Depends
from models import Test
from datetime import datetime
from database import SessionLocal
from sqlalchemy.orm import Session


app = FastAPI()

test_raw = Test(company='UGS', api_key='serial_0000',
                create_date=datetime.now())


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/test")
def create_table(db: Session = Depends(get_db)):
    db.add(test_raw)
    db.commit()

    return test_raw
