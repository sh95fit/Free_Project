from fastapi import FastAPI, Depends, Path
from models import main_models
from models.gsrems_models import gsmon_solar_data
from database.connection import main_db, gsrems_db
from sqlalchemy.orm import Session
from sqlalchemy import and_, or_, desc

from routes.gsrems.gsrems_router import router as GSREMS_router

app = FastAPI()


app.include_router(GSREMS_router)
