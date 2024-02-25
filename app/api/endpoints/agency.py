from fastapi import APIRouter, Depends
from app.database.database import get_db
from app.models.agency_module import Agency
from sqlalchemy.orm import Session

router = APIRouter(prefix="/agency", tags=["agency"])

@router.get("")
async def get_agency_list(db:Session=Depends(get_db)):
    return db.query(Agency.agency_name).all()