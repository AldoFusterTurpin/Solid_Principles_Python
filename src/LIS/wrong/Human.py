from src.LIS.wrong.AnimalBaseClass import AnimalBaseClass


class Human(AnimalBaseClass):
    def walk(self) -> None:
        print("A human can walk")

    def fly(self) -> None:
        raise NotImplementedError("A human can NOT fly")

    def swim(self) -> None:
        print("A human can swim")
