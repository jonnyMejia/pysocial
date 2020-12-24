# Django Library
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import FormMixin, UpdateView, CreateView, DeleteView
from django.views.generic import TemplateView
from django.urls import reverse_lazy
from django.http import Http404
from django.contrib.auth.decorators import login_required
from django.shortcuts import render

# Localfolder Library
from ..models import PyPublication

def pysocial(request):
    """View Home
    """
    return render(request, "pysocial.html")

class HomeTemplateView(LoginRequiredMixin, TemplateView):
    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super(HomeTemplateView, self).get_context_data(**kwargs)
        context["publications"] = PyPublication.objects.all()        
        return context
    

PyHomeTemplateView = HomeTemplateView.as_view()



