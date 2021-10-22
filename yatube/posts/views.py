from django import template
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.template import loader
from .models import Post, Group

# Create your views here.
def index(request):
    template = 'posts/index.html'
    title = 'Главная Cтраница'
    posts = Post.objects.order_by('-pub_date')[:10]
    context = {
        'posts': posts,
        'title' : title,
    }
    return render(request, template, context)

def group_posts_temp(request):
    template = 'posts/group_list.html'
    title = 'Посты групп'
    info = 'Здесь будет информация о группах проекта Yatube'
    group = Post.group
    group_ten_posts = Post.objects.filter(group=group).order_by('-pub_date')[:10]
    context = {
        'title' : title,
        'info' : info,
        'group_ten_posts' : group_ten_posts,
    }
    return render(request, template, context)

def group_posts(request, slug):
    template = 'posts/group_list.html'
    title = 'Посты групп'
    group = get_object_or_404(Group, slug=slug)
    posts = Post.objects.filter(group=group).order_by('-pub_date')[:10]

    context = {
        'title' : title,
        'group_slug' : slug,
        'group_ten_posts' : posts,
        'group_title': title,
    }
    return render(request, template, context)

def post_detail(request):
    return HttpResponse('Post details') 