from django.db import transaction
from .models import File

class FileService:
    def upload_file(self, user, file_obj):
        file_size = file_obj.size

        if user.space_left < file_size:
            return None, "Not enough storage space"

        with transaction.atomic():
            file = File.objects.create(
                user=user,
                file=file_obj,
                filename=file_obj.name,
                file_size=file_size
            )
            user.space_left -= file_size
            user.save()

        return file, None

    def list_files(self, user):
        return File.objects.filter(user=user).order_by('-uploaded_at')
