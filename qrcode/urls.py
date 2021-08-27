from django.urls import path
from . import views

app_name = "qrcode"
urlpatterns = [
    path("add/", views.add_code_view, name="add"),
    path("edit/<int:id>/", views.edit_code_view, name="edit"),
    path("delete/<int:id>/", views.delete_code_view, name="delete"),
    path("show/<int:id>/", views.show_code_view, name="show"),
]
