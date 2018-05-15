from storage.user import *


class UserStorage:

    def add(self, user: User): pass

    def remove_by_nickname(self, nickname: str): pass

    def find_by_nickname(self, nickname: str): pass

    def find_by_profile(self, profile: UserProfile): pass

    def find_by_date_last_access(self, date_last_access: str): pass

    def count_by_profile(self): pass
