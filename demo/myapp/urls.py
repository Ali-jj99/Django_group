from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("join", views.join, name="join"),
    path("login", views.login_view, name="login_view"),
    path("vote", views.vote_view, name="vote_view"),
    path("progress", views.progress_view, name="progress_view"),
    path("signup", views.signup_view, name="signup_view"),
    path("summary", views.summary_view, name="summary_view"),
]

