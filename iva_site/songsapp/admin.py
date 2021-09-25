from django.contrib import admin

from songsapp.models import ContentCategory, Songs

admin.site.register(ContentCategory)

@admin.register(Songs)
class SongsAdmin(admin.ModelAdmin):
    list_display = ('song_name', 'image_album','artist_name','size_music','music_file')
    fields = ('song_name','artist_name', 'image_album',('music_file','size_music'),'category')
    # readonly_fields = ('artist_name',) #если только для чтения
    ordering = ('song_name',) # сортировка от я до а с -
    search_fields = ('song_name',) # поиск