from django.db import models
from django.core.urlresolvers import reverse

# Red Pk 1
class Album(models.Model):
    nama_lomba = models.CharField(max_length=250)
    jenis_lomba = models.CharField(max_length=500)
    batas_pendaftaran = models.CharField(max_length=100)
    poster_lomba = models.CharField(max_length=1000)
    publisher_lomba=models.CharField(max_length=500 ,default="")

    def get_absolute_url(self):
        return reverse('lab-1:detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.nama_lomba + ' - ' + self.jenis_lomba



class Song(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    file_type = models.CharField(max_length=10)
    song_title = models.CharField(max_length=25)
    is_favorite = models.BooleanField(default=False)

    def __str__(self):
        return self.song_title
