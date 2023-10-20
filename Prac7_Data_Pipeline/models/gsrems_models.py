from sqlalchemy import MetaData, Table
from database.session.gsrems_db import engine_gs

metadata = MetaData(bind=engine_gs)

gsmon_solar_data = Table('gsmon_solar_data', metadata,
                         autoload=True, autoload_with=engine_gs)
