import os
import json
from django.shortcuts import render
from django.views.generic import DetailView
from songsapp.models import Songs, ContentCategory, Blog

MODULE_DIR = os.path.dirname(__file__)


def songs(request):
    file_path = os.path.join(MODULE_DIR, 'fixtures/product.json')
    contex = {
        'title': 'AndreyIva - ТРЕКИ',
        'songs': Songs.objects.all(),
    }
    return render(request, 'songsapp/songs.html', contex)


def about(request):
    contex = {
        'title': 'AndreyIva - ОБО МНЕ',
    }
    return render(request, 'songsapp/about.html', contex)

def blog(request):
    contex = {
        'title': 'AndreyIva - БЛОГ',
        'blogs': Blog.objects.all(),
    }
    return render(request, 'songsapp/blog.html', contex)

def contact(request):
    contex = {
        'title': 'AndreyIva - КОНТАКТЫ',
    }
    return render(request, 'songsapp/contact.html', contex)


class ProductDetail(DetailView):
    """
    Контроллер вывода информации о продукте
    """
    model = Blog
    template_name = 'songsapp/blog_detail.html'
    context_object_name = 'blog'


    def get_context_data(self, category_id=None, *args, **kwargs):
        """Добавляем список категорий для вывода сайдбара с категориями на странице каталога"""
        context = super().get_context_data()
        context['categories'] = ContentCategory.objects.all()
        context['title'] = 'AndreyIva - О БЛОГЕ'
        return context


def portfolio(request):
    contex = {
        'title': 'AndreyIva - ТРЕКИ',
    }
    return render(request, 'songsapp/portfolio.html', contex)