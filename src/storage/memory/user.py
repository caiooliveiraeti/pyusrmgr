from storage.userstorage import UserStorage
from user import *


class InMemoryUserStorage(UserStorage):

    def __init__(self):
        self.commands = []

    def add(self, user: User):
        print("You're a loony.")

    def remove_by_nickname(self, nickname: str):
        print("You're a loony.")

    def find_by_nickname(self, nickname: str):
        print("You're a loony.")

    def find_by_profile(self, profile: UserProfile):
        print("You're a loony.")

    def count_superusers(self):
        print("You're a loony.")
