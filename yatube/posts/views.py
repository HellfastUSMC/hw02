from django.shortcuts import render
from django.shortcuts import get_object_or_404

from .models import Post
from .models import Group


def index(request):
    template = 'posts/index.html'
    page_title = 'Последние обновления на сайте'
    title = page_title
    posts = Post.objects.order_by('-pub_date')[:10]
    context = {
        'posts': posts,
        'title': title,
        'page_title': page_title,
    }
    return render(request, template, context)


def group_posts(request, slug):
    template = 'posts/group_list.html'
    group = get_object_or_404(Group, slug=slug)
    title = group.title
    posts = group.posts.all().order_by('-pub_date')[:10]
    context = {
        'group_slug': slug,
        'group_ten_posts': posts,
        'group_title': title,
    }
    return render(request, template, context)
