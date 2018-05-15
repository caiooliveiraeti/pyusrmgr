from storage.userstorage import UserStorage
from storage.user import *


class InMemoryUserStorage(UserStorage):

    def __init__(self):
        self.users = []

    def add(self, user: User):
        self.users.append(user)

    def remove_by_nickname(self, nickname: str):
        self.users = list(filter(lambda user: user.nickname != nickname, self.users))

    def find_by_nickname(self, nickname: str):
        users = list(filter(lambda user: user.nickname == nickname, self.users))
        if len(users) > 0:
            return users[0]

    def find_by_profile(self, profile: UserProfile):
        return list(filter(lambda user: user.profile == profile, self.users))

    def find_by_date_last_access(self, date_last_access: str):
        return list(filter(lambda user: user.date_last_access == date_last_access, self.users))

    def count_by_profile(self, profile: UserProfile):
        return len(list(filter(lambda user: user.profile == profile, self.users)))
