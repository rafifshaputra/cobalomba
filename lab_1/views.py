from django.shortcuts import render
from django.template import loader
from django.shortcuts import render
from django.http import HttpResponse

from .models import Album

mhs_name = 'Rafif Iqbal Shaputra'

def index(request):
    all_albums = Album.objects.all()
    context = {
        'all_albums' : all_albums,
    }
    return render(request, 'music/index.html', context)

def detail(request,album_id):
    return HttpResponse("<h2>Details for Album id " + str(album_id) + "</h2>")
