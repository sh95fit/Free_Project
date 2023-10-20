from sqlalchemy import Column, Integer, String, Text, DateTime, MetaData, Table, BigInteger, SmallInteger, Float, TIMESTAMP, func
from database.session.gsrems_db import Base_gs, engine_gs

metadata = MetaData()
gsmon_solar_data = Table('gsmon_solar_data', metadata,
                         autoload=True, autoload_with=engine_gs)


# class GsmonSolarData(Base_gs):
#     __tablename__ = "gsmon_solar_data"

#     id = Column(BigInteger, nullable=False,
#                 autoincrement=True, primary_key=True)
#     rtu_id = Column(BigInteger)
#     inverter_id = Column(BigInteger, nullable=False)
#     multi = Column(SmallInteger, nullable=False)
#     phase = Column(Integer)
#     code = Column(Integer, nullable=False)
#     lerr = Column(Integer, nullable=False)
#     inv = Column(SmallInteger)
#     inv2 = Column(SmallInteger)
#     inv3 = Column(SmallInteger)
#     inv4 = Column(SmallInteger)
#     inv5 = Column(SmallInteger)
#     inv6 = Column(SmallInteger)
#     ina = Column(SmallInteger)
#     ina1 = Column(SmallInteger)
#     ina2 = Column(SmallInteger)
#     ina3 = Column(SmallInteger)
#     ina4 = Column(SmallInteger)
#     ina5 = Column(SmallInteger)
#     ina6 = Column(SmallInteger)
#     inp = Column(Integer)
#     outv = Column(SmallInteger)
#     outa = Column(SmallInteger)
#     outvr = Column(SmallInteger)
#     outvs = Column(SmallInteger)
#     outvt = Column(SmallInteger)
#     outar = Column(SmallInteger)
#     outas = Column(SmallInteger)
#     outat = Column(SmallInteger)
#     outp = Column(Integer)
#     pf = Column(Float)
#     frq = Column(Float)
#     temp = Column(Float)
#     tpg = Column(Integer)
#     run = Column(Integer)
#     cpg = Column(BigInteger)
#     ec = Column(SmallInteger)
#     onhour = Column(SmallInteger)
#     dsp = Column(SmallInteger)
#     status01 = Column(SmallInteger)
#     status02 = Column(SmallInteger)
#     status03 = Column(SmallInteger)
#     status04 = Column(SmallInteger)
#     status05 = Column(SmallInteger)
#     status06 = Column(SmallInteger)
#     status07 = Column(SmallInteger)
#     status08 = Column(SmallInteger)
#     status09 = Column(SmallInteger)
#     status10 = Column(SmallInteger)
#     version = Column(SmallInteger)
#     save_time_id = Column(Integer, nullable=False)
#     status = Column(String(3))
#     save_time = Column(TIMESTAMP, nullable=False,
#                        server_default=func.current_timestamp())


# gsmon_solar_data = GsmonSolarData.__table__
