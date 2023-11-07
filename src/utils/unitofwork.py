from abc import ABC, abstractmethod
from typing import Type

from src.database.db import async_session_maker
# from src.repositories.task_history import TaskHistoryRepository
from src.repositories.tasks import TasksRepository
from src.repositories.users import UsersRepository


class IUnitOfWork(ABC):
    users: Type[UsersRepository]
    tasks: Type[TasksRepository]

    @abstractmethod
    def __int__(self):
        ...

    @abstractmethod
    async def __aenter__(self):
        ...

    @abstractmethod
    async def __aexit__(self, *args):
        ...

    @abstractmethod
    async def commit(self):
        ...

    @abstractmethod
    async def rollback(self):
        ...


class UnitOfWork:
    def __init__(self):
        self.session_factory = async_session_maker

    async def __aenter__(self):
        self.session = self.session_factory()

        self.users = UsersRepository(self.session)
        self.tasks = TasksRepository(self.session)

    async def __aexit__(self, *args):
        await self.rollback()
        await self.session.close()

    async def commit(self):
        await self.session.commit()

    async def rollback(self):
        await self.session.rollback()

