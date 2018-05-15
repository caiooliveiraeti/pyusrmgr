from commands.command import Command
from storage.userstorage import UserStorage


class RemoveUser(Command):

    def __init__(self, user_storage: UserStorage):
        self.user_storage = user_storage

    def execute(self):
        nickname = input("nickname: ")
        user = self.user_storage.find_by_nickname(nickname)
        if user:
            print("Deseja excluir o usuário: ")
            print(str(user))
            if input("S/N: ") == "S":
                self.user_storage.remove_by_nickname(nickname)
        else:
            print("Usuário não encontrado")

    def name(self):
        return "remove"

    def help(self):
        return "'remove' Remove usuário por nickname"
