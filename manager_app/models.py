from django.db import models
from django.utils import timezone


class Player(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    jersey_num = models.PositiveIntegerField()
    position = models.CharField(max_length=20)
    dob = models.DateField()
    age = models.PositiveIntegerField()
    height_feet = models.PositiveIntegerField()
    height_inches = models.PositiveIntegerField()
    date_added = models.DateTimeField()
