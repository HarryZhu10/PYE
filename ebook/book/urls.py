from django.urls import path

from . import views

app_name = 'book'

urlpatterns = [
    path('add/', views.add, name='add'),
]