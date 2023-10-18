from django.db import models

class Moviedata(models.Model):
    def __str__(self):
        return self.name

    name=models.CharField(max_length=255)
    duration = models.FloatField()
    rating = models.FloatField()