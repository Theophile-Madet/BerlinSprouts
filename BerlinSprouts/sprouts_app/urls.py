from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add_meal', views.add_meal, name='add_meal'),
]
