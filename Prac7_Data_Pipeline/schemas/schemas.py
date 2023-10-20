from pydantic import BaseModel
from datetime import datetime


class GsremsData(BaseModel):

    __tablename__ = "gsmon_solar_data"

    id: int
    rtu_id: int
    inverter_id: int
    multi: int
    phase: int
    code: int
    lerr: int
    inv: int
    inv2: int
    inv3: int
    inv4: int
    inv5: int
    inv6: int
    ina: int
    ina2: int
    ina3: int
    ina4: int
    ina5: int
    ina6: int
    inp: int
    outv: int
    outa: int
    outvr: int
    outvs: int
    outvt: int
    outar: int
    outas: int
    outat: int
    outp: int
    pf: float
    frq: float
    temp: float
    tpg: int
    run: int
    cpg: int
    ec: int
    onhour: int
    dsp: int
    status01: int
    status02: int
    status03: int
    status04: int
    status05: int
    status06: int
    status07: int
    status08: int
    status09: int
    status10: int
    version: int
    save_time_id: int
    status: str
    save_time: datetime
