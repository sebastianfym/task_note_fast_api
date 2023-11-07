from src.schemas.tasks import TaskSchemasAction
from src.utils.repository import AbstractRepository
from src.utils.unitofwork import IUnitOfWork


class TaskService:
    async def add_task(self, uow: IUnitOfWork, task: TaskSchemasAction):
        task_dict = task.model_dump()

        async with uow:
            task_id = uow.tasks.add_one(task_dict)
            await uow.commit()
            return task_id

    async def get_tasks(self, uow: IUnitOfWork):
        async with uow:
            tasks = uow.tasks.find_all()
            return tasks

    async def edit_task(self, uow: IUnitOfWork, task_id: int, task: TaskSchemasAction):
        tasks_dict = task.model_dump()
        async with uow:
            await uow.tasks.edit_one(task_id, tasks_dict)

            curr_task = await uow.tasks.find_one(id=task_id)
            task_history_log = TaskSchemasAction(
                task_id=task_id,
                previous_assignee_id=curr_task.assignee_id,
                new_assignee_id=task.assignee_id
            )
            task_history_log = task_history_log.model_dump()
            await uow.commit()


