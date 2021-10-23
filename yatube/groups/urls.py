from . import views
from django.urls import path

app_name = 'groups'
urlpatterns = [
    path('<slug:slug>/', views.group_posts, name='group_list'),
]
