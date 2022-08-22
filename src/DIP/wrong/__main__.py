from src.DIP.wrong.StringEncrypter import StringEncrypter
from src.DIP.wrong.User import User
from src.DIP.wrong.UserPrinter import UserPrinter


def main():
    stringEncrypter = StringEncrypter()
    userPrinter = UserPrinter()

    aldo: User = User('Aldo', 'Fuster Turpin', 25, 'secret', stringEncrypter)
    elliot: User = User('Elliot', 'Alderson', 28, 'I_am_a_great_hacker', stringEncrypter)

    userPrinter.printUserToConsole(aldo)
    userPrinter.printUserToConsole(elliot)

    print(f"Aldo encrypted password: {aldo.encryptPassword()}")
    print(f"Elliot encrypted password: {elliot.encryptPassword()}")



main()
