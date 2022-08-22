from dataclasses import dataclass
from src.DIP.right.stringEncrypter.IStringEncrypter import IStringEncrypter


@dataclass
class User:
    name: str
    surname: str
    age: int
    password: str
    stringEncrypter: IStringEncrypter

    def getStringRepresentation(self) -> str:
        return f"""User information:
        - Name:      {self.name}
        - Surname:   {self.surname}
        - Age:       {self.age}
        - Password:  {self.password}
    """

    def encryptPassword(self) -> str:
        return self.stringEncrypter.encryptString(self.password)
