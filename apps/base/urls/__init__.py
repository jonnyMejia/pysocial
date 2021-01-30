"""Urls for base
"""
# Django Library
from django.urls import path, include
from ..views.home import pysocial

urlpatterns = [
    # ============================ New URLs ============================ #
    path("", pysocial, name="pysocial"),
    path('base/', include('apps.base.urls.base')),
    path('profile/', include('apps.base.urls.profile')),
    path('publication/', include('apps.base.urls.publication')),
    path('user/', include('apps.base.urls.usercustom')),
]
