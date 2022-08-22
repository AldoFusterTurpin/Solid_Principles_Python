from src.OCP.right.AdminConfigFileReader.GuestAuthorization import GuestAuthorization
from src.OCP.right.AdminConfigFileReader.RegisteredAuthorization import RegisteredAuthorization
from src.OCP.right.AdminConfigFileReader.AdminAuthorization import AdminAuthorization
from src.OCP.right.User import User

from src.OCP.right.UserPrinter import UserPrinter
from src.OCP.right.AdminConfigFile import AdminConfigFile

def main():
    guest: User = User(
        'Guest',
        'Guest',
        None,
        None,
        GuestAuthorization()
    )

    elliot: User = User(
        'Elliot',
        'Alderson',
        28,
        'I_am_a_great_hacker',
        RegisteredAuthorization()
    )

    aldo: User = User(
        'Aldo',
        'Fuster Turpin',
        25,
        'secret',
        AdminAuthorization()
    )

    userPrinter = UserPrinter()
    userPrinter.printUserToConsole(guest)
    userPrinter.printUserToConsole(elliot)
    userPrinter.printUserToConsole(aldo)

    adminConfigurationFile = AdminConfigFile(
        'admin_file.txt',
        'This is the content of a super secret configuration file. 🕵️‍♂️'
    )

    print(guest.readAdminFile(adminConfigurationFile))
    print(elliot.readAdminFile(adminConfigurationFile))
    print(aldo.readAdminFile(adminConfigurationFile))


main()