from commands.command import Command
from storage.userstorage import UserStorage
from user import *


class AddUser(Command):

    def __init__(self, user_storage: UserStorage):
        self.user_storage = user_storage

    def execute(self):
        user = self.input_user()
        self.user_storage.add(user)

    def name(self):
        return "add"

    def help(self):
        return "'add' Adiciona novo usuário"

    @staticmethod
    def input_user():
        return User(
            input("name: "),
            input("nickname: "),
            input("responsibility: "),
            UserProfile[input("profile: [VISITOR, USER, ADMINISTRATIVE, TECHNICIAN, SUPERUSER] ")],
            input("date_last_access: "),
            input("time_last_access: ")
        )
