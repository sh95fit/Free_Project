from fastapi import FastAPI
from middleware.cors import setup_cors

from routes.daily_router import router as Daily_router
from routes.get_info import router as GetUnt_router
from routes.hourly_router import router as Hourly_router
from routes.auth_router import router as Auth_router

app = FastAPI()


@app.get('/')
def main():
    return "Hun's Dashboard"


setup_cors(app)

app.include_router(Daily_router)
app.include_router(Hourly_router)
app.include_router(GetUnt_router)


app.include_router(Auth_router)
