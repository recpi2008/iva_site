import single as single
from django.db import models


class ContentCategory(models.Model):
    name = models.CharField(max_length=64, unique=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


class Songs(models.Model):
    image_album = models.ImageField(upload_to='albums_images', blank=True, null=True)
    song_name = models.CharField(max_length=256, blank=True, null=True)
    artist_name = models.CharField(max_length=256, blank=True, null=True)
    music_file = models.FileField(upload_to='music_file', blank=True, null=True)
    size_music = models.CharField(max_length=64, blank=True, null=True)
    category = models.ForeignKey(ContentCategory, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.song_name} | {self.category.name}'


class Blog(models.Model):
    blog_name = models.CharField(verbose_name='Имя блога', max_length=64, blank=True, null=True)
    image_blog = models.ImageField(verbose_name='Фото блога',upload_to='blog_images', blank=True, null=True)
    blog_desription = models.CharField(verbose_name='Описание блога', max_length=256, blank=True, null=True)
    blog_duration = models.CharField(verbose_name='Продолжительность',max_length=32, blank=True, null=True)
    blog_type = models.CharField(verbose_name='Тип блога',max_length=32, blank=True, null=True)
    blog_date = models.CharField(verbose_name='Дата блога',max_length=32, blank=True, null=True)
    url_video = models.URLField(verbose_name='Ссылка видео', blank=True, null=True)
    in_one_image = models.ImageField(verbose_name='Первое фото внутри',upload_to='blog_images', blank=True, null=True)
    in_two_image = models.ImageField(verbose_name='Второе фото внутри',upload_to='blog_images', blank=True, null=True)
    in_paragraph_one = models.CharField(verbose_name='Первый заголовок', max_length=256, blank=True, null=True)
    in_paragraph_two = models.TextField(verbose_name='Первое описание', blank=True, null=True)
    in_paragraph_three = models.CharField(verbose_name='Второй заголовок', max_length=256, blank=True, null=True)
    in_paragraph_four = models.TextField(verbose_name='Второе описание', blank=True, null=True)
    category = models.ForeignKey(ContentCategory, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.blog_name} | {self.category.name}'
