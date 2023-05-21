from django.urls import path
from . import views

urlpatterns = [
    path("", views.my_home, name="home"),
    path("sobre/", views.my_about, name="about"),
]
