from django.urls import path, include
from . import views

app_name = "account"
urlpatterns = [
    path("", views.base_view, name="base"),
    path("login/", views.login_view, name="login"),
    path("logout/", views.logout_view, name="logout"),
    path("signup/", views.signup_view, name="signup"),
    path("home/", include("home.urls")),
]
