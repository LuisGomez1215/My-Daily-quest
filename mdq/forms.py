from django import forms
from django.urls import reverse_lazy
from django.utils.translation import gettext as _
from django.db import transaction
from django.contrib.auth import forms as user_forms, password_validation
from django.utils.safestring import mark_safe
from turnstile.fields import TurnstileField

from mdq.models import MdqUser, Pet, PetBackground, Profile


class PetSelectForm(forms.ModelForm):
    class Meta:
        model = Pet
        fields = ['name']
        widgets = {
        'name': forms.TextInput(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        self.species_id = kwargs.pop('species_id', None)
        super().__init__(*args, **kwargs)


class MdqUserRegistrationForm(forms.Form):
    username = user_forms.UsernameField(widget=forms.TextInput(attrs={'autofocus': True}))
    email = forms.EmailField(
        label=_('Email'),
        max_length=254,
        widget=forms.EmailInput(attrs={'autocomplete': 'email'}),
    )
    password1 = forms.CharField(
        label=_('Password'),
        widget=forms.PasswordInput(
            attrs={'autocomplete': 'new-password', 'autofocus': True}
        ),
        strip=False,
    )
    password2 = forms.CharField(
        label=_('Password (again)'),
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password'}),
        strip=False,
        help_text=_('Enter the same password as before, for verification.'),
    )
    turnstile = TurnstileField()

    error_messages = {
        'password_mismatch': _('The two password fields didn’t match.'),
        'user_exists': _('That username is already taken.'),
        'email_exists': _('That email is in use.'),
    }

    def clean_username(self):
        username = self.cleaned_data.get('username')
        try:
            MdqUser.objects.get(username=username)
            raise forms.ValidationError(
                self.error_messages['user_exists'],
                code='user_exists',
            )
        except MdqUser.DoesNotExist:
            return username

    def clean_email(self):
        email = self.cleaned_data.get('email')
        try:
            MdqUser.objects.get(email=email)
            raise forms.ValidationError(
                self.error_messages['email_exists'],
                code='email_exists',
            )
        except MdqUser.DoesNotExist:
            return email

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError(
                self.error_messages['password_mismatch'],
                code='password_mismatch',
            )
        password_validation.validate_password(password2)
        return password2

    def save(self):
        data = self.cleaned_data
        new_user = MdqUser.objects.create_user(username=data['username'], email=data['email'], password=data['password1'])
        Profile.objects.create(user=new_user)
        return new_user