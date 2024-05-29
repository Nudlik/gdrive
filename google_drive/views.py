from rest_framework import generics, status
from rest_framework.response import Response

from google_drive.serializers import FileCreateSerializer, FilesListSerializer
from google_drive.services import GoogleDriveService


class GdriveView(generics.ListCreateAPIView):
    serializer_class = FileCreateSerializer
    service = GoogleDriveService
    choice_serializer = {
        'GET': FilesListSerializer,
        'POST': FileCreateSerializer,
    }

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.service().upload(serializer.data['name'], serializer.data['data'])
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def get(self, request, *args, **kwargs):
        data = self.service().get_files()

        page = self.paginate_queryset(data)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(data, many=True)
        return Response(serializer.data)

    def get_serializer_class(self, *args, **kwargs):
        return self.choice_serializer.get(self.request.method, self.serializer_class)
