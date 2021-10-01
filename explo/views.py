from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Explo

# Create your views here.

def liste_explo(request):
    explo = Explo.objects.all()
    data = {'explorations': explo}
    return render(request, 'explo/explo.html', data)

def exploration(request,name):
    try:
        exploration = Explo.objects.get(slug=name)
        data = {'exploration':exploration}
    except:
        data = {'exploration','Cette exploration n\'existe pas'}
    return render(request, 'explo/detail_explo.html', data)


