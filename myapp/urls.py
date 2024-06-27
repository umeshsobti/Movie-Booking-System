from django import urls
from django.urls import path
from . import views
from .views import main
urlpatterns = [
    path('', views.main, name="main"),
    path('movie_detail/', views.save_movie, name="save_movie")
    
]
