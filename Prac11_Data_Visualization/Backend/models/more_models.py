from sqlalchemy import Column, String, Integer, Float, DateTime, func, select, VARCHAR, MetaData, Table, DECIMAL, text
from sqlalchemy.orm import declarative_base
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


# 인버터별 발전량 데이터 받아오기
def create_dynamic_model_class(table_name):
    # 모델의 충돌을 방지 (class_registry를 빈 딕셔너리로 지정하여 비움으로써 새로운 세션에서 중복을 방지)
    DynamicBase = declarative_base(class_registry=dict())

    class get_lawdata(DynamicBase):
        __tablename__ = table_name
        __table_args__ = {'extend_existing': True}
        UNTID = Column(VARCHAR(20), primary_key=True, comment='시공사ID')
        IVTID = Column(VARCHAR(20), primary_key=True, comment='INVERTERID')
        EVTDATME = Column(VARCHAR(25), primary_key=True, comment='날짜시간')
        READTIME = Column(VARCHAR(20), comment='설비읽은시간')
        PHASE = Column(Integer, comment='단/삼상')
        STATIONNO = Column(Integer, primary_key=True, comment='국번')
        ERRCD = Column(Integer, comment='통신오류')
        INV1 = Column(Integer, comment='입력 전압1')
        INV2 = Column(Integer, comment='입력 전압2')
        INV3 = Column(Integer, comment='입력 전압3')
        INV4 = Column(Integer, comment='입력 전압4')
        INV5 = Column(Integer, comment='입력 전압5')
        INV6 = Column(Integer, comment='입력 전압6')
        INV7 = Column(Integer, comment='입력 전압7')
        INV8 = Column(Integer, comment='입력 전압8')
        INV9 = Column(Integer, comment='입력 전압9')
        INV10 = Column(Integer, comment='입력 전압10')
        # INV11 = Column(Integer, comment='입력 전압11')
        # INV12 = Column(Integer, comment='입력 전압12')
        # INV13 = Column(Integer, comment='입력 전압13')
        # INV14 = Column(Integer, comment='입력 전압14')
        # INV15 = Column(Integer, comment='입력 전압15')
        # INV16 = Column(Integer, comment='입력 전압16')
        # INV17 = Column(Integer, comment='입력 전압17')
        # INV18 = Column(Integer, comment='입력 전압18')
        # INV19 = Column(Integer, comment='입력 전압19')
        # INV20 = Column(Integer, comment='입력 전압20')
        INA1 = Column(Integer, comment='입력 전류1')
        INA2 = Column(Integer, comment='입력 전류2')
        INA3 = Column(Integer, comment='입력 전류3')
        INA4 = Column(Integer, comment='입력 전류4')
        INA5 = Column(Integer, comment='입력 전류5')
        INA6 = Column(Integer, comment='입력 전류6')
        INA7 = Column(Integer, comment='입력 전류7')
        INA8 = Column(Integer, comment='입력 전류8')
        INA9 = Column(Integer, comment='입력 전류9')
        INA10 = Column(Integer, comment='입력 전류10')
        # INA11 = Column(Integer, comment='입력 전류11')
        # INA12 = Column(Integer, comment='입력 전류12')
        # INA13 = Column(Integer, comment='입력 전류13')
        # INA14 = Column(Integer, comment='입력 전류14')
        # INA15 = Column(Integer, comment='입력 전류15')
        # INA16 = Column(Integer, comment='입력 전류16')
        # INA17 = Column(Integer, comment='입력 전류17')
        # INA18 = Column(Integer, comment='입력 전류18')
        # INA19 = Column(Integer, comment='입력 전류19')
        # INA20 = Column(Integer, comment='입력 전류20')
        INP = Column(Integer, comment='입력 전력')
        OUTV = Column(Integer, comment='단상 출력 전압')
        OUTA = Column(Integer, comment='단상 출력 전류')
        OUTVR = Column(Integer, comment='삼상 출력 전압 R')
        OURVS = Column(Integer, comment='삼상 출력 전압 S')
        OUTVT = Column(Integer, comment='삼상 출력 전압 T')
        OUTAR = Column(Integer, comment='삼상 출력 전류 R')
        OUTAS = Column(Integer, comment='삼상 출력 전류 S')
        OUTAT = Column(Integer, comment='삼상 출력 전류 T')
        OUTP = Column(Integer, comment='출력 전력')
        PF = Column(Float, comment='Power factor')
        FRQ = Column(Float, comment='주파수')
        TEMP = Column(Float, comment='온도')
        TPG = Column(DECIMAL(20, 0), comment='당일 발전량')
        RUNTYPE = Column(Integer, comment='작동 여부')
        CPG = Column(DECIMAL(20, 0), comment='누적 발전량')
        INVERRCD = Column(Integer, comment='인버터 에러코드')
        ONHOUR = Column(Integer, comment='연속 동작 시간')
        IVTFIRMVER = Column(Integer, comment='인버터 펌웨어 버전')
        # STATUS01 = Column(Integer, comment='상태코드1')
        # STATUS02 = Column(Integer, comment='상태코드2')
        # STATUS03 = Column(Integer, comment='상태코드3')
        # STATUS04 = Column(Integer, comment='상태코드4')
        # STATUS05 = Column(Integer, comment='상태코드5')
        # STATUS06 = Column(Integer, comment='상태코드6')
        # STATUS07 = Column(Integer, comment='상태코드7')
        # STATUS08 = Column(Integer, comment='상태코드8')
        # STATUS09 = Column(Integer, comment='상태코드9')
        # STATUS10 = Column(Integer, comment='상태코드10')
        # STATUS11 = Column(Integer, comment='상태코드11')
        EVTDATE = Column(VARCHAR(10), comment='날짜')
        VERSION = Column(Integer, comment='버전')
        USETYPE = Column(VARCHAR(1), default='Y', comment='사용구분')
        UPDDATIME = Column(DateTime, comment='업데이트시간')
        TOTAL_CO2 = Column(
            Integer, comment='누적 CO2 저감량 CPG(kWh) * 0.46625/1000')
        TODAY_CO2 = Column(
            Integer, comment='당일 CO2 저감량 TPG(kWh) * 0.46625/1000')
        GENERATION_TIME = Column(Integer, comment='발전시간')

        def as_dict(self):
            return {column.name: getattr(self, column.name) for column in self.__table__.columns}

    return get_lawdata


metadata = MetaData()
Base.metadata.reflect(bind=engine)


daily_solar_data.__table__ = Base.metadata.tables['tb_sladayhis']
get_untmstinfo.__table__ = Base.metadata.tables['tb_untmstinfo']
get_cstpwrmap.__table__ = Base.metadata.tables['tb_cstpwrmap']
