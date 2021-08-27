from django.urls import path
from . import views

app_name = "home"
urlpatterns = [
    path("", views.main_view, name="main"),
    path("add/", views.add_code_view, name="add-code"),
    path("edit/", views.edit_view, name="edit-main"),
    path("edit/<int:id>/", views.edit_code_view, name="edit-code"),
    path("delete/<int:id>/", views.delete_code_view, name="delete-code"),
]
