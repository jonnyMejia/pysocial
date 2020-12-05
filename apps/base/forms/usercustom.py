# Django Library
from django import forms
from django.utils.translation import ugettext_lazy as _

from ..models import PyUser

class ProfileForm(forms.ModelForm):
    """Clase para actualizar el perfil del usuario en el sistema
    """
    class Meta:
        model = PyUser
        fields = (
            'avatar',
            'first_name',
            'last_name',
            'gender',
            'day_of_birth',
        )
        labels = {
            'avatar': _('Avatar'),
            'first_name': _('Name'),
            'last_name': _('Last Name'),
            'gender': _('Gender'),
            'day_of_birth': _('Day of Birth'),
        }
        widgets = {
            'avatar': forms.FileInput(attrs={'class': 'form-control'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'gender': forms.Select(attrs={'class': 'form-control'}),
            'day_of_birth': forms.DateInput( format=('%m/%d/%Y'), attrs={'placeholder':'like 05/12/1999'}),
        }