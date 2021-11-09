from re import template
from django.contrib.auth import get_user_model
from django.core.paginator import Paginator
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.shortcuts import get_object_or_404

from . import forms
from .models import Post
from .models import Group

User = get_user_model()


def index(request):
    template = 'posts/index.html'
    page_title = 'Главная страница Yatube'
    title = 'Последние обновления на сайте'
    posts = Post.objects.order_by('-pub_date')
    paginator = Paginator(posts, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'posts': page_obj,
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


def profile(request, username):
    template = 'posts/profile.html'
    user_c = get_object_or_404(User, username=username)
    posts = user_c.posts.all().order_by('-pub_date')
    paginator = Paginator(posts, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    posts_total = posts.count()
    user_name = f'{user_c.first_name} {user_c.last_name}'
    title = f'Профайл пользователя {user_name}'
    context = {
        'title': title,
        'posts': page_obj,
        'user': user_c,
        'posts_total': posts_total,
        'user_name': user_name
    }
    return render(request, template, context)


def post_detail(request, post_id):
    template = 'posts/post_detail.html'
    post = get_object_or_404(Post, pk=post_id)
    group = post.group
    author = f'{post.author.first_name} {post.author.last_name}'
    date = post.pub_date
    posts_count = post.author.posts.count()
    title = f'Пост {post.text[:30]}'
    username = post.author.username
    text = post.text
    context = {
        'title': title,
        'author': author,
        'group': group,
        'date': date,
        'posts_count': posts_count,
        'username': username,
        'text': text,
    }
    return render(request, template, context)


def post_create(request):
    if request.user.is_authenticated:
        template = 'posts/create_post.html'
        #groups = Group.objects.all()
        if request.method == 'POST':
            PostForm = forms.CreatePost(request.POST)
            if PostForm.is_valid():
                new_post = Post(text=PostForm.cleaned_data['text'], author=request.user, group=PostForm.cleaned_data['group'])
                new_post.save()
                return redirect('posts:index')

            PostForm = forms.CreatePost(request.POST)
            context = {
                'form': PostForm,
                'request': request,
                #'groups': groups,
            }
            return render(request, template, context)

        PostForm = forms.CreatePost()
        context = {
            'form': PostForm,
            'request': request,
            #'groups': groups,
        }
        return render(request, template, context)
    else:
        return redirect('users:login')


def post_edit(request, post_id):
    post_obj = Post.objects.get(pk=post_id)
    if request.user.is_authenticated and request.user == post_obj.author:
        template = 'posts/create_post.html'
        form = forms.CreatePost()
        context = {
            'is_edit': True,
            'form': form,
        }
        return (request, template, context)
    else:
        return redirect('posts:post_detail/post_id')
