# Generated by Django 3.2.7 on 2021-09-22 13:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ContentCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, unique=True)),
                ('description', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Songs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_album', models.ImageField(blank=True, null=True, upload_to='albums_images')),
                ('song_name', models.CharField(max_length=256)),
                ('artist_name', models.CharField(max_length=256)),
                ('music_file', models.FileField(upload_to='music_file')),
                ('size_music', models.CharField(max_length=64)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='songsapp.contentcategory')),
            ],
        ),
    ]
