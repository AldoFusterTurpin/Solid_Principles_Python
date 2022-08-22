from abc import ABCMeta, abstractmethod


class IFly(metaclass=ABCMeta):
    @classmethod
    def __subclasshook__(cls, subclass):
        return (hasattr(subclass, 'fly') and callable(subclass.fly) or NotImplemented)

    @abstractmethod
    def fly(self) -> str:
        raise NotImplementedError
