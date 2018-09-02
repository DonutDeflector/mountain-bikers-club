from django import forms
from django.contrib.auth.forms import UserCreationForm as DefaultUserCreationForm
from django.utils.translation import gettext_lazy as _

from .models import User


forbidden_username = [
    'superuser',
    'member'
]


class UserCreateForm(DefaultUserCreationForm):
    class Meta:
        model = User
        fields = DefaultUserCreationForm.Meta.fields + ('email',)

    def clean_username(self):
        username = self.cleaned_data['username']

        if username in forbidden_username or username.startswith('admin'):
            raise forms.ValidationError(_("This username is forbidden."))

        return username


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email')

    def clean_username(self):
        username = self.cleaned_data['username']

        if username in forbidden_username or username.lower().startswith('admin'):
            raise forms.ValidationError(_("This username is forbidden."))

        return username

    def save(self, commit=True):
        user = super().save(commit=False)
        if commit:
            user.save()
        return user
