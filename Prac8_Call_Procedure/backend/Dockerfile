FROM python:3.11

COPY . /src
WORKDIR /src

RUN pip install fastapi uvicorn[standard] --no-cache-dir

CMD ["uvicorn", 'main:app', '--host', '0.0.0.0', '--reload']