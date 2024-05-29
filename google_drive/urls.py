from django.urls import path

from google_drive.views import GDriveView

urlpatterns = [
    path('gdrive/', GDriveView.as_view(), name='gdrive'),
]
