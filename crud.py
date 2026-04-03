from sqlalchemy.future import select
from models import Task

async def create_task(db, task):
    new_task = Task(
        title=task.title,
        description=task.description
    )

    db.add(new_task)
    await db.commit()
    await db.refresh(new_task)

    return new_task

async def get_tasks(db):
    result = await db.execute(select(Task))
    return result.scalars().all()

async def get_task(db, task_id):
    result = await db.execute(
        select(Task).where(Task.id == task_id)
    )
    return result.scalar_one_or_none()

async def delete_task(db, task):
    await db.delete(task)
    await db.commit()