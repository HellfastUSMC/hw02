from django.core.paginator import Paginator
from django.shortcuts import render
from django.shortcuts import get_object_or_404

from .models import Post
from .models import Group


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
