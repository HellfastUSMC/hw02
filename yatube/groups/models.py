from django.db import models
from django.db import models
from django.contrib.auth import get_user_model
from django.db.models.fields import CharField, SlugField, TextField

# Create your models here.
User = get_user_model()

class Group(models.Model):
    title = CharField(max_length=100)
    slug = SlugField()
    description = TextField()

    def __str__(self):
        return self.title
