from abc import ABCMeta, abstractmethod


class IWalk(metaclass=ABCMeta):
    @classmethod
    def __subclasshook__(cls, subclass):
        return (hasattr(subclass, 'walk') and callable(subclass.walk) or NotImplemented)

    @abstractmethod
    def walk(self) -> str:
        raise NotImplementedError
