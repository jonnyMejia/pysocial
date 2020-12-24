# Django Library
from django import forms
from django.utils.translation import ugettext_lazy as _

from ..models import PyPublication

class PublicationForm(forms.ModelForm):
    """Clase para actualizar un publicacion
    """
    class Meta:
        model = PyPublication
        fields = (
            'content',
        )
        labels = {
            'content': _('Content'),
        }
        widgets = {
            'content': forms.Textarea(attrs={'type':"text", "placeholder":''
            , "style":"resize: none;"}),
            
        }
