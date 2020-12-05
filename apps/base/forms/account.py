from django.conf import settings
from django.utils.translation import ugettext_lazy as _
from django import forms
from allauth.account.forms import LoginForm, SignupForm

class MyLoginForm(LoginForm):

    def __init__(self, *args, **kwargs):
           super(MyLoginForm, self).__init__(*args, **kwargs)
           self.fields['login'].widget = forms.TextInput(attrs={'type': 'email', 'class': 'input100', "placeholder": _("E-mail address")})
           self.fields['password'].widget = forms.PasswordInput(attrs={'class': 'input100', "placeholder": _("Password")})

class MySignupForm(SignupForm):

    def __init__(self, *args, **kwargs):
           super(MySignupForm, self).__init__(*args, **kwargs)
           self.fields['email'].widget = forms.TextInput(attrs={'class': 'input100',  "placeholder": _("E-mail address")})
           self.fields['password1'].widget = forms.PasswordInput(attrs={'class': 'input100', "placeholder": _("Password")})
           self.fields['password2'].widget = forms.PasswordInput(attrs={'class': 'input100', "placeholder": _("Password (again)")})