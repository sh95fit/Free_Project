from sqlalchemy.orm import Session, aliased
from sqlalchemy.sql import cast
from sqlalchemy import Integer, and_, exists, select, literal
from models.more_models import daily_solar_data, get_rtumodmap, get_modivtmap, get_pwrrtuinfo
from schemas.schemas import DailyData
from datetime import datetime

from typing import Optional, List


def get_solar_day_history(db: Session, untid: str, ivtid: str, start_date: str, end_date: str):
    return db.query(daily_solar_data).filter(
        daily_solar_data.UNTID == untid,
        daily_solar_data.IVTID == ivtid,
        cast(daily_solar_data.EVTDATE, Integer) >= int(start_date),
        cast(daily_solar_data.EVTDATE, Integer) <= int(end_date)
    ).all()


def get_solay_daily_history(db: Session, untid: str, ivt_list: List[str], start_date: str, end_date: str):
    return db.query(daily_solar_data).filter(
        daily_solar_data.UNTID == untid,
        daily_solar_data.IVTID.in_(ivt_list),
        cast(daily_solar_data.EVTDATE, Integer) >= int(start_date),
        cast(daily_solar_data.EVTDATE, Integer) <= int(end_date)
    )


def get_solar_daily_data(db: Session, untid: str, pwrid: str, start_date: str, end_date: str):

    # # 별칭을 사용하여 같은 테이블을 조인할 경우 충돌을 피합니다.
    daily_table = aliased(daily_solar_data)

    # join으로 처리 시 성능 이슈 발생 (로딩 2~30초 (20일치 데이터 기준))
    # query = (
    #     db.query(daily_table)
    #     .join(
    #         get_modivtmap, daily_table.IVTID == get_modivtmap.IVTID
    #     )
    #     .join(
    #         get_rtumodmap,
    #         (get_modivtmap.MODEMID == get_rtumodmap.MODEMID) &
    #         (get_modivtmap.MODTYPE == get_rtumodmap.MODTYPE)
    #     )
    #     .join(
    #         get_pwrrtuinfo, get_rtumodmap.RTUID == get_pwrrtuinfo.RTUID
    #     )
    #     .filter(
    #         (get_pwrrtuinfo.PWRID == pwrid) &
    #         (get_modivtmap.UNTID == untid)
    #     )
    # )

    # 서브쿼리 방식도 성능 이슈 발생
    # # 서브쿼리 정의
    # subquery = (
    #     select(1)
    #     .where(
    #         (daily_table.IVTID == get_modivtmap.IVTID) &
    #         (get_modivtmap.MODEMID == get_rtumodmap.MODEMID) &
    #         (get_modivtmap.MODTYPE == get_rtumodmap.MODTYPE) &
    #         (get_rtumodmap.RTUID == get_pwrrtuinfo.RTUID) &
    #         (get_pwrrtuinfo.PWRID == pwrid) &
    #         (get_modivtmap.UNTID == untid)
    #     )
    #     .exists()
    # )

    # # # 메인 쿼리에서 서브쿼리 활용
    # query = db.query(daily_table).filter(subquery)

    # # 코드 최적화
    pwrrtu = aliased(get_pwrrtuinfo)
    rtumod = aliased(get_rtumodmap)
    modivt = aliased(get_modivtmap)

    result = (
        db.query(daily_table)
        .join(modivt, daily_table.IVTID == modivt.IVTID)
        .join(rtumod, (modivt.MODEMID == rtumod.MODEMID) & (modivt.MODTYPE == rtumod.MODTYPE))
        .join(pwrrtu, rtumod.RTUID == pwrrtu.RTUID)
        .filter(
            (pwrrtu.PWRID == pwrid) &
            (modivt.UNTID == untid)
        )
        .all()
    )

    # join방식, 서브쿼리 방식에서 사용
    # result = query.all()

    return result


def convert_to_dict(crud_model, data):
    return [crud_model(**item.as_dict()) for item in data]
