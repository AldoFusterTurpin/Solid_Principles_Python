from abc import ABCMeta, abstractmethod
from src.OCP.right.AdminConfigFile import AdminConfigFile


class IAuthorizationController(metaclass=ABCMeta):
    @classmethod
    def __subclasshook__(cls, subclass):
        return (
            hasattr(subclass, 'getAuthorizationLevel') and callable(subclass.getAuthorizationLevel) and
            hasattr(subclass, 'readAdminFile') and callable(subclass.readAdminFile) or
            NotImplemented
        )

    @abstractmethod
    def getAuthorizationLevel(self) -> str:
        raise NotImplementedError

    @abstractmethod
    def readAdminFile(self, file: AdminConfigFile) -> str:
        raise NotImplementedError
