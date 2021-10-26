from django.shortcuts import render
from django.shortcuts import get_object_or_404

from .models import Group


def group_posts(request, slug):
    template = 'groups/group_list.html'
    group = get_object_or_404(Group, slug=slug)
    title = group.title
    page_title = f'Посты группы {title}.'
    posts = group.posts.all().order_by('-pub_date')[:10]
    context = {
        'group_slug': slug,
        'group_ten_posts': posts,
        'group_title': title,
        'page_title': page_title,
    }
    return render(request, template, context)
