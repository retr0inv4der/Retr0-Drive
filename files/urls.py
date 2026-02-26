from django.urls import path
from .views import FileUploadView, FileListView, FileDownloadView

urlpatterns = [
    path("upload/", FileUploadView.as_view(), name="file-upload"),
    path("list/", FileListView.as_view(), name="file-list"),
    path("<int:file_id>/download/", FileDownloadView.as_view(), name="file-download"),
]
