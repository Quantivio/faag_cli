from app.dao import SampleDao
from app.schemas import UserResponseSchema


class SampleService:
    def __init__(self):
        self.sampleDao = SampleDao()

    def get_all_users(self) -> list[UserResponseSchema]:
        raw_users = self.sampleDao.get_all_users()
        users: list[UserResponseSchema] = [UserResponseSchema.parse_obj(user) for user in raw_users]
        return users
