"""Urls for base
"""
# Django Library
from django.urls import path

# Localfolder Library
from ..views import PyHomeTemplateView, PyUserUpdateView, PyUserDeleteView
from ..views.publication import PyPublicationCreateView

app_name = 'PyProfile'

urlpatterns = [
    path('update/', PyUserUpdateView, name='update'),
    path('delete/', PyUserDeleteView, name='delete'),
]