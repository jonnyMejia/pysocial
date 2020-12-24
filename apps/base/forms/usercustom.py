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
            'avatar': forms.FileInput(attrs={'class': 'pi-input pi-input-lg'}),
            'first_name': forms.TextInput(attrs={'class': 'pi-input pi-input-lg'}),
            'last_name': forms.TextInput(attrs={'class': 'pi-input pi-input-lg'}),
            'gender': forms.Select(attrs={'class': 'pi-input pi-input-md'}),
            'day_of_birth': forms.DateInput(format=('%m/%d/%Y'), attrs={'class': 'pi-input pi-input-lg'}),
        }