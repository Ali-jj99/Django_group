from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("join", views.join, name="join"),
    path("login", views.login_view, name="login_view"),
]

