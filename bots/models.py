from django.db import models

class Bot(models.Model):
    name = models.CharField(max_length=100)
    status = models.CharField(max_length=50, default='idle')

    def __str__(self):
        return self.name
