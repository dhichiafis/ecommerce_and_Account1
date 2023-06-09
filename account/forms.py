from django.contrib.auth.models import User
from .models import Profile
from django import forms
class UserRegistrationForm(forms.ModelForm):
    password=forms.CharField(label='password',widget=forms.PasswordInput)
    password2=forms.CharField(label='repeat-password',widget=forms.PasswordInput)

    class Meta:
        model=User
        fields=('username','first_name','email')

    def clean_password2(self):
        cd=self.cleaned_data
        if cd['password']!=cd['password2']:
            raise forms.ValidationError(
            'Password data match'
            )
        return cd['password2']


class UserEditForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['first_name','email']

class ProfileEditForm(forms.ModelForm):
    class Meta:
        model=Profile
        fields=['date_of_birth','photo']