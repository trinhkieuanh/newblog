from django import forms
import re
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist

class RegistrationForm(forms.Form):
    username = forms.CharField(label='Account', max_length=30)
    email = forms.EmailField(label='Email')
    password = forms.CharField(label='Password', widget=forms.PasswordInput())
    repass = forms.CharField(label='Confirm Password', widget=forms.PasswordInput())

    def clean_repass(self):
        if 'password' in self.cleaned_data:
            password  = self.cleaned_data['password']
            repass = self.cleaned_data['repass']
            if password == repass and password:
                return repass
        raise forms.ValidationError('Invalis password')

# Lỗi check username
    '''def clean_username(self):
        username = self.cleaned_data['username']
        if not re.search(r'^\W+$', username):
            raise forms.ValidationError('invalid username')
        try:
            User.objects.get(username=username)
        except ObjectDoesNotExist:
            return username
        raise forms.ValidationError('existed username')'''
    
    def save(self):
        User.objects.create_user(username=self.cleaned_data['username'], email = self.cleaned_data['email'], password  = self.cleaned_data['password'])