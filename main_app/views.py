from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

# Add the Album class & list and view function below the imports
class Album:
  def __init__(self, title, band, releaseyear, price):
    self.title = title
    self.band = band
    self.releaseyear = releaseyear
    self.price = price

albums = [
  Album("Rumours", "Fleetwood Mac", 1977, 30),
  Album("The Wall", "Pink Floyd", 1979, 40),
  Album("Ride The Lightning", "Metallica", 1984, 25),
  Album("Stadium Arcadium", "Red Hot Chilli Peppers", 2006, 15)
]

# Define the home view
def home(request):
  return HttpResponse('<h1>ALBUMS HOME PAGE</h1>')

def about(request):
  return render(request, 'about.html')

def albums_index(request):
  return render(request, 'albums/index.html', { 'albums': albums })


