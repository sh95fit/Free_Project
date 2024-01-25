import os
from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = f"mysql+pymysql://{os.environ['db_user']}:{os.environ['db_password']}@{os.environ['db_host']}:{os.environ['db_port']}/{os.environ['db_name']}"

MODEM_TYPE = {'LTE': 0,
              'TCP': 0,
              'LORA': 1,
              'GSREMS': 3}

TABLE_TYPE = {0: 'tb_slalteloghis',
              1: 'tb_slaloraloghis',
              3: 'tb_slagsremsloghis'}