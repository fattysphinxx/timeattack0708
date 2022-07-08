from django.contrib import admin
from django.urls import path, include
from .views import SignUpView, SignInView
from rest_framework_simplejwt.views import TokenObtainPairView
urlpatterns = [
    path('sign-up', SignUpView.as_view()),
    path('sign-in', SignInView.as_view()),
    path('login/', TokenObtainPairView.as_view()),
]
