from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.index, name = 'index'),
    path('index', views.index, name = 'index'),
    path('evenements', views.evenements, name = 'evenements'),
    path('team', views.team, name = 'team'),
    path('pres', views.pres, name = 'pres'),
]
