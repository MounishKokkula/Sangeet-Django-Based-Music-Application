from django.db import models
from django.urls import reverse
# Create your models here.
# creates a primary key by default for each table
# when you declare a foreign key it is associated with the primary key

class Album(models.Model):
    artist = models.CharField(max_length = 250)
    album_title = models.CharField(max_length = 500)
    genre = models.CharField(max_length = 100)
    album_logo = models.FileField()

    def get_absolute_url(self):
        return reverse('detail',kwargs={'pk':self.pk})

    def __str__(self):
        return self.artist + "  " + self.album_title + "  " +self.genre



class Song(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    file_type = models.CharField(max_length=10)
    song_title = models.CharField(max_length=250)
    is_favorite = models.BooleanField(default=False)

    def __str__(self):
        return self.song_title