"""Urls for base
"""
# Django Library
from django.urls import path

# Localfolder Library
from ..views import PyHomeTemplateView, PyUserUpdateView, PyUserDeleteView
from ..views.publication import PyPublicationCreateView

app_name = 'base'

urlpatterns = [
    path('', PyHomeTemplateView, name='home'),
]