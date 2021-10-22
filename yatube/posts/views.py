from django import template
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Post, Group

# Create your views here.


def index(request):
    template = 'posts/index.html'
    title = 'Последние обновления на сайте'
    posts = Post.objects.order_by('-pub_date')[:10]
    context = {
        'posts': posts,
        'title': title,
    }
    return render(request, template, context)


def group_posts(request, slug):
    template = 'posts/group_list.html'
    group = get_object_or_404(Group, slug=slug)
    title = group.title
    posts = Post.objects.filter(group=group).order_by('-pub_date')[:10]

    context = {
        'title': title,
        'group_slug': slug,
        'group_ten_posts': posts,
        'group_title': title,
    }
    return render(request, template, context)


def post_detail(request):
    return HttpResponse('Post details')
