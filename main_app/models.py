from django.db import models
from django.urls import reverse

# Create your models here.

OPTIONS = (
    (True, 'Yes'),
    (False,'No')
)

class Album(models.Model):
    title = models.CharField(max_length=100)
    band = models.CharField(max_length=100)
    releaseyear = models.IntegerField()
    price = models.IntegerField()

    def __str__(self):
        return self.title
      
    def get_absolute_url(self):
        return reverse("detail", kwargs={ "album_id": self.id })
    
    
class TrackList(models.Model):
    track = models.CharField('Song', max_length=100)
    single = models.BooleanField(default=False, choices=OPTIONS)
    order = models.IntegerField(default=1)
    
    # create a album_id column in the db
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.track} is track number {self.order}"
