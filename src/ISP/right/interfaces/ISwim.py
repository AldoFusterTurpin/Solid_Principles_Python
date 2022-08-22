from abc import ABCMeta, abstractmethod


class ISwim(metaclass=ABCMeta):
    @classmethod
    def __subclasshook__(cls, subclass):
        return (hasattr(subclass, 'swim') and callable(subclass.swim) or NotImplemented)

    @abstractmethod
    def swim(self) -> str:
        raise NotImplementedError
