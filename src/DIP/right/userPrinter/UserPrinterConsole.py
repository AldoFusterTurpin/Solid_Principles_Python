from src.DIP.right.userPrinter.IUserPrinter import IUserPrinter
from src.DIP.right.User import User



class UserPrinterConsole(IUserPrinter):
    def printUser(self, user: User) -> None:
        print(f"{user.getStringRepresentation()}")
