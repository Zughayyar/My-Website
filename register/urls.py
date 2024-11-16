from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('success', views.success),
    path('register', views.register),
    path('signout', views.signout),
    path('login', views.login),
]