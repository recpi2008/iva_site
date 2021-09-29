from django.contrib import admin

from songsapp.models import ContentCategory, Songs, Blog

admin.site.register(ContentCategory)

@admin.register(Songs)
class SongsAdmin(admin.ModelAdmin):
    list_display = ('song_name', 'image_album','artist_name','size_music','music_file')
    fields = ('song_name','artist_name', 'image_album',('music_file','size_music'),'category')
    # readonly_fields = ('artist_name',) #если только для чтения
    ordering = ('song_name',) # сортировка от я до а с -
    search_fields = ('song_name',) # поиск

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('blog_name','image_blog', 'blog_desription','blog_duration','blog_type','blog_date',
                    'in_main_image','in_one_image','in_two_image','in_paragraph_one','in_paragraph_two',
                    'in_paragraph_three','in_paragraph_four','category')
    fields = ('blog_name','image_blog', 'blog_desription','blog_duration','blog_type','blog_date',
                    'in_main_image','in_one_image','in_two_image','in_paragraph_one','in_paragraph_two',
                    'in_paragraph_three','in_paragraph_four','category')
