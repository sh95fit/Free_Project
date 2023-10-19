import os
import dotenv

dotenv_file = dotenv.find_dotenv()
dotenv.load_dotenv(dotenv_file)

# 데이터베이스 경로
DATABASE_URL = f"mysql+pymysql://{os.environ['db_user']}:{os.environ['db_password']}@{os.environ['db_host']}:{os.environ['db_port']}/{os.environ['db_name']}"

GSREMS_URL = f"mysql+pymysql://{os.environ['gsrems_user']}:{os.environ['gsrems_password']}@{os.environ['gsrems_host']}:{os.environ['gsrems_port']}/{os.environ['gsrems_name']}"
