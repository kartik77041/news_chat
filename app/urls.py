from django.contrib import admin
from django.urls import path,include
from app import views
urlpatterns = [
    path('', views.home),
    path('news/<int:i>', views.news),
]