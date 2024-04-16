from django import forms 
from .models import *
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm,UsernameField
from django.utils.translation import gettext,gettext_lazy as _

class RegistrationForm(UserCreationForm):
    password1 = forms.CharField(label='Password',widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password2 = forms.CharField(label='Confirm Password',widget=forms.PasswordInput(attrs={'class':'form-control'}))
    email = forms.CharField(required=True,widget=forms.EmailInput(attrs={'class':'form-control'}))
    class Meta: 
        model=User
        fields = ['username','first_name','last_name','email','password1','password2']


class LogInForm(AuthenticationForm):
    username = UsernameField(widget=forms.TextInput(attrs={'autofocus':True,'class':'form-control'}))
    password = forms.CharField(label=_('Password'),strip=False,widget=forms.PasswordInput(attrs={'autocomplete':'current-password','class':'form-control'}))


class ProfileForm(forms.Form):
    username = UsernameField(widget=forms.TextInput(attrs={'autofocus':True,'class':'form-control',}))
    bio = forms.CharField(label='Bio',widget=forms.Textarea(attrs={'autofocus':True,'class':'form-control'}))
    profile_picture = forms.ImageField()
    

class EditProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'

        