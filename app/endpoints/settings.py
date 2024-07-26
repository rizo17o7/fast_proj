from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from .. import crud, schemas
from ..database import SessionLocal

router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get("/settings/", response_model=schemas.Settings)
def read_settings(db: Session = Depends(get_db)):
    return crud.get_settings(db)


@router.put("/settings/", response_model=schemas.Settings)
def update_settings(settings: schemas.SettingsCreate, db: Session = Depends(get_db)):
    return crud.update_settings(db, settings)
