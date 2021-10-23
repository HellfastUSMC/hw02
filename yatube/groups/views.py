from django.shortcuts import render, get_object_or_404

from .models import Group
from posts.models import Post


def group_posts(request, slug):
    template = 'groups/group_list.html'
    group = get_object_or_404(Group, slug=slug)
    title = group.title
    posts = Post.objects.filter(group=group).order_by('-pub_date')[:10]
    context = {
        'group_slug': slug,
        'group_ten_posts': posts,
        'group_title': title,
    }
    return render(request, template, context)
