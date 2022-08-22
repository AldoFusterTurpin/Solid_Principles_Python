from src.OCP.wrong.AdminConfigFile import AdminConfigFile
from src.OCP.wrong.StringEncrypter import StringEncrypter
from src.OCP.wrong.User import User, AuthorizationLevel
from src.OCP.wrong.UserPrinter import UserPrinter


def main():
    guest: User = User('Guest', 'Guest', None, None, AuthorizationLevel.GUEST)

    elliot: User = User('Elliot', 'Alderson', 28, 'I_am_a_great_hacker', AuthorizationLevel.REGISTERED)

    aldo: User = User('Aldo', 'Fuster Turpin', 25, 'secret', AuthorizationLevel.ADMIN)

    userPrinter = UserPrinter()
    userPrinter.printUserToConsole(guest)
    userPrinter.printUserToConsole(elliot)
    userPrinter.printUserToConsole(aldo)

    adminConfigurationFile = AdminConfigFile(
        name='admin_file.txt',
        content='This is the content of a super secret configuration file. 🕵️‍♂️'
    )

    print(guest.readFileContent(adminConfigurationFile))
    print(elliot.readFileContent(adminConfigurationFile))
    print(aldo.readFileContent(adminConfigurationFile))


main()