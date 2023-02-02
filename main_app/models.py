from django.db import models

# Create your models here.

class Flight(models.Model):
    route = models.CharField(max_length=10)
    airline = models.CharField(max_length=2)
    aircraft = models.CharField(max_length=10)
    number = models.IntegerField(default=0)
    duration = models.IntegerField(default=0)

    def __str__(self):
        return self.route