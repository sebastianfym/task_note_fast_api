from src.models.tasks import Task
from src.utils.repository import SQLAlchemyRepository


class TasksRepository(SQLAlchemyRepository):
    model = Task
