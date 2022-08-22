from dataclasses import dataclass


@dataclass
class User:
    name: str
    surname: str
    age: int
    password: str

    def getStringRepresentation(self) -> str:
        return f"""User information:
        - Name:      {self.name} 
        - Surname:   {self.surname} 
        - Age:       {self.age} 
        - Password:  {self.password}
    """
