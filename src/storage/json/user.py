from storage.userstorage import UserStorage
from storage.user import *
import json


class JsonFileUserStorage(UserStorage):

    def __init__(self):
        self.users = []
        self.load_from_file()

    def add(self, user: User):
        self.users.append(user)
        self.dump_to_file()

    def remove_by_nickname(self, nickname: str):
        self.users = list(filter(lambda user: user.nickname != nickname, self.users))
        self.dump_to_file()

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

    def dump_to_file(self):
        users_file = open('users.json', 'w')
        json_data = json.dumps(self.users, cls=JsonUser, indent=2, sort_keys=False)
        users_file.write(json_data)
        users_file.close()

    def load_from_file(self):
        try:
            users_file = open('users.json', 'r')
            self.users = list(map(lambda user: JsonUser.userDecode(user), json.load(users_file)))
            users_file.close()
        except FileNotFoundError:
            self.dump_to_file()


class JsonUser(json.JSONEncoder):
    def default(self, user: User):
        return self.userEncode(user)

    @staticmethod
    def userEncode(user: User):
        return {
            "name": user.name,
            "nickname": user.nickname,
            "responsibility": user.responsibility,
            "profile": user.profile.name,
            "date_last_access": user.date_last_access,
            "time_last_access": user.time_last_access
        }

    @staticmethod
    def userDecode(user):
        user['profile'] = UserProfile[user['profile']]
        return User(**user)
