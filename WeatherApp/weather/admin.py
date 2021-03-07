from django.contrib import admin
from .models import WeatherTable, UploadTable
# Register your models here.

admin.site.register(WeatherTable)
admin.site.register(UploadTable)