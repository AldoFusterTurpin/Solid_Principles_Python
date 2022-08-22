from src.OCP.wrong.AdminConfigFile import AdminConfigFile
from dataclasses import dataclass
from enum import Enum


class AuthorizationLevel(Enum):
    GUEST = "GUEST"
    REGISTERED = "REGISTERED"
    ADMIN = "ADMIN"


@dataclass
class User:
    name: str
    surname: str
    age: int
    password: str
    authorizationLevel: AuthorizationLevel

    def getStringRepresentation(self) -> str:
        return f"""User information:
        - Name:      {self.name}
        - Surname:   {self.surname}
        - Age:       {self.age}
        - Password:  {self.password}
        - Authorization Level:  {self.authorizationLevel.name}
    """

    def readFileContent(self, file: AdminConfigFile) -> str:
        infoContext = f"{self.name} is trying to read the file {file.name}.\n"

        if self.authorizationLevel == AuthorizationLevel.GUEST:
            return f"{infoContext}Error: {self.name} can NOT access the file {file.name} because he/she must be Registered and Admin.\n"

        if self.authorizationLevel == AuthorizationLevel.REGISTERED:
            return f"{infoContext}Error: {self.name} can NOT access the file {file.name} even he/she is registered because he/she must be Admin.\n"

        if self.authorizationLevel == AuthorizationLevel.ADMIN:
            return f"{infoContext}Permission granted. The content of the file {file.name} is:\n{file.content}\n"
