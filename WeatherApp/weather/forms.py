from django import forms
from .models import UploadTable
'''
class TableForm(forms.ModelForm):
    class Meta:
        model = WeatherTable
        fields = ('date','time','t','ran','td','atm_pres','wind_dir','wind_speed','cloudiness','h','vv','wconditions')
 '''       
class UploadTableForm(forms.ModelForm):
    class Meta:
        model = UploadTable
        fields = ('description','document',)
        
        
