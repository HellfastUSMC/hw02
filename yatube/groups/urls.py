from django.urls import path
from . import views

urlpatterns = [
    path('groups/', views.groups),
    path('groups/<int:group_id>', views.group_detail),
]