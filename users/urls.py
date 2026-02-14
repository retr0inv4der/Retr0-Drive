from django.urls import path
from .views import * 

urlpatterns = [
    path("register/" , UserRegisterAPI.as_view()),
    path("login/" , UserLoginAPI.as_view()),
    path("profile/" , GetUserProfileInfoAPI.as_view())
]