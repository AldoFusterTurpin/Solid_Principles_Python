from src.DIP.right.userPrinter.IUserPrinter import IUserPrinter
from src.SRP.right.User import User



class UserPrinterFile(IUserPrinter):
    def printUser(self, user: User) -> None:
        outFileName = user.name + ".txt"
        with open(outFileName, 'w') as f:
            f.write(user.getStringRepresentation())
            print(f"Successfully written user to file {outFileName}\n")
