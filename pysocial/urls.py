"""Rutas de PySocial
"""
# Django Library
from django.conf import settings
from django.contrib import admin
from django.urls import path
from django.conf.urls import include, url
from django.views.static import serve

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('apps.base.urls')),
    # url(r'^rest-auth/', include('rest_auth.urls')),
    path('media/<path:path>', serve, {'document_root': settings.MEDIA_ROOT, }),
    path('static/<path:path>', serve, {'document_root': settings.STATIC_ROOT, }),
]
