from birthday_bot.services.adress_book import AddressBook
from birthday_bot.services.birthdays import Birthdays
from services.cmd_factory import CmdFactory
from views.view import View
from controllers.controller import Controller


def main():
    storage = AddressBook()
    birthdays = Birthdays(storage)
    cmd_factory = CmdFactory(birthdays, storage)
    controller = Controller(cmd_factory)
    view = (View(controller))

    view.start("help")


if __name__ == '__main__':
    main()
