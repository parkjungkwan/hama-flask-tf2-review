from typing import List
from fastapi import APIRouter
from com_sba_api.user.user_dao import UserDao
from com_sba_api.user.user_dto import UserDto

class UserApi(object):
    def __init__(self):
        self.router = APIRouter()

    def getRouter(self):
        return self.router
