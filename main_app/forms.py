from django.forms import ModelForm
from .models import TrackList

class TrackListForm(ModelForm):
  class Meta:
    model = TrackList
    fields = ['order', 'track', 'single']