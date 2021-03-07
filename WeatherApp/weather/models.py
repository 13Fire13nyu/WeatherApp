from django.db import models


class WeatherTable(models.Model):
    
    date = models.CharField(max_length=20)
    time = models.CharField(max_length=5)
    t = models.DecimalField(max_digits=3,decimal_places=1)
    ran = models.DecimalField(max_digits=4,decimal_places=2)
    td = models.DecimalField(max_digits=3,decimal_places=1)
    atm_pres = models.IntegerField()
    wind_dir = models.TextField(blank=True)
    wind_speed = models.TextField(blank=True)
    cloudiness = models.TextField(blank=True)
    h = models.PositiveIntegerField()
    vv = models.TextField(blank=True)
    wconditions = models.CharField(max_length=100)
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        
    def __str__(self):
        return 'Table id: '+str(self.id)
    
    


class UploadTable(models.Model):
    description = models.CharField(max_length=255, blank=True)
    document = models.FileField(upload_to='tables/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    #activated = models.BooleanField(default=False)
    
    def __str__(self):
        return 'File id: '+str(self.id)