from user import *


class UserStorage:

    def add(self, user: User): pass

    def remove_by_nickname(self, nickname: str): pass

    def find_by_nickname(self, nickname: str): pass

    def find_by_profile(self, profile: UserProfile): pass

    def count_superusers(self): pass
