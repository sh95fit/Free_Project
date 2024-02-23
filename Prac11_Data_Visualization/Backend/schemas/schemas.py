from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime


class DailyData(BaseModel):
    UNTID: str
    IVTID: str
    EVTDATE: str
    TPG: float = 0.00
    CPG: Optional[float] = None
    EQLOW: Optional[int] = None
    EQMAX: Optional[int] = None
    GENTIME: Optional[float] = 0.00
    UPDDATIME: Optional[datetime] = None

    class Config:
        from_attributes = True


class SolarDailyData(BaseModel):
    UNTID: str
    IVTID: List[str]
    start_date: str
    end_date: str


class SolarDayData(BaseModel):
    UNTID: str
    PWRID: str
    start_date: str
    end_date: str


class HourData(BaseModel):
    UNTID: str
    IVTID: str
    EVTDATE: str
    EVTHH: str
    TPG: float = 0.00
    CPG: Optional[float] = None
    GENTIME: Optional[float] = 0.00
    UPDDATIME: Optional[datetime] = None

    class Config:
        from_attributes = True


class SolarHourData(BaseModel):
    UNTID: str
    IVTID: List[str]
    start_date: str
    end_date: str


class SolarHourlyData(BaseModel):
    UNTID: str
    PWRID: str
    start_date: str
    end_date: str


class UntInfo(BaseModel):
    UNTID: str
    UNTNM: str
    UNTNM_EN: Optional[str] = None
    UNTCEO: str
    UNTCEO_EN: Optional[str] = None
    BIZNO: Optional[str] = None
    BIZKINDNO: Optional[str] = None
    CORPNO: Optional[str] = None
    BIZKIND: Optional[str] = None
    BIZITEM: Optional[str] = None
    TELNO: Optional[str] = None
    FAXNO: Optional[str] = None
    ZIPNO: Optional[str] = None
    ADDR1: Optional[str] = None
    ADDR2: Optional[str] = None
    ADDR1_EN: Optional[str] = None
    ADDR2_EN: Optional[str] = None
    EHOME: Optional[str] = None
    CTRDATE: Optional[str] = None
    EXPDATE: Optional[str] = None
    CHGNAME: Optional[str] = None
    CHGOFFITEL: Optional[str] = None
    CHGPERHP: Optional[str] = None
    TAXEMAIL: Optional[str] = None
    VATTYPE: Optional[str] = None
    TRFCYC: Optional[int] = None
    SMPCYC: Optional[int] = None
    REMARK: Optional[str] = None
    USETYPE: Optional[str] = 'Y'
    REGUSER: Optional[str] = None
    EDTUSER: Optional[str] = None
    REGDATIME: Optional[datetime] = None
    EDTDATIME: Optional[datetime] = None
    BIZTYPE: Optional[int] = None

    class Config:
        from_attributes = True


class CstInfo(BaseModel):
    UNTID: str
    CSTID: str
    PWRID: str

    class Config:
        from_attributes = True


class PwrRtuInfo(BaseModel):
    UNTID: str
    PWRID: str
    RTUID: str

    class Config:
        from_attributes = True


class RtuModInfo(BaseModel):
    UNTID: str
    RTUID: str
    MODEMID: str
    MODEMTYPE: int

    class Config:
        from_attributes = True


class ModIvtInfo(BaseModel):
    UNTID: str
    MODEMID: str
    IVTID: str
    MODETYPE: int


class LawData(BaseModel):
    UNTID: str
    IVTID: str
    EVTDATME: datetime
    READTIME: Optional[str] = None
    PHASE: Optional[int] = None
    STATIONNO: Optional[int] = None
    ERRCD: Optional[int] = None
    INV1: Optional[float] = None
    INV2: Optional[float] = None
    INV3: Optional[float] = None
    INV4: Optional[float] = None
    INV5: Optional[float] = None
    INV6: Optional[float] = None
    INV7: Optional[float] = None
    INV8: Optional[float] = None
    INV9: Optional[float] = None
    INV10: Optional[float] = None
    # INV11: Optional[float] = None
    # INV12: Optional[float] = None
    # INV13: Optional[float] = None
    # INV14: Optional[float] = None
    # INV15: Optional[float] = None
    # INV16: Optional[float] = None
    # INV17: Optional[float] = None
    # INV18: Optional[float] = None
    # INV19: Optional[float] = None
    # INV20: Optional[float] = None
    INA1: Optional[float] = None
    INA2: Optional[float] = None
    INA3: Optional[float] = None
    INA4: Optional[float] = None
    INA5: Optional[float] = None
    INA6: Optional[float] = None
    INA7: Optional[float] = None
    INA8: Optional[float] = None
    INA9: Optional[float] = None
    INA10: Optional[float] = None
    # INA11: Optional[float] = None
    # INA12: Optional[float] = None
    # INA13: Optional[float] = None
    # INA14: Optional[float] = None
    # INA15: Optional[float] = None
    # INA16: Optional[float] = None
    # INA17: Optional[float] = None
    # INA18: Optional[float] = None
    # INA19: Optional[float] = None
    # INA20: Optional[float] = None
    INP: Optional[float] = None
    OUTV: Optional[float] = None
    OUTA: Optional[float] = None
    OUTVR: Optional[float] = None
    OURVS: Optional[float] = None
    OUTVT: Optional[float] = None
    OUTAR: Optional[float] = None
    OUTAS: Optional[float] = None
    OUTAT: Optional[float] = None
    OUTP: Optional[float] = None
    PF: Optional[float] = None
    FRQ: Optional[float] = None
    TEMP: Optional[float] = None
    TPG: Optional[float] = None
    RUNTYPE: Optional[int] = None
    CPG: Optional[float] = None
    INVERRCD: Optional[int] = None
    ONHOUR: Optional[int] = None
    IVTFIRMVER: Optional[int] = None
    # STATUS01: Optional[int] = None
    # STATUS02: Optional[int] = None
    # STATUS03: Optional[int] = None
    # STATUS04: Optional[int] = None
    # STATUS05: Optional[int] = None
    # STATUS06: Optional[int] = None
    # STATUS07: Optional[int] = None
    # STATUS08: Optional[int] = None
    # STATUS09: Optional[int] = None
    # STATUS10: Optional[int] = None
    # STATUS11: Optional[int] = None
    EVTDATE: Optional[str] = None
    VERSION: Optional[int] = None
    USETYPE: Optional[str] = 'Y'
    UPDDATIME: Optional[datetime] = None
    TOTAL_CO2: Optional[int] = None
    TODAY_CO2: Optional[int] = None
    GENERATION_TIME: Optional[int] = None

    class Config:
        from_attributes = True
