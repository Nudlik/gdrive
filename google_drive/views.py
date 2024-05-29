from rest_framework import generics

from google_drive.serializers import GDdriveSerializer
from google_drive.services import GoogleDriveService


class GdriveView(generics.CreateAPIView):
    serializer_class = GDdriveSerializer
    service = GoogleDriveService

    def post(self, request, *args, **kwargs):
        pass
