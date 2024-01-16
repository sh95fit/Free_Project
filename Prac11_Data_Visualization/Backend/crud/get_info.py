from sqlalchemy.orm import Session
from sqlalchemy.sql import cast
from sqlalchemy import Integer
from models.more_models import get_untmstinfo, get_cstpwrmap
from schemas.schemas import UntInfo
from datetime import datetime


def get_unt_info(db: Session):
    return db.query(get_untmstinfo).all()


def get_cst_info(db: Session, untid: str):
    return db.query(get_cstpwrmap).filter(
        get_cstpwrmap.UNTID == untid
    ).all()


def convert_to_dict(crud_model, data):
    return [crud_model(**item.as_dict()) for item in data]
