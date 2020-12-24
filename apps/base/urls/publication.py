"""Urls for base
"""
# Django Library
from django.urls import path

# Localfolder Library
from ..views import PyHomeTemplateView, PyUserUpdateView, PyUserDeleteView
from ..views.publication import PyPublicationCreateView, PyPublicationListView, PyPublicationUpdateView, PyPublicationDeleteView

app_name = 'PyPublication'

urlpatterns = [
    path('', PyPublicationListView, name='list'),
    path('add/', PyPublicationCreateView, name='add'),
    path('<int:pk>/update/', PyPublicationUpdateView, name='update'),
    path('<int:pk>/delete/', PyPublicationDeleteView, name='delete'),
]