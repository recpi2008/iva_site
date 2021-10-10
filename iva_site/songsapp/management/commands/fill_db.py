import os
import json
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User
from django.core.management.base import BaseCommand


from songsapp.models import ContentCategory, Songs, Blog

JSON_PATH = 'products/fixtures'


def load_from_json(file_name):
    with open(file_name, mode='r', encoding='utf-8') as infile:

        return json.load(infile)


class Command(BaseCommand):
    def handle(self, *args, **options):
        categories = load_from_json('songsapp/fixtures/categories.json')

        ContentCategory.objects.all().delete()
        for category in categories:
            cat = category.get('fields')
            cat['id'] = category.get('pk')
            new_category = ContentCategory(**cat)
            new_category.save()

        songs = load_from_json('songsapp/fixtures/songs.json')

        Songs.objects.all().delete()
        for product in songs:
            prod = product.get('fields')
            category = prod.get('category')
            _category = ContentCategory.objects.get(id=category)
            prod['category'] =_category
            new_category = Songs(**prod)
            new_category.save()

        blogs = load_from_json('songsapp/fixtures/blogs.json')

        Blog.objects.all().delete()
        for product in blogs:
            prod = product.get('fields')
            category = prod.get('category')
            _category = ContentCategory.objects.get(id=category)
            prod['category'] = _category
            new_category = Blog(**prod)
            new_category.save()
