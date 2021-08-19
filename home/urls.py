from django.urls import path
from . import views

app_name = "home"
urlpatterns = [
    path("", views.main_view, name="main"),
    path("add/", views.add_link_view, name="add-link"),
    path('edit/', views.edit_view, name='edit-main'),
    path("edit/<int:id>/", views.edit_link_view, name="edit-link"),
    path('delete/<int:id>/', views.delete_link_view, name='delete-link'),
]
