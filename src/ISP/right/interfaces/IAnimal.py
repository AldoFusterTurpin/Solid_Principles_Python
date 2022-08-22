from abc import ABCMeta, abstractmethod


class IAnimal(metaclass=ABCMeta):
    @classmethod
    def __subclasshook__(cls, subclass):
        return (hasattr(subclass, 'getName') and callable(subclass.getName) or NotImplemented)

    @abstractmethod
    def getName(self) -> str:
        raise NotImplementedError
