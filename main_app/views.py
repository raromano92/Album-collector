from ast import Delete
from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import Album
from .forms import TrackListForm
from django.views.generic.edit import CreateView, UpdateView, DeleteView

# Define the home view
def home(request):
  return render(request, 'albums/home.html')

def about(request):
  return render(request, 'about.html')

def albums_index(request):
  albums = Album.objects.all()
  return render(request, 'albums/index.html', { 'albums': albums })

def albums_detail(request, album_id):
  album = Album.objects.get(id=album_id)
  # instantiate TrackListForm to be rendered in the template
  tracklist_form = TrackListForm()
  return render(request, 'albums/detail.html', { 'album': album, 'tracklist_form': tracklist_form })

class AlbumCreate(CreateView):
  model = Album
  fields = '__all__'
  
class AlbumUpdate(UpdateView):
  model = Album
  fields = ['band', 'price']
  
class AlbumDelete(DeleteView):
  model = Album
  success_url = '/albums/'
  


