from typing import List
from src.LIS.wrong.AnimalBaseClass import AnimalBaseClass
from src.LIS.wrong.Bird import Bird
from src.LIS.wrong.Fish import Fish
from src.LIS.wrong.Human import Human

def printNames(animals: List[AnimalBaseClass]) -> None:
    print("printNames...")
    for animal in animals:
        print(f"Hello I am {animal.name}")
    print()

def makeAnimalsFly(animals: List[AnimalBaseClass]) -> None:
    print("makeAnimalsFly...")
    try:
        for animal in animals:
            animal.fly()
    except Exception as e:
        print(f"Something went wrong. {e}\n")


def makeAnimalsSwim(animals: List[AnimalBaseClass]) -> None:
    print("makeAnimalsSwim...")
    try:
        for animal in animals:
            animal.swim()
    except Exception as e:
        print(f"Something went wrong. {e}\n")


def makeAnimalsWalk(animals: List[AnimalBaseClass]) -> None:
    print("makeAnimalsWalk...")
    try:
        for animal in animals:
            animal.walk()
    except Exception as e:
        print(f"Something went wrong. {e}\n")


def main():
    animals: List[AnimalBaseClass] = [Human('Aldo'), Fish('The fish'), Bird('The bird')]

    printNames(animals)
    makeAnimalsFly(animals)
    makeAnimalsSwim(animals)
    makeAnimalsWalk(animals)

main()
