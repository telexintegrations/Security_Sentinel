from django.shortcuts import render
from django.urls import path
from . import views


urlpatterns = [
    path('core/integration.json/', views.CoreIntegration.as_view(), name='coreintegration'),
]

