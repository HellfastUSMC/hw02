from django.views.generic.base import TemplateView

# Create your views here.


class Author(TemplateView):
    template_name = 'about/author.html'


class Tech(TemplateView):
    template_name = 'about/tech.html'
