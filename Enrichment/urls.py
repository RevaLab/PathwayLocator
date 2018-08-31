from django.urls import path

from . import views

urlpatterns = [
    path('gene-enrichment', views.index, name='index'),
]
