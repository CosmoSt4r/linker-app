from django.urls import path
from . import views

app_name = 'account'
urlpatterns = [
    path('', views.base_view, name="base"),
    path('login/', views.login_view, name='login'),
    path('signup/', views.signup_view, name='signup'),
    # path('home/', <home_view>, name='home'),
]