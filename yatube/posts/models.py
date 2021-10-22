from django.db import models
from django.contrib.auth import get_user_model
from django.db.models.fields.related import ForeignKey

from groups.models import Group
# Create your models here.
User = get_user_model()


class Post(models.Model):
    text = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='posts'
    )
    group = ForeignKey(
        Group,
        on_delete=models.CASCADE,
        related_name='posts',
        blank=True, null=True
    )
