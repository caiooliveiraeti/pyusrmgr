from storage.userstorage import UserStorage
from storage.user import *
import json
import inspect


class JsonFileUserStorage(UserStorage):

    def __init__(self):
        self.users = []
        self.loadFromFile()

    def add(self, user: User):
        self.users.append(user)
        self.dumpToFile()

    def remove_by_nickname(self, nickname: str):
        self.users = list(filter(lambda user: user.nickname != nickname, self.users))
        self.dumpToFile()

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

    def dumpToFile(self):
        users_file = open('users.json', 'w')
        json_data = json.dumps(self.users, cls=JsonObjectEncoder, indent=2, sort_keys=False)
        users_file.write(json_data)
        users_file.close()

    def loadFromFile(self):
        try:
            users_file = open('users.json', 'r')
            self.users = list(map(lambda user: self.userJsonParser(user), json.load(users_file)))
            users_file.close()
        except FileNotFoundError:
            self.dumpToFile()

    @staticmethod
    def userJsonParser(user):
        user['profile'] = UserProfile[user['profile']]
        return User(**user)


class JsonObjectEncoder(json.JSONEncoder):
    def default(self, obj):
        if hasattr(obj, "to_json"):
            return self.default(obj.to_json())
        elif hasattr(obj, "__dict__"):
            d = {}
            for key, value in inspect.getmembers(obj):
                if not key.startswith("__") \
                        and not inspect.isabstract(value) \
                        and not inspect.isbuiltin(value) \
                        and not inspect.isfunction(value) \
                        and not inspect.isgenerator(value) \
                        and not inspect.isgeneratorfunction(value) \
                        and not inspect.ismethod(value) \
                        and not inspect.ismethoddescriptor(value) \
                        and not inspect.isroutine(value):

                    if isinstance(value, Enum):
                        d[key] = value.name
                    else:
                        d[key] = value

            return self.default(d)
        return obj
