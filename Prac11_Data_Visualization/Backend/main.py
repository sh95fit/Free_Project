from fastapi import FastAPI
from middleware.cors import setup_cors

from routes.daily_router import router as Daily_router

app = FastAPI()


@app.get('/')
def main():
    return "Hun's Dashboard"


setup_cors(app)

app.include_router(Daily_router)
