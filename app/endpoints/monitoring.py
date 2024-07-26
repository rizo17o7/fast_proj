from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from .. import crud
from ..database import SessionLocal

router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get("/monitoring/")
def read_statistics(db: Session = Depends(get_db)):
    return crud.get_statistics(db)
