from src.ISP.right.interfaces.IAnimal import IAnimal
from src.ISP.right.interfaces.IFly import IFly
from src.ISP.right.interfaces.ISwim import ISwim
from src.ISP.right.interfaces.IWalk import IWalk
from src.ISP.right.Human import Human
from src.ISP.right.Bird import Bird
from src.ISP.right.Fish import Fish
from typing import List


def printNames(animals: List[IAnimal]) -> None:
    print("printNames...")
    for animal in animals:
        print(f"Hello I am {animal.getName()}")
    print()


def makeAnimalsFly(flyierAnimals: List[IFly]) -> None:
    print("makeAnimalsFly...")
    for animal in flyierAnimals:
        animal.fly()
    print()


def makeAnimalsSwim(swimmerAnimals: List[ISwim]) -> None:
    print("makeAnimalsSwim...")
    for animal in swimmerAnimals:
        animal.swim()
    print()


def makeAnimalsWalk(walkerAnimals: List[IWalk]) -> None:
    print("makeAnimalsWalk...")
    for animal in walkerAnimals:
        animal.walk()
    print()


def main():
    human = Human('Aldo')
    fish = Fish('The fish')
    bird = Bird('The bird')

    animals: List[IAnimal] = [human, fish, bird]
    printNames(animals)

    flyierAnimals: List[IFly] = [bird]
    makeAnimalsFly(flyierAnimals)

    swimmerAnimals: List[ISwim] = [human, fish]
    makeAnimalsSwim(swimmerAnimals)

    walkerAnimals = [human, bird]
    makeAnimalsWalk(walkerAnimals)


main()
