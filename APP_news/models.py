from django.db import models
import datetime

# Create your models here.
class MO_news(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='APP_med_news/images')
    date = models.DateField(default=datetime.date.today)

    def __str__(self):
        return self.title