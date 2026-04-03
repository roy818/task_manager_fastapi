from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

import crud, schemas
from database import AsyncSessionLocal

router = APIRouter()

async def get_db():
    async with AsyncSessionLocal() as session:
        yield session

@router.post("/tasks")
async def create_task(task: schemas.TaskCreate, db: AsyncSession = Depends(get_db)): # dependency injection
    return await crud.create_task(db, task)

@router.get("/tasks")
async def read_tasks(db: AsyncSession = Depends(get_db)):
    return await crud.get_tasks(db)

@router.get("/tasks/{task_id}")
async def read_task(task_id: int, db: AsyncSession = Depends(get_db)):
    task = await crud.get_task(db, task_id)

    if not task:
        raise HTTPException(status_code=404, detail="Task not found")

    return task