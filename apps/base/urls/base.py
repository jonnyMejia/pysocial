"""Urls for base
"""
# Django Library
from django.urls import path

# Localfolder Library
from ..views import social_home, PySettingsUpdateView, PyUserDeleteView

app_name = 'base'

urlpatterns = [
    path('', social_home, name='home'),
    path('settings/', PySettingsUpdateView, name='settings'),
    path('delete-account/', PyUserDeleteView, name='delete_account'),
]