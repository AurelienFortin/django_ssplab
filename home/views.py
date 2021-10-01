from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, 'home/index.html')

def evenements_view(request):
    return render(request, 'home/evenements.html')

def team_view(request):
    return render(request, 'home/team.html')

def pres_view(request):
    return render(request, 'home/presentation_generale.html')