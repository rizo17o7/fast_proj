from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List, Optional
from .. import crud, schemas
from ..database import SessionLocal

router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/debts/", response_model=schemas.Debt)
def create_debt(debt: schemas.DebtCreate, db: Session = Depends(get_db)):
    return crud.create_debt(db, debt)


@router.put("/debts/{debt_id}", response_model=schemas.Debt)
def update_debt(debt_id: int, debt: schemas.DebtCreate, db: Session = Depends(get_db)):
    db_debt = crud.update_debt(db, debt_id, debt)
    if db_debt is None:
        raise HTTPException(status_code=404, detail="Debt not found")
    return db_debt


@router.delete("/debts/{debt_id}", response_model=schemas.Debt)
def delete_debt(debt_id: int, db: Session = Depends(get_db)):
    db_debt = crud.delete_debt(db, debt_id)
    if db_debt is None:
        raise HTTPException(status_code=404, detail="Debt not found")
    return db_debt


@router.get("/debts/", response_model=List[schemas.Debt])
def read_debts(debt_type: Optional[str] = None, db: Session = Depends(get_db)):
    return crud.get_debts(db, debt_type)
