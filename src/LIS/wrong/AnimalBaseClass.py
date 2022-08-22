from abc import ABCMeta, abstractmethod
from dataclasses import dataclass


@dataclass
class AnimalBaseClass(metaclass=ABCMeta):
    name: str

    @classmethod
    def __subclasshook__(cls, subclass):
        return (
            hasattr(subclass, 'walk') and callable(subclass.walk) and
            hasattr(subclass, 'fly') and callable(subclass.fly) and
            hasattr(subclass, 'swim') and callable(subclass.swim) or
            NotImplemented
        )

        @abstractmethod
        def walk(self) -> None:
            raise NotImplementedError

        @abstractmethod
        def fly(self) -> None:
            raise NotImplementedError

        @abstractmethod
        def swim(self) -> None:
            raise NotImplementedError
