FROM python:3.11

COPY . /src
WORKDIR /src

RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt
# RUN pip install sqlalchemy pymysql 

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--reload", "--port", "8888"]