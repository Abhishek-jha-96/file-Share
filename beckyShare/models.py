from django.db import models

# Create your models here.
class OperationalUser(models.Model):
    email = models.EmailField(max_length=255, unique=True)
    password = models.CharField(max_length=255, blank=False)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['email', 'password']

    def __str__(self):
        return self.email

class ClientUser(models.Model):
    email = models.EmailField(max_length=255, unique=True)
    password = models.CharField(max_length=128)
    is_active = models.BooleanField(default=True)
    is_verified = models.BooleanField(default=False)
    verification_token = models.CharField(max_length=255)

    def __str__(self):
        return self.email  

class File(models.Model):
    uploaded_by = models.ForeignKey(OperationalUser, on_delete=models.CASCADE)
    file = models.FileField(upload_to='uploads/')
    name = models.CharField(max_length=255)
    file_type = models.CharField(max_length=10, choices=[('docx', 'docx'), ('xlsx', 'xlsx'), ('pptx', 'pptx')])
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name