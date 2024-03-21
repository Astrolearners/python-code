import colorama
from modules.helpers.logger import logger
from modules.schemas.schemas import commands


class commandHandler():
    def __init__(self):
        self.log = logger("commandHandler")
        self.commands = commands
        colorama.init()

        self.log.info("Command handler ready!")

    def helpCommand(self):
        print(colorama.Fore.RED + "Help" + colorama.Fore.RESET)
        for i in self.commands.keys():
            print(colorama.Fore.BLUE + i + colorama.Fore.RESET +
                  " - " + colorama.Fore.GREEN + self.commands[i])

    def findCommand(self, command):
        try:
            self.commands[command]
            self.log.debug("Command found!")
            return True
        except KeyError:
            self.log.error("Command not found!")
            return False

    def inputShell(self):
        command = input(colorama.Fore.BLUE +
                        "Enter Command >> " + colorama.Fore.RESET)
        if command == "" or command.isspace():
            pass
        elif self.findCommand(command):
            return command
        else:
            return None
