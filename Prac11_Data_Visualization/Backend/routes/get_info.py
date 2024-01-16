from fastapi import APIRouter, HTTPException, status, Depends, Path, Query

from models.more_models import get_untmstinfo

from database.connection import more_db

from sqlalchemy.orm import Session
from sqlalchemy import and_, or_, desc
from typing import List

from schemas.schemas import UntInfo, CstInfo

from crud.get_info import convert_to_dict, get_unt_info, get_cst_info

from datetime import datetime

router = APIRouter(
    prefix="/more",
    tags=["MORE"]
)


@router.get("/unt", response_model=List[UntInfo])
def get_unt_info_route(db: Session = Depends(more_db)):
    unt_info = get_unt_info(db)
    return convert_to_dict(UntInfo, unt_info)


@router.get("/cst", response_model=List[CstInfo])
def get_cst_info_route(untid: str, db: Session = Depends(more_db)):
    cst_info = get_cst_info(db, untid)
    return convert_to_dict(CstInfo, cst_info)
