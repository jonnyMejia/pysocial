# Django Library
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import FormMixin, UpdateView, CreateView
from django.urls import reverse_lazy
from django.http import Http404

from ..forms import ProfileForm
from ..models import PyUser

class SettingsView(LoginRequiredMixin, UpdateView):
    """View edit Personal Information
    """
    model = PyUser
    template_name = 'base/settings.html'
    form_class = ProfileForm

    def get_object(self):
        try:
            return self.request.user
        except self.model.DoesNotExist:
            raise Http404("No MyModel matches the given query.")

settingsView = SettingsView.as_view()
