from sqlalchemy import Column, String, Integer, Float, DateTime, func, select
from database.session.more_db import engine, Base
from pydantic import BaseModel

# 기존 데이터베이스 테이블 모델 정의
class daily_solar_data(Base):
    __tablename__ = "tb_sladayhis"

    UNTID = Column(String(20), primary_key=True, comment='시공사ID')
    IVTID = Column(String(20), primary_key=True, comment='INVERTERID')
    EVTDATE = Column(String(10), primary_key=True, comment='날짜')
    TPG = Column(Float(precision=20), nullable=False, default=0.00, comment='당일 발전량')
    CPG = Column(Float(precision=20), comment='누적 발전량')
    EQLOW = Column(Integer, comment='최저출력')
    EQMAX = Column(Integer, comment='최대출력')
    GENTIME = Column(Float(precision=20), default=0.00, comment='발전시간')
    UPDDATIME = Column(DateTime, default=func.now(), comment='업데이트시간')

    def as_dict(self):
        return {column.name: getattr(self, column.name) for column in self.__table__.columns}

Base.metadata.reflect(bind=engine)
daily_solar_data.__table__ = Base.metadata.tables['tb_sladayhis']