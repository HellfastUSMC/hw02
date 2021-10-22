from django.urls import path
from . import views

app_name = 'posts'

urlpatterns = [
    path('', views.index, name='index'),
    path('group_list/', views.post_detail, name='group_temp'),
    path('group_list/<slug>', views.group_posts, name='group_list'),
]
