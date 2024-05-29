from django.urls import path

from google_drive.views import GdriveView

urlpatterns = [
    path('drive/', GdriveView.as_view()),
]
