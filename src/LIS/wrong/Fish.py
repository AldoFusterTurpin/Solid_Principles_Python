from src.LIS.wrong.AnimalBaseClass import AnimalBaseClass


class Fish(AnimalBaseClass):
    def walk(self) -> None:
        raise NotImplementedError("A fish can NOT walk")

    def fly(self) -> None:
        raise NotImplementedError("A fish can NOT fly")

    def swim(self) -> None:
        print("A fish can swim")
