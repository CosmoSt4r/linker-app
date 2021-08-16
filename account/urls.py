from django.urls import path
from . import views

app_name = 'account'
urlpatterns = [
    # path('', <base_view>, name="base")
    # path('login/', <login_view>, name='login'),
    path('signup/', views.signup, name='signup'),
    # path('home/', <home_view>, name='home'),
]