from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import AppuiR

# Create your views here.

def liste_appui(request):
    appuimethodo = AppuiR.objects.all()
    data = {'appui': appui}
    return render(request, 'appui/appui.html', data)

def appui(request,name):
    try:
        appui = AppuiR.objects.get(slug=name)
        data = {'appui':appui}
    except:
        data = {'appui','Ce soutien méthodologique n\'existe pas'}
    return render(request, 'appui/detail_appui.html', data)