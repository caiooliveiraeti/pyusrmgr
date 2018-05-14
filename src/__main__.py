from commands.adduser import AddUser
from commands.getuser import GetUser
from storage.memory.user import InMemoryUserStorage


class CommandRunner:
    def __init__(self):
        self.commands = []

    def add(self, command):
        self.commands.append(command)

    def run(self):
        for c in self.commands:
            print(c.help())

        command = input("command: ")
        while command != 'exit':
            self.execute_command(command);
            command = input("command: ")

    def execute_command(self, command: str):
        for c in self.commands:
            if c.name() == command:
                c.execute()


def main():
    user_storage = InMemoryUserStorage()

    runner = CommandRunner()
    runner.add(AddUser(user_storage))
    runner.add(GetUser(user_storage))
    runner.run()


if __name__ == '__main__':
    main();
