from django.urls import path
from . import views

urlpatterns = [
    path('', views.tweet_display, name='home')
]
