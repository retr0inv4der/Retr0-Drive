from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from django.http import FileResponse

from .serializers import FileSerializer
from .FileService import FileService

class FileUploadView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        file_obj = request.FILES.get('file')

        if not file_obj:
            return Response({
                "error": "No file provided"
            }, status=status.HTTP_400_BAD_REQUEST)

        service = FileService()
        file, error = service.upload_file(request.user, file_obj)

        if error:
            return Response({
                "error": error,
                "space_left": request.user.space_left,
                "file_size": file_obj.size
            }, status=status.HTTP_400_BAD_REQUEST)

        serializer = FileSerializer(file)
        return Response({
            "message": "File uploaded successfully",
            "file": serializer.data,
            "space_left": request.user.space_left
        }, status=status.HTTP_201_CREATED)


class FileListView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        service = FileService()
        files = service.list_files(request.user)
        serializer = FileSerializer(files, many=True)
        return Response({
            "files": serializer.data
        }, status=status.HTTP_200_OK)


class FileDownloadView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, file_id):
        service = FileService()
        file, error = service.get_file_for_download(request.user, file_id)

        if error:
            return Response({
                "error": error
            }, status=status.HTTP_404_NOT_FOUND)

        response = FileResponse(
            file.file,
            as_attachment=True,
            filename=file.filename
        )
        response['Content-Length'] = file.file_size
        return response
