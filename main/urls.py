from django.urls import path
from . import views

app_name = "main"
urlpatterns = [
    path("", views.main_view, name="search"),
    path("<str:username>/", views.show_user, name="user"),
]
