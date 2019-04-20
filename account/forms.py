from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from account.models import profile

class userregister(UserCreationForm):
    email = forms.EmailField()
    
    class Meta:
        model = User
        fields=['username','email','password1','password2']

class updateuser(forms.ModelForm):
    email = forms.EmailField()  
    class Meta:
        model = User
        fields = ['username', 'email']
        
class updateprofile(forms.ModelForm):
    class Meta:
        model = profile
        fields = ['image']