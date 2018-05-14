from commands.command import Command
from storage.userstorage import UserStorage


class GetUser(Command):

    def __init__(self, user_storage: UserStorage):
        self.user_storage = user_storage

    def execute(self):
        nickname = input("nickname: ")
        user = self.user_storage.find_by_nickname(nickname)
        if user:
            print(str(user))

    def name(self):
        return "get"

    def help(self):
        return "'get' Busca usuário"