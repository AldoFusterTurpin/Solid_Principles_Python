from abc import ABCMeta, abstractmethod
from src.DIP.right.User import User


class IUserPrinter(metaclass=ABCMeta):
    @classmethod
    def __subclasshook__(cls, subclass):
        return (hasattr(subclass, 'printUser') and callable(subclass.printUser) or NotImplemented)

    @abstractmethod
    def printUser(self, user: User) -> None:
        raise NotImplementedError
