from django import forms
from .models import Profile
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username','first_name', 'last_name', 'password1', 'password2')
    def save(self, commit = True):
        user = super(UserForm, self).save(commit=False)

        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']

        if commit:
            user.save()
        return user

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('account_type',)
    #def save(self, commit = True):
     #   user = super(ProfileForm, self).save(commit = False)
      #  user.account_type = self.cleaned_data['account_type']

       # if commit:
        #    user.save()
        #return user

class UserLoginForm(forms.ModelForm):
    username = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ('username', 'password',)