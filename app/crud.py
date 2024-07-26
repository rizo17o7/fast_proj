from sqlalchemy.orm import Session
from . import models, schemas


def get_settings(db: Session):
    return db.query(models.Settings).first()


def update_settings(db: Session, settings: schemas.SettingsCreate):
    db_settings = get_settings(db)
    if db_settings is None:
        db_settings = models.Settings(**settings.dict())
        db.add(db_settings)
    else:
        for key, value in settings.dict().items():
            setattr(db_settings, key, value)
    db.commit()
    db.refresh(db_settings)
    return db_settings


def get_statistics(db: Session):
    total_owed_to = db.query(models.Debt).filter(models.Debt.debt_type == "owed_to").all()
    total_owed_by = db.query(models.Debt).filter(models.Debt.debt_type == "owed_by").all()
    return {
        "total_owed_to": sum(debt.amount for debt in total_owed_to),
        "total_owed_by": sum(debt.amount for debt in total_owed_by),
        "current_balance": sum(debt.amount for debt in total_owed_to) - sum(debt.amount for debt in total_owed_by)
    }


def create_debt(db: Session, debt: schemas.DebtCreate):
    db_debt = models.Debt(**debt.dict())
    db.add(db_debt)
    db.commit()
    db.refresh(db_debt)
    return db_debt


def update_debt(db: Session, debt_id: int, debt: schemas.DebtCreate):
    db_debt = db.query(models.Debt).filter(models.Debt.id == debt_id).first()
    if not db_debt:
        return None
    for key, value in debt.dict().items():
        setattr(db_debt, key, value)
    db.commit()
    db.refresh(db_debt)
    return db_debt


def delete_debt(db: Session, debt_id: int):
    db_debt = db.query(models.Debt).filter(models.Debt.id == debt_id).first()
    if db_debt:
        db.delete(db_debt)
        db.commit()
    return db_debt


def get_debts(db: Session, debt_type: str = None):
    if debt_type:
        return db.query(models.Debt).filter(models.Debt.debt_type == debt_type).all()
    return db.query(models.Debt).all()
