from django.conf.urls import url
from . import views
#url for app

app_name='lab_1'

urlpatterns = [
    # /music/
    url(r'^$', views.IndexView.as_view(), name='index'),


    #/music/<album_id>
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
    #/music/<album_id>/favorite

    url(r'^album/add/$', views.AlbumCreate.as_view(), name='album-add'),

    #/lab-1/album/2/
    url(r'^album/(?P<pk>[0-9]+)/$', views.AlbumUpdate.as_view(), name='album-update'),

    #/lab-1/album/2/delete/
    url(r'^album/(?P<pk>[0-9]+)/delete/$', views.AlbumDelete.as_view(), name='album-delete'),


]
