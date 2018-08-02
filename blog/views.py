import logging

from django.shortcuts import get_object_or_404
from blog.models import Category, Post
from blog.utils import pagination
from utils_main.decorators import render_to


logger = logging.getLogger('django.request')


@render_to('blog/index.html')
def index(request):
    categories = Category.objects.filter(publicated=True)
    posts = Post.objects.filter(publicated=True)
    most_viewed = posts.order_by('?')[:10]

    page = pagination(request, posts, 15)
    if request.GET.get('json'):
        return page

    return {'categories': categories, 'most_viewed': most_viewed, 'page': page}


@render_to('blog/category.html')
def category(request, slug):
    categories = Category.objects.filter(publicated=True)
    category = get_object_or_404(Category, slug=slug)
    posts = Post.objects.filter(category=category, publicated=True)
    most_viewed = posts.order_by('?')[:10]

    page = pagination(request, posts, 15)
    if request.GET.get('json'):
        return page

    return {'categories': categories, 'category': category, 'most_viewed': most_viewed, 'page': page}


@render_to('blog/post.html')
def post(request, slug):
    post = get_object_or_404(Post, slug=slug)
    categories = Category.objects.filter(publicated=True)
    related_posts = Post.objects.filter(category=post.category, publicated=True).exclude(id=post.id)[:10]

    request.session.set_test_cookie()
    if request.session.test_cookie_worked():
        request.session.delete_test_cookie()
        viewed_posts = set(request.session.get('viewed_posts', set()))
        if post.id not in viewed_posts:
            post.increase_views_count()
            viewed_posts.update((post.id, ))
            request.session['viewed_posts'] = list(viewed_posts)

    return {'categories': categories, 'related_posts': related_posts,'post': post}

@render_to('blog/search.html')
def search(request):
    return {}
