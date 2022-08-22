from src.SRP.right.User import User
from src.SRP.right.StringEncrypter import StringEncrypter
from src.SRP.right.UserPrinter import UserPrinter


def main():
    aldo = User("Aldo", "Fuster Turpin", 25, "secret")
    elliot = User("Elliot", "Alderson", 28, "I_am_a_great_hacker")

    userPrinter = UserPrinter()

    userPrinter.printUserToConsole(aldo)
    userPrinter.printUserToFile(outFileName="aldo.txt", user=aldo)

    print("\n")

    userPrinter.printUserToConsole(elliot)
    userPrinter.printUserToFile(outFileName="elliot.txt", user=elliot)

    stringEncrypter = StringEncrypter()

    aldoPasswordEncrypted = stringEncrypter.encryptString(aldo.password)
    print(f"\nPassword encrypted of {aldo.name} is: {aldoPasswordEncrypted}")

    elliotPasswordEncrypted = stringEncrypter.encryptString(elliot.password)
    print(f"Password encrypted of {elliot.name} is: {elliotPasswordEncrypted}")

main()