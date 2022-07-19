from django.db import models
from django.urls import reverse

# Create your models here.
class Album(models.Model):
    title = models.CharField(max_length=100)
    band = models.CharField(max_length=100)
    releaseyear = models.IntegerField()
    price = models.IntegerField()

    def __str__(self):
        return self.title
      
    def get_absolute_url(self):
        return reverse("detail", kwargs={ "album_id": self.id })
    
