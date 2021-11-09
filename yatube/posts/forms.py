from django import forms
from django.contrib.auth import get_user_model

from groups import models as gm


User = get_user_model()


class CreatePost(forms.Form):
    text = forms.CharField(label="Текст поста", help_text='Текст нового поста', widget=forms.Textarea, required=True)
    group = forms.ModelChoiceField(label="Группа", help_text='Группа, к которой будет относиться пост', queryset=gm.Group.objects.all(), required=False)
