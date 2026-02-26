from django.db import models
from users.models import Users

def user_file_path(instance, filename):
    return f'users/{instance.user.id}/{filename}'

class File(models.Model):
    user = models.ForeignKey(Users, on_delete=models.CASCADE, related_name='files')
    file = models.FileField(upload_to=user_file_path)
    filename = models.CharField(max_length=255)
    file_size = models.BigIntegerField()
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.filename
