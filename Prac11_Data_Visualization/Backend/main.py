from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from routes.daily_router import router as Daily_router

app = FastAPI()

@app.get('/')
def main() :
    return "Hun's Dashboard"

app.include_router(Daily_router)