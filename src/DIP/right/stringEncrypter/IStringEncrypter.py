from abc import ABCMeta, abstractmethod


class IStringEncrypter(metaclass=ABCMeta):
    @classmethod
    def __subclasshook__(cls, subclass):
        return (hasattr(subclass, 'encryptString') and callable(subclass.encryptString) or NotImplemented)

    @abstractmethod
    def encryptString(self, toEncrypt: str) -> str:
        raise NotImplementedError
