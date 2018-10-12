from django.db import models

# Create your models here.
class Movie(models.Model):
    name = models.CharField(max_length=200)
    yearReleased = models.IntegerField()
    ageAllowed = models.IntegerField()
    genre = models.CharField(max_length=200)

    def __str__(self):
        return self.name