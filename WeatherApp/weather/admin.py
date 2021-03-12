from django.contrib import admin
from .models import WeatherTable
from import_export.admin import ImportExportModelAdmin


admin.site.register(WeatherTable)

class WeatherAdmin(ImportExportModelAdmin):
    list_display = ('date','time','t','ran','td','atm_pres','wind_dir','wind_speed','cloudiness','h','vv','wconditions')
    
    
