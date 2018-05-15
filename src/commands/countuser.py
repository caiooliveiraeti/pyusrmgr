from commands.command import Command
from storage.userstorage import UserStorage
from storage.user import UserProfile


class CountSuperUser(Command):

    def __init__(self, user_storage: UserStorage):
        self.user_storage = user_storage

    def execute(self):
        count = self.user_storage.count_by_profile(UserProfile.SUPERUSER)
        print(str(count) + " super usuários")

    def name(self):
        return "countSuper"

    def help(self):
        return "'countSuper' Conta numero de super usuário"
