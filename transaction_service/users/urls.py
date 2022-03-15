from django.contrib.auth.views import (LoginView, LogoutView)
from django.urls import path

from . import views

app_name = 'users'

urlpatterns = [
    path('sign_up/', views.SignUp.as_view(), name='sign_up'),
    path('login/', LoginView.as_view(
        template_name='users/login.html'
    ), name='login'),
    path('logout/', LogoutView.as_view(
        template_name='users/logout.html'),
         name='logout'),
    path('profile/', views.Profile.as_view(), name='profile')
]
