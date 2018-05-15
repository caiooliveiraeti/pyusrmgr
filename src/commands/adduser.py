from commands.command import Command
from storage.userstorage import UserStorage
from storage.user import *


class AddUser(Command):

    def __init__(self, user_storage: UserStorage):
        self.user_storage = user_storage

    def execute(self):
        user_input = self.input_user()
        user = self.user_storage.find_by_nickname(user_input.nickname)
        if user:
            print("Usuário " + user.nickname + " já existe")
        else:
            self.user_storage.add(user_input)

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
