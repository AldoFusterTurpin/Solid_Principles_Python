from src.DIP.wrong.User import User


class UserPrinter():
    def printUserToConsole(self, user: User) -> None:
        print(user.getStringRepresentation() + "\n")

    def printUserToFile(self, outFileName: str, user: User) -> None:
        with open(outFileName, 'w') as f:
            f.write(user.getStringRepresentation())
            print(f"Successfully written user to file {outFileName}")
