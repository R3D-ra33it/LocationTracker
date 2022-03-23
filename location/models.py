from django.db import models
# Create your models here.
class locationinfo(models.Model):
    latitude = models.FloatField()
    longitude = models.FloatField()



