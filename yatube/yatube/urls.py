from django.contrib import admin
from django.urls import include
from django.urls import path


urlpatterns = [
    path('admin/', admin.site.urls),
    path('group/', include('groups.urls', namespace='groups')),
    path('', include('posts.urls', namespace='posts')),
]
