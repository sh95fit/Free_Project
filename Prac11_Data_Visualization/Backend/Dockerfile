FROM python:3.11

COPY . /src
WORKDIR /src

RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt
# RUN pip install sqlalchemy pymysql

# docker-compose와 dockerfile 중 적용 우선순위 확인
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--reload", "--port", "8888"]