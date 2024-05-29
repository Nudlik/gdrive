from rest_framework import generics, status
from rest_framework.response import Response

from google_drive.serializers import GDdriveSerializer
from google_drive.services import GoogleDriveService


class GdriveView(generics.CreateAPIView):
    serializer_class = GDdriveSerializer
    service = GoogleDriveService

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.service().upload(serializer.data['name'], serializer.data['data'])
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
