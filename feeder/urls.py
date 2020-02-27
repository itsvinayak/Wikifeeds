from django.urls import path
from . import views

urlpatterns = [
    path('', views.index,name="home"),
    path('getfeeds/',views.getFeeds,name="feeds"),
    path('about/',views.about,name="about"),
]
