import tempfile
from abc import ABC, abstractmethod

from google.oauth2 import service_account
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload

from config.settings import SERVICE_ACCOUNT_FILE, SCOPES, FOLDER_ID


class RemoteStorageService(ABC):
    """ "Огрызок" абстрактного интерфейса """

    @abstractmethod
    def upload(self, name, data):
        pass


class GoogleDriveService(RemoteStorageService):
    """ Реализация абстрактного интерфейса посредством Google Drive API """

    __credentials = service_account.Credentials.from_service_account_file(
        filename=SERVICE_ACCOUNT_FILE,
        scopes=SCOPES,
    )
    __service = build('drive', 'v3', credentials=__credentials)

    def upload(self, name, data):
        """ Загрузка файла в Google Drive """

        file_metadata = {
            'name': name,
            'parents': [FOLDER_ID]
        }

        # уж не знаю на сколько целесообразно это вынести в селери, надо замерять производительность
        with tempfile.NamedTemporaryFile(delete=False) as tmp_file:
            tmp_file.write(data.encode())
            tmp_file.flush()
            media = MediaFileUpload(tmp_file.name, resumable=True)

        file = self.__service.files().create(body=file_metadata, media_body=media, fields='id').execute()
        return file.get('id')

    def get_files(self):
        """ Получение списка файла в Google Drive """

        results = self.__service.files().list(
            pageSize=10,
            fields='nextPageToken, files(id, name, mimeType)'
        ).execute()
        return results.get('files')
