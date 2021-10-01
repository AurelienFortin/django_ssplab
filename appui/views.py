from django.shortcuts import render
from django.views.generic import ListView, DetailView


# Create your views here.

def appui(request):
    return render(request, 'appui/appui.html')