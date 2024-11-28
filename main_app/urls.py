# catcollector/urls.py

from django.contrib import admin
from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('cats/', views.cat_index, name='cat-index'),

]