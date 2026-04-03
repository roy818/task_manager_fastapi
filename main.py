from fastapi import FastAPI
from database import engine
from models import Base
from routers.task_router import router   # import router

app = FastAPI()


async def create_tables():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)


@app.on_event("startup")
async def startup():
    await create_tables()

# REGISTER ROUTER
app.include_router(router)

@app.get("/")
async def root():
    return {"message": "FastAPI running"}