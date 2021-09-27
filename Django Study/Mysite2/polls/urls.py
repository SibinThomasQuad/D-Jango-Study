from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('insert/student/', views.insert, name='insert'),
]

