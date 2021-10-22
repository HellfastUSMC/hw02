from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def groups(request):
    return HttpResponse('Groups page')

def group_detail(request):
    return HttpResponse('Group detail page')