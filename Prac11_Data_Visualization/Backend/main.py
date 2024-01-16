from fastapi import FastAPI
from middleware.cors import setup_cors

from routes.daily_router import router as Daily_router
from routes.get_info import router as GetUnt_router

app = FastAPI()


@app.get('/')
def main():
    return "Hun's Dashboard"


setup_cors(app)

app.include_router(Daily_router)
app.include_router(GetUnt_router)
