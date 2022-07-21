from django.contrib import admin

# Register your models here.
from .models import Album, TrackList

admin.site.register(Album)
admin.site.register(TrackList)
