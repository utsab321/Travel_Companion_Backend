from django.db import models
class Destination(models.Model):
    name = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    description = models.TextField()
   

    def __str__(self):
        return f"{self.name}, {self.country} "
# Create your models here.
