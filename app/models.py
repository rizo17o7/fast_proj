from sqlalchemy import Column, Integer, String, Float, DateTime
from .database import Base


class Debt(Base):
    __tablename__ = "debts"

    id = Column(Integer, primary_key=True, index=True)
    debt_type = Column(String, index=True)
    name = Column(String, index=True)
    amount = Column(Float)
    currency = Column(String)
    description = Column(String, index=True, nullable=True)
    date_incurred = Column(DateTime)
    date_due = Column(DateTime, nullable=True)


class Settings(Base):
    __tablename__ = "settings"

    id = Column(Integer, primary_key=True, index=True)
    currency = Column(String)
    reminder_time = Column(Integer)
