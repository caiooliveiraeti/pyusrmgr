from enum import Enum


class UserProfile(Enum):
    VISITOR = "visitante"
    USER = "usuário"
    ADMINISTRATIVE = "administrativo"
    TECHNICIAN = "técnico"
    SUPERUSER = "super-usuário"


class User:

    def __init__(self, name: str, nickname: str, responsibility: str, profile: UserProfile,
                 date_last_access: str, time_last_access: str):
        self.name = name
        self.nickname = nickname
        self.responsibility = responsibility
        self.profile = profile
        self.date_last_access = date_last_access
        self.time_last_access = time_last_access

    def __str__(self):
        return f'name: {self.name} \n' \
               f'nickname: {self.nickname} \n' \
               f'responsibility: {self.responsibility} \n' \
               f'profile: {self.profile.name} \n' \
               f'date_last_access: {self.date_last_access} \n' \
               f'time_last_access: {self.time_last_access}'
