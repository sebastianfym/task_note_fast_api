from fastapi import APIRouter

from src.api.dependencies import UOWDep
from src.schemas.tasks import TaskSchema, TaskSchemasAction
from src.services.tasks import TaskService

router = APIRouter(
    prefix="/tasks",
    tags=["tasks"]
)


@router.get("")
async def get_tasks(uow: UOWDep):
    tasks = await TaskService.get_tasks(uow=uow)
    return tasks


@router.post("")
async def add_task(uow: UOWDep, task: TaskSchemasAction):
    task = await TaskService.add_task(uow=uow, task=task)
    return {"task_id": task}


@router.patch("/{id}")
async def edit_task(id: int, task: TaskSchemasAction, uow: UOWDep):
    edited_task = await TaskService.edit_task(uow=uow, task=task, task_id=id)
    return {"successfully": True}
