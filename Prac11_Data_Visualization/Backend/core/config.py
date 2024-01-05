import os
from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = f"mysql+pymysql://{os.environ['db_user']}:{os.environ['db_password']}@{os.environ['db_host']}:{os.environ['db_port']}/{os.environ['db_name']}"