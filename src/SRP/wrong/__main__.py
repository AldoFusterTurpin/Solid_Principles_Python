from dataclasses import dataclass


@dataclass
class User:
    name: str
    surname: str
    age: int
    password: str

    def printInfo(self) -> None:
        print(f"User information")
        print(f"Name:      {self.name}")
        print(f"Surname:   {self.surname}")
        print(f"Age:       {self.age}")
        print(f"Password: {self.password}")
        print()

    def encryptPassword(self) -> str:
        encrypted_list = []
        password_length = len(self.password)

        for char in self.password:
            encoded_char = char + str(password_length)
            encrypted_list.append(encoded_char)

        return "".join(encrypted_list)


def main():
    aldo = User("Aldo", "Fuster Turpin", 25, "secret")
    aldo.printInfo()
    print(f"Encrypted password of {aldo.name} is: {aldo.encryptPassword()}\n")

    elliot = User("Elliot", "Alderson", 28, "I_am_a_great_hacker")
    elliot.printInfo()
    print(f"Encrypted password of {elliot.name} is: {elliot.encryptPassword()}")


main()