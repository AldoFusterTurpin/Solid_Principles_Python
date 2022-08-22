from src.OCP.right.AdminConfigFileReader.IAuthorizationController import IAuthorizationController
from src.OCP.right.AdminConfigFile import AdminConfigFile


class AdminAuthorization(IAuthorizationController):
    def getAuthorizationLevel(self) -> str:
        return "Admin"

    def readAdminFile(self, file: AdminConfigFile) -> str:
        return f"Permission granted ✅. The content of the file {file.name} is:\n{file.content}\n"
