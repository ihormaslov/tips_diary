from django.shortcuts import get_object_or_404
from blog.models import Category, Post
from page.models import Page
from utils_main.decorators import render_to


@render_to('page.html')
def page(request, slug):
    page = get_object_or_404(Page, slug=slug)
    posts = Post.objects.filter(publicated=True)
    categories = Category.objects.filter(publicated=True)

    return {'categories': categories, 'page': page, 'posts': posts}

