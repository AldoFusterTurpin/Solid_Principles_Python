from src.ISP.right.interfaces.IAnimal import IAnimal
from src.ISP.right.interfaces.IFly import IFly
from src.ISP.right.interfaces.IWalk import IWalk
from dataclasses import dataclass


@dataclass
class Bird(IAnimal, IFly, IWalk):
    name: str

    def getName(self) -> str:
        return self.name

    def walk(self) -> None:
        print("A bird can walk")

    def fly(self) -> None:
        print("A bird can fly")
