from django.db import models

# Create your models here.
class MO_visitors(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=30)
    email = models.CharField(max_length=100)
    messagge = models.TextField(max_length=600)

    def __str__(self):
        return self.name