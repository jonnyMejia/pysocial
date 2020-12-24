# Django Library
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import FormMixin, UpdateView, CreateView, DeleteView
from django.views.generic import TemplateView, ListView
from django.urls import reverse_lazy
from django.http import Http404
from django.contrib.auth.decorators import login_required
from django.shortcuts import render

# Localfolder Library
from ..models import PyPublication
from ..forms import PublicationForm

class PublicationListView(LoginRequiredMixin, ListView):
    model = PyPublication
    template_name = "base/publication/list.html"

PyPublicationListView =  PublicationListView.as_view()

class PublicationCreateView(LoginRequiredMixin, CreateView):
    model = PyPublication
    template_name = "base/publication/add.html"
    form_class = PublicationForm
    success_url = reverse_lazy('base:home')

    def form_valid(self, form):
        publication = form.save()
        publication.user = self.request.user
        publication.save()
        return super(PublicationCreateView, self).form_valid(form)

PyPublicationCreateView =  PublicationCreateView.as_view()

class PublicationUpdateView(LoginRequiredMixin, UpdateView):
    model = PyPublication
    template_name = "base/publication/update.html"
    form_class = PublicationForm
    success_url = reverse_lazy('PyPublication:list')

PyPublicationUpdateView = PublicationUpdateView.as_view()

class PublicationDeleteView(LoginRequiredMixin, DeleteView):
    model = PyPublication
    template_name = "base/publication/delete.html"
    success_url = reverse_lazy('PyPublication:list')

PyPublicationDeleteView = PublicationDeleteView.as_view()