from django.shortcuts import render
from django.urls import path
from . import views


urlpatterns = [
    path('security/integration.json/', views.SecurityIntegration.as_view(), name='securityintegration'),
]
