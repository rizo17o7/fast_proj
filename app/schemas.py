from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class DebtBase(BaseModel):
    debt_type: str
    name: str
    amount: float
    currency: str
    description: Optional[str] = None
    date_incurred: datetime
    date_due: Optional[datetime] = None


class DebtCreate(DebtBase):
    pass


class Debt(DebtBase):
    id: int

    class Config:
        orm_mode = True


class SettingsBase(BaseModel):
    currency: str
    reminder_time: int


class SettingsCreate(SettingsBase):
    pass


class Settings(SettingsBase):
    id: int

    class Config:
        orm_mode = True
