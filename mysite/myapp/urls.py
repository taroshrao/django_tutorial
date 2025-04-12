from django.urls import path

from . import views

urlpatterns = [
    path('something_interesting/', views.index, name='index'),
]