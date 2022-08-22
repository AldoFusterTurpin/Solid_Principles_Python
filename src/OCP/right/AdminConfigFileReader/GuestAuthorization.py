from src.OCP.right.AdminConfigFileReader.IAuthorizationController import IAuthorizationController
from src.OCP.right.AdminConfigFile import AdminConfigFile


class GuestAuthorization(IAuthorizationController):
    def getAuthorizationLevel(self) -> str:
        return "Guest"

    def readAdminFile(self, file: AdminConfigFile) -> str:
        return f"Permission Denied ❌: the user can NOT access the file {file.name} because he/she must be Registered and Admin.\n"
