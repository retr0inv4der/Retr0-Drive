from django.urls import path
from .views import * 

urlpatterns = [
     path("register/" , RegisterView.as_view()),
     path("login/" , LoginView.as_view()),
     path("refresh/" , RefreshTokenView.as_view()),
     path("profile/" , GetUserInfoView.as_view()),
]