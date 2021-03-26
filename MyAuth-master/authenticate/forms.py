from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from django import forms

class editProfileForm(UserChangeForm):
	password = forms.CharField(label="", widget=forms.TextInput(attrs={'type':'hidden'}))
	class Meta:
		model = User
		fields = ('username','email','password')

class signUpForm(UserCreationForm):
	email = forms.EmailField(label="", widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Email Address'}))
	First_name = forms.CharField(label="", max_length=25, widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter First Name'})) 
	Last_name = forms.CharField(label="", max_length=25, widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Last Name'}))

	class Meta:
		model = User
		fields = ('username','First_name','Last_name','email','password1','password2',)

	