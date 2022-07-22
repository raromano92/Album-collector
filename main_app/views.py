from ast import Delete
from django.shortcuts import render, redirect

# Create your views here.
from django.http import HttpResponse
from .models import Album, BandMember
from .forms import TrackListForm
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView


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
  # Get the bandmembers the album doesn't have...
  # First, create a list of the member ids that the album DOES have
  id_list = album.band_members.all().values_list('id')
  # Now we can query for members whose ids are not in the list using exclude
  mems_album_doesnt_have = BandMember.objects.exclude(id__in=id_list)
  # instantiate TrackListForm to be rendered in the template
  tracklist_form = TrackListForm()
  return render(request, 'albums/detail.html', {
    'album': album, 'tracklist_form': tracklist_form,
    'bandmems': mems_album_doesnt_have
  })

class AlbumCreate(CreateView):
  model = Album
  fields = '__all__'
  
class AlbumUpdate(UpdateView):
  model = Album
  fields = ['band', 'price']
  
class AlbumDelete(DeleteView):
  model = Album
  success_url = '/albums/'
  
def add_track(request, album_id):
  # create a ModelForm instance using the data in request.POST
  form = TrackListForm(request.POST)
  # validate the form
  if form.is_valid():
    # don't save the form to the db until it
    # has the album_id assigned
    new_track = form.save(commit=False)
    new_track.album_id = album_id
    new_track.save()
  return redirect('detail', album_id=album_id)

class BandMemberList(ListView):
  model = BandMember
  
class BandMemberDetail(DetailView):
  model = BandMember
  
class BandMemberCreate(CreateView):
  model = BandMember
  fields = '__all__'
  
def assoc_mem(request, album_id, bandmember_id):
  Album.objects.get(id=album_id).bandmembers.add(bandmember_id)
  return redirect('detail', album_id=album_id)
