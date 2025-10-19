from django.db import models

class Url(models.Model):
    link = models.CharField(max_length=2000)
    uid = models.CharField(max_length=10, unique=True)

    def __str__(self):
        return f"{self.link}"