from src.ISP.right.interfaces.ISwim import ISwim
from src.ISP.right.interfaces.IAnimal import IAnimal
from dataclasses import dataclass


@dataclass
class Fish(IAnimal, ISwim):
    name: str

    def getName(self) -> str:
        return self.name

    def swim(self) -> None:
        print("A fish can swim")
