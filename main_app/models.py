from django.db import models
from django.urls import reverse
from datetime import date
# Import the User
from django.contrib.auth.models import User

# Create your models here.

class Sub(models.Model):
    aircraft = models.CharField(max_length=50)
    capacity = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.aircraft}, {self.capacity} people'

    def get_absolute_url(self):
        return reverse("detail", kwargs={'pk': self.id})

class Flight(models.Model):
    route = models.CharField(max_length=10)
    airline = models.CharField(max_length=2)
    aircraft = models.CharField(max_length=10)
    number = models.IntegerField(default=0)
    duration = models.IntegerField(default=0)
    # Add the M:M relationship
    subs = models.ManyToManyField(Sub)

    # Add the foreign key linking to a user instance
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.route

    def get_absolute_url(self):
        return reverse("detail", kwargs={'flight_id': self.id})

class History(models.Model):
    TYPES = (
        ('O','On-Time'),
        ('D','Delayed'),
        ('C','Cancelled'),
    )
    date = models.DateField('history date')
    status = models.CharField(
        max_length=1,
        choices=TYPES,
        default=TYPES[0][0]
    )
    # Create a flight_id FK
    flight = models.ForeignKey(Flight, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.status} on {self.date}"

    # change the default sort
    class Meta:
        ordering = ['-date']
