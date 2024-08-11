from birthday_bot.services.commands.abstract_cmd import AbstractCmd


class CmdNotFound(AbstractCmd):
    CMD_NAME = 'NOT_FOUND'

    def __init__(self):
        super().__init__()

    def action(self):
        return """WTF, Doc? valid commands only pleazzzzze!
        - help
        - hello
        - exit
        - close 
        - add <name> <phone> 
        - del <name>
        - find <name>
        - append_phone <name> <additional_phone>
        - list
        - birth_add <name> <birth MM.DD>
        - birth_list
        
        - add <name> <not_valid_number, like 3e3> -> to get decorator handled error
        """
