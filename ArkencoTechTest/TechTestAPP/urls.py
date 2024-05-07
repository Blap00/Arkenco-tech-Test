# This file is used to map the URL to the view function
from django.urls import path
from . import views
#from django.contrib.auth.views import LogoutView
#from django.contrib.auth import views as auth_views


app_name = "TechTestAPP"
urlpatterns = [
    path('', views.home_view, name="Home"),
    path('logout', views.home_view, name='logout'),
    path('login', views.home_view, name='login'),
]