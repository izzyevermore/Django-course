from django.urls import path

from . import views

urlpatterns = [
    path('meetups', views.starting_page) # our-domain.com/meetups
]