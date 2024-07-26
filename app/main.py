from fastapi import FastAPI
from .database import engine, Base
from .endpoints import settings, monitoring, debts

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(settings.router, prefix="/api", tags=["settings"])
app.include_router(monitoring.router, prefix="/api", tags=["monitoring"])
app.include_router(debts.router, prefix="/api", tags=["debts"])
