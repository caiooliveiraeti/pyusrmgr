from commands.adduser import AddUser
from commands.getuser import GetUser
from commands.listuser import ListUserByLastAccess
from commands.listuser import ListUserByProfile
from commands.countuser import CountSuperUser
from commands.removeuser import RemoveUser


from storage.memory.user import InMemoryUserStorage


class CommandRunner:
    def __init__(self):
        self.commands = []

    def add(self, command):
        self.commands.append(command)

    def run(self):
        self.printCommands()

        command = input("command: ")
        while command != 'exit':
            self.execute_command(command);
            command = input("command: ")

    def execute_command(self, command: str):
        if command == 'help':
            self.printCommands()

        for c in self.commands:
            if c.name() == command:
                c.execute()

    def printCommands(self):
        for c in self.commands:
            print(c.help())
        print("'help' Lista todos os comandos")

def main():
    user_storage = InMemoryUserStorage()

    runner = CommandRunner()
    runner.add(AddUser(user_storage))
    runner.add(GetUser(user_storage))
    runner.add(ListUserByProfile(user_storage))
    runner.add(ListUserByLastAccess(user_storage))
    runner.add(CountSuperUser(user_storage))
    runner.add(RemoveUser(user_storage))

    runner.run()


if __name__ == '__main__':
    main();
