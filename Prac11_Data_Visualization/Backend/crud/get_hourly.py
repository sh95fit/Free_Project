from sqlalchemy.orm import Session, aliased
from sqlalchemy.sql import cast
from sqlalchemy import Integer, and_, exists
from models.more_models import hourly_solar_data, get_pwrrtuinfo, get_rtumodmap, get_modivtmap
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


def get_solar_hourly_history(db: Session, untid: str, pwrid: str, start_date: str, end_date: str):

    hourly_table = aliased(hourly_solar_data)

    pwrrtu = aliased(get_pwrrtuinfo)
    rtumod = aliased(get_rtumodmap)
    modivt = aliased(get_modivtmap)

    result = (
        db.query(hourly_table)
        .join(modivt, hourly_table .IVTID == modivt.IVTID)
        .join(rtumod, (modivt.MODEMID == rtumod.MODEMID) & (modivt.MODTYPE == rtumod.MODTYPE))
        .join(pwrrtu, rtumod.RTUID == pwrrtu.RTUID)
        .filter(
            (pwrrtu.PWRID == pwrid) &
            (modivt.UNTID == untid)
        )
        .all()
    )

    return result


def convert_to_dict(crud_model, data):
    return [crud_model(**item.as_dict()) for item in data]
