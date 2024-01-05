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