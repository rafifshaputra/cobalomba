from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login

from .models import Album


class IndexView(generic.ListView):
    template_name='music/index.html'
    context_object_name = 'all_albums'

    def get_queryset(Self):
        return Album.objects.all()

class DetailView(generic.DetailView):
    model = Album
    template_name= 'music/detail.html'

class AlbumCreate(CreateView):
    model =Album
    template_name= 'music/album_form.html'
    fields=['publisher_lomba','nama_lomba', 'jenis_lomba', 'batas_pendaftaran', 'poster_lomba']

class AlbumUpdate(UpdateView):
    model =Album
    template_name= 'music/album_form.html'
    fields=['publisher_lomba','nama_lomba', 'jenis_lomba', 'batas_pendaftaran', 'poster_lomba']

class AlbumDelete(DeleteView):
    model =Album
    success_url=reverse_lazy('lab-1:index')
