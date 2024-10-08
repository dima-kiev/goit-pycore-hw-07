from birthday_bot.services.commands.cmd_add import CmdAdd
from birthday_bot.services.commands.cmd_birth_add import CmdBirthAdd
from birthday_bot.services.commands.cmd_birth_list import CmdBirthList
from birthday_bot.services.commands.cmd_del import CmdDel
from birthday_bot.services.commands.cmd_edit import CmdEdit
from birthday_bot.services.commands.cmd_exit import CmdExit
from birthday_bot.services.commands.cmd_find import CmdFind
from birthday_bot.services.commands.cmd_hello import CmdHello
from birthday_bot.services.commands.cmd_list import CmdList
from birthday_bot.services.commands.cmd_not_found import CmdNotFound


class CmdFactory:

    def __init__(self, birth_service, storage):
        self.birth_service = birth_service
        self.storage = storage
        self.__init_commands()

    def find_command(self, user_inp: str):
        for cmd_name in self.commands:
            if user_inp.startswith(cmd_name):
                return self.commands[cmd_name]
        return self.commands.get(CmdNotFound.CMD_NAME)

    def __init_commands(self):
        self.commands = dict()
        self.commands[CmdNotFound.CMD_NAME] = CmdNotFound()
        self.commands[CmdHello.CMD_NAME] = CmdHello()
        self.commands[CmdAdd.CMD_NAME] = CmdAdd(self.storage)
        self.commands[CmdEdit.CMD_NAME] = CmdEdit(self.storage)
        self.commands[CmdFind.CMD_NAME] = CmdFind(self.storage)
        self.commands[CmdList.CMD_NAME] = CmdList(self.storage)
        self.commands[CmdDel.CMD_NAME] = CmdDel(self.storage)
        self.commands[CmdBirthAdd.CMD_NAME] = CmdBirthAdd(self.storage)
        self.commands[CmdBirthList.CMD_NAME] = CmdBirthList(self.birth_service)
        self.commands[CmdExit.CMD_NAME] = CmdExit()
        self.commands["close"] = self.commands.get(CmdExit.CMD_NAME)
        self.commands["help"] = self.commands.get(CmdNotFound.CMD_NAME)
