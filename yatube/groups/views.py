from django.core.paginator import Paginator
from django.shortcuts import render
from django.shortcuts import get_object_or_404

from .models import Group


def group_posts(request, slug):
    template = 'groups/group_list.html'
    group = get_object_or_404(Group, slug=slug)
    title = group.title
    page_title = f'Посты группы {title}.'
    posts = group.posts.all().order_by('-pub_date')
    paginator = Paginator(posts, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'group_slug': slug,
        'posts': page_obj,
        'group_title': title,
        'page_title': page_title,
    }
    return render(request, template, context)
