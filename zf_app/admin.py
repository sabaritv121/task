from django.contrib import admin

# Register your models here.
from zf_app import models

admin.site.register(models.Login)
admin.site.register(models.student)
admin.site.register(models.adm)