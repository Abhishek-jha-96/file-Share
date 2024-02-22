from django.contrib import admin
from .models import OperationalUser, ClientUser, File
# Register your models here.

admin.site.register(OperationalUser)
admin.site.register(ClientUser)
admin.site.register(File)
