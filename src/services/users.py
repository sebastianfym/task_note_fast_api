from src.schemas.users import UserSchemaAdd, UserSchema
from src.utils.unitofwork import IUnitOfWork


class UserService:
    async def add_user(self, uow: IUnitOfWork, user: UserSchemaAdd):
        user_dict = user.model_dump()

        async with uow:
            user_id = await uow.users.add_one(user_dict)
            await uow.commit()
            return user_id

    async def get_users(self, uow: IUnitOfWork):
        async with uow:
            users = await uow.users.find_all()
            return users

    async def get_user(self, uow: IUnitOfWork, user_id: int, user: UserSchema):
        async with uow:
            user = await uow.users.find_one(id=user_id)
            return user
