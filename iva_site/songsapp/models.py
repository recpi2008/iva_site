from django.db import models

class ContentCategory(models.Model):
    name = models.CharField(max_length=64, unique=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

class Songs(models.Model):
    image_album = models.ImageField(upload_to='albums_images', blank=True, null=True)
    song_name = models.CharField(max_length=256)
    artist_name = models.CharField(max_length=256)
    music_file = models.FileField(upload_to='music_file')
    size_music = models.CharField(max_length=64)
    category = models.ForeignKey(ContentCategory, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.song_name} | {self.category.name}'

