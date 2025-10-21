from django import forms
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.forms import UserCreationForm

class UserSignInForm(forms.Form):

    email = forms.CharField(label=_('Email'), 
                             required=True, 
                             widget=forms.TextInput(attrs={'id': 'email',
                                                           'placeholder': _('Your Email')})) 
    
    password = forms.CharField(label='Password',
                               required=True,
                               widget=forms.PasswordInput(attrs={'placeholder': _('Parol'),
                                                                 'id': 'password'}))