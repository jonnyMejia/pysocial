"""Urls for base
"""
# Django Library
from django.urls import path, include
from ..views.home import pysocial
urlpatterns = [
    # ============================ New URLs ============================ #
    path("", pysocial, name="erp_home"),
    path('', include('apps.base.urls.usercustom')),
    path('base/', include('apps.base.urls.base')),
   
]
