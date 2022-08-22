from src.LIS.wrong.AnimalBaseClass import AnimalBaseClass


class Bird(AnimalBaseClass):
    def walk(self) -> None:
        print("A bird can walk")

    def fly(self) -> None:
        print("A bird can fly")

    def swim(self) -> None:
        raise NotImplementedError("A Bird can not swim")
