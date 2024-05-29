from abc import ABC, abstractmethod


class RemoteStorageService(ABC):

    @abstractmethod
    def upload(self, name, data):
        pass


class GoogleDriveService(RemoteStorageService):

    def upload(self, name, data):
        pass
