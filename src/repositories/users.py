from src.utils.repository import SQLAlchemyRepository
from src.models.users import User


class UsersRepository(SQLAlchemyRepository):
    model = User

