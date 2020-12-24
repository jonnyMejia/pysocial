# Django Library
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import FormMixin, UpdateView, CreateView, DeleteView
from django.urls import reverse_lazy
from django.http import Http404

from ..forms import ProfileForm
from ..models import PyUser

class UserUpdateView(LoginRequiredMixin, UpdateView):
    """View edit Personal Information
    """
    model = PyUser
    template_name = 'base/personal/update.html'
    form_class = ProfileForm
    success_url = reverse_lazy('PyProfile:update') 
    
    def get_object(self):
        try:
            return self.request.user
        except self.model.DoesNotExist:
            raise Http404("No MyModel matches the given query.")
    
PyUserUpdateView = UserUpdateView.as_view()

class UserDeleteView(LoginRequiredMixin, DeleteView):
    model = PyUser
    template_name = "base/personal/delete.html"
    success_url = reverse_lazy("base:home")
    
    def get_object(self):
        try:
            return self.request.user
        except self.model.DoesNotExist:
            raise Http404("No MyModel matches the given query.")

PyUserDeleteView = UserDeleteView.as_view()
