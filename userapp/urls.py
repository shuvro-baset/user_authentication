from django.urls import path
from . import views

app_name = 'userapp'
urlpatterns = [
    path('', views.home, name='home'),
    path('login', views.login, name='login'),
    path('signup', views.signup, name='signup'),
]