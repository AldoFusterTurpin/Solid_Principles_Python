from src.OCP.right.AdminConfigFile import AdminConfigFile
from src.OCP.right.AdminConfigFileReader.IAuthorizationController import IAuthorizationController
from dataclasses import dataclass


@dataclass
class User:
    name: str
    surname: str
    age: int
    password: str
    userAuthreader: IAuthorizationController

    def getStringRepresentation(self) -> str:
        return f"""User information:
        - Name:      {self.name}
        - Surname:   {self.surname}
        - Age:       {self.age}
        - Password:  {self.password}
        - Authorization Level:  {self.userAuthreader.getAuthorizationLevel()}
    """

    def readAdminFile(self, file: AdminConfigFile) -> str:
        infoContext = f"{self.name} is trying to read the file {file.name}.\n"
        fileContent = self.userAuthreader.readAdminFile(file)

        return infoContext + fileContent
