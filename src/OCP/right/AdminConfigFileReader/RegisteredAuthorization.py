from src.OCP.right.AdminConfigFileReader.IAuthorizationController import IAuthorizationController
from src.OCP.right.AdminConfigFile import AdminConfigFile


class RegisteredAuthorization(IAuthorizationController):
    def getAuthorizationLevel(self) -> str:
        return "Registered"

    def readAdminFile(self, file: AdminConfigFile) -> str:
        return f"Permission Denied ❌: the user can NOT access the file {file.name} even he/she is registered because he/she must be Admin.\n"