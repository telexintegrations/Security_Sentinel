from django.shortcuts import render
from django.urls import path
from . import views


urlpatterns = [
    path('compliances/integration.json/', views.CompliancesIntegration.as_view(), name='compliancesintegration'),
]
