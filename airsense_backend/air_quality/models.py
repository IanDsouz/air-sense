from django.db import models

class AirQualityReading(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)
    temperature = models.FloatField()
    humidity = models.FloatField()
    co2 = models.IntegerField()
