# Django Library
from django.contrib.auth.decorators import login_required
from django.shortcuts import render

# Localfolder Library

def pysocial(request):
    """View Home
    """

    return render(request, "pysocial.html")


@login_required()
def social_home(request):
    """View Home
    """

    return render(request, "base_social.html")

