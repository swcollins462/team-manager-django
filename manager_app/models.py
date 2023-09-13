from django.db import models
from datetime import date


class Player(models.Model):
    first_name = models.CharField(max_length=35)
    last_name = models.CharField(max_length=35)
    jersey_num = models.CharField(max_length=3)
    position = models.CharField(max_length=20)
    born = models.DateField()
    height_feet = models.PositiveIntegerField()
    height_inches = models.PositiveIntegerField()
    weight = models.CharField(max_length=3)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    def calculate_age(self, born):
        today = date.today()
        return today.year - born.year - ((today.month, today.day) < (born.month, born.day))

    @property
    def player_age(self):
        age = self.calculate_age(self.born)
        return age
