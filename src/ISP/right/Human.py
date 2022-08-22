from src.ISP.right.interfaces.IAnimal import IAnimal
from src.ISP.right.interfaces.ISwim import ISwim
from src.ISP.right.interfaces.IWalk import IWalk
from dataclasses import dataclass


@dataclass
class Human(IAnimal, ISwim, IWalk):
    name: str

    def getName(self) -> str:
        return self.name

    def swim(self) -> None:
        print("A human can swim")

    def walk(self) -> None:
        print("A human can walk")
