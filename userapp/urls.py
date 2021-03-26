from django.urls import path
from . import views

app_name = 'userapp'
urlpatterns = [
    path('', views.home, name='home'),
    path('login', views.loginUser, name='login'),
    path('logout', views.logoutUser, name='logout'),
    path('signup', views.signup, name='signup'),
    path('change-password', views.changePass, name='change_pass'),
    path('session-time', views.sessionTime, name='session_time'),
]