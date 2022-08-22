from src.DIP.right.User import User

from src.DIP.right.stringEncrypter.IStringEncrypter import IStringEncrypter
from src.DIP.right.stringEncrypter.SimpleStringEncrypter import SimpleStringEncrypter
from src.DIP.right.stringEncrypter.RandomStringEncrypter import RandomStringEncrypter

from src.DIP.right.userPrinter.IUserPrinter import IUserPrinter
from src.DIP.right.userPrinter.UserPrinterConsole import UserPrinterConsole
from src.DIP.right.userPrinter.UserPrinterFile import UserPrinterFile


def main():
    simpleStringEncrypter: IStringEncrypter = SimpleStringEncrypter()
    randomStringEncrypter: IStringEncrypter = RandomStringEncrypter()

    userPrinterConsole: IUserPrinter = UserPrinterConsole()
    userPrinterFile: IUserPrinter = UserPrinterFile()

    aldo: User = User('Aldo', 'Fuster Turpin', 25, 'secret', randomStringEncrypter)
    elliot: User = User('Elliot', 'Alderson', 28, 'I_am_a_great_hacker', simpleStringEncrypter)

    userPrinterConsole.printUser(aldo)
    userPrinterFile.printUser(elliot)

    print(f"Aldo is encrypting the password: {aldo.encryptPassword()}")
    print(f"Elliot is encrypting the password: {elliot.encryptPassword()}")


main()
