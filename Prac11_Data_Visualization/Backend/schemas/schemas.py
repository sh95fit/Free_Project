from pydantic import BaseModel
from typing import Optional
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


class CstInfo(BaseModel):
    UNTID: str
    CSTID: str
    PWRID: str
