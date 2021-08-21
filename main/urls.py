from django.urls import path
from . import views

app_name = "main-page"
urlpatterns = [
    path("", views.main_view, name="main"),
    path("<str:username>", views.show_user, name="show-user"),
]
