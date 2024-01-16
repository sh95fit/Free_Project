from sqlalchemy import Column, String, Integer, Float, DateTime, func, select, VARCHAR, MetaData, Table
from database.session.more_db import engine, Base, Session
from pydantic import BaseModel

# get_daily 데이터


class daily_solar_data(Base):
    __tablename__ = "tb_sladayhis"

    UNTID = Column(String(20), primary_key=True, comment='시공사ID')
    IVTID = Column(String(20), primary_key=True, comment='INVERTERID')
    EVTDATE = Column(String(10), primary_key=True, comment='날짜')
    TPG = Column(Float(precision=20), nullable=False,
                 default=0.00, comment='당일 발전량')
    CPG = Column(Float(precision=20), comment='누적 발전량')
    EQLOW = Column(Integer, comment='최저출력')
    EQMAX = Column(Integer, comment='최대출력')
    GENTIME = Column(Float(precision=20), default=0.00, comment='발전시간')
    UPDDATIME = Column(DateTime, default=func.now(), comment='업데이트시간')

    def as_dict(self):
        return {column.name: getattr(self, column.name) for column in self.__table__.columns}


# 시공사 ID 가져오기
class get_untmstinfo(Base):
    __tablename__ = 'tb_untmstinfo'
    UNTID = Column(String(20), primary_key=True, comment='시공사 아이디(ID)')
    UNTNM = Column(String(50), nullable=False, comment='시공사명 (한글)')
    UNTNM_EN = Column(String(50), comment='시공사명 (영문)')
    UNTCEO = Column(String(30), nullable=False, comment='대표자 (한글)')
    UNTCEO_EN = Column(String(50), comment='대표자 (영문)')
    BIZNO = Column(String(12), comment='사업자번호')
    BIZKINDNO = Column(String(4), comment='사업장종번호')
    CORPNO = Column(String(20), comment='법인번호')
    BIZKIND = Column(String(50), comment='업태')
    BIZITEM = Column(String(50), comment='종목')
    TELNO = Column(String(30), comment='전화번호')
    FAXNO = Column(String(30), comment='팩스번호')
    ZIPNO = Column(String(7), comment='우편번호')
    ADDR1 = Column(String(100), comment='주소 (한글)')
    ADDR2 = Column(String(100), comment='상세주소 (한글)')
    ADDR1_EN = Column(String(100), comment='주소 (영문)')
    ADDR2_EN = Column(String(100), comment='상세주소 (영문)')
    EHOME = Column(String(100), comment='홈페이지')
    CTRDATE = Column(String(10), comment='계약일')
    EXPDATE = Column(String(10), comment='만료일')
    CHGNAME = Column(String(30), comment='전자세금계산서 담당자')
    CHGOFFITEL = Column(String(30), comment='전자세금계산서 전화번호')
    CHGPERHP = Column(String(30), comment='전자세금계산서 휴대폰')
    TAXEMAIL = Column(String(50), comment='전자세금계산서 메일주소')
    VATTYPE = Column(String(4), comment='과세, 영세, 면세 (공통 ID 정보 ''V'')')
    TRFCYC = Column(Integer, comment='전송주기')
    SMPCYC = Column(Integer, comment='셈플링주기')
    REMARK = Column(String(100), comment='비고')
    USETYPE = Column(String(1), default='Y', comment='사용구분 Y / N')
    REGUSER = Column(String(20), comment='등록담당자')
    EDTUSER = Column(String(20), comment='수정담당자')
    REGDATIME = Column(DateTime, comment='등록일')
    EDTDATIME = Column(DateTime, comment='수정일')
    BIZTYPE = Column(Integer, comment='사업자 구분')

    def as_dict(self):
        return {column.name: getattr(self, column.name) for column in self.__table__.columns}


# 발전소그룹 ID 가져오기
class get_cstpwrmap(Base):
    __tablename__ = 'tb_cstpwrmap'
    UNTID = Column(VARCHAR(20), comment='시공사ID', primary_key=True)
    CSTID = Column(VARCHAR(20), comment='발전소그룹(거래처)ID', primary_key=True)
    PWRID = Column(VARCHAR(20), comment='발전소ID', primary_key=True)

    def as_dict(self):
        return {column.name: getattr(self, column.name) for column in self.__table__.columns}


metadata = MetaData()
Base.metadata.reflect(bind=engine)


daily_solar_data.__table__ = Base.metadata.tables['tb_sladayhis']
get_untmstinfo.__table__ = Base.metadata.tables['tb_untmstinfo']
get_cstpwrmap.__table__ = Base.metadata.tables['tb_cstpwrmap']
