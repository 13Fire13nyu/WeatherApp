from import_export import resources
from .models import WeatherTable

class WeatherResource(resources.ModelResource):
    class meta:
        model = WeatherTable