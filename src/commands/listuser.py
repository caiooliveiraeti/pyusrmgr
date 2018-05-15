from commands.command import Command
from storage.userstorage import UserStorage
from storage.user import UserProfile


class ListUserByProfile(Command):

    def __init__(self, user_storage: UserStorage):
        self.user_storage = user_storage

    def execute(self):
        profile = UserProfile[input("profile: [VISITOR, USER, ADMINISTRATIVE, TECHNICIAN, SUPERUSER] ")]
        printUsers(self.user_storage.find_by_profile(profile))

    def name(self):
        return "list"

    def help(self):
        return "'list' Lista usuário por nível de acesso"


class ListUserByLastAccess(Command):

    def __init__(self, user_storage: UserStorage):
        self.user_storage = user_storage

    def execute(self):
        date_last_access = input("date_last_access: ")
        printUsers(self.user_storage.find_by_date_last_access(date_last_access))

    def name(self):
        return "listLastAccess"

    def help(self):
        return "'listLastAccess' Lista usuário por data de acesso"


def printUsers(users):
    if len(users) == 0:
        print("Nenhum usuário encontrado")
    else:
        for user in users:
            print(str(user))
            print("------------------------------------")