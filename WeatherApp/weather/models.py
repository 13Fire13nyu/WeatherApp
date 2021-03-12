from django.db import models


class WeatherTable(models.Model):
    
    date_time = models.DateTimeField()
    #time = models.CharField(max_length=5)
    t = models.DecimalField(max_digits=6,decimal_places=1)
    ran = models.DecimalField(max_digits=6,decimal_places=2)
    td = models.DecimalField(max_digits=6,decimal_places=1)
    atm_pres = models.IntegerField()
    wind_dir = models.TextField(blank=True, null=True)
    wind_speed = models.TextField(blank=True, null=True)
    cloudiness = models.TextField(blank=True, null=True)
    h = models.TextField(blank=True, null=True)
    vv = models.TextField(blank=True, null=True)
    wconditions = models.TextField(blank=True, null=True)


    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
   

    def __str__(self):
        return 'Table data: '+ self.date_time

