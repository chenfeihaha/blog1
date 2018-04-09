from django.urls import path,include
from . import views

urlpatterns = [
    #path(r'', views.home),
    path(r'home', views.home),
]
