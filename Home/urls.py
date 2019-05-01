from django.urls import path

from . import views

urlpatterns = [
    path('', views.aboutUs, name='About Us'),
]
