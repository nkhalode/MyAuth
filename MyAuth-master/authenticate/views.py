from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.contrib import messages
from .forms import signUpForm, editProfileForm

def home(request):
	return render(request,'authenticate/home.html',{})

def login_user(request):
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(request, username=username, password=password)
		if user is not None:
			login(request, user)
			messages.success(request,('You Have Logged in'))
			return redirect('home')
		else:
			messages.success(request,('Login Error '))
			return redirect('login')
	else:
		return render(request,'authenticate/login.html',{})

def logout_user(request):
	logout(request)
	messages.success(request,('You have been logout'))
	return redirect('home')

def register_user(request):
	if request.method=='POST':
		form = signUpForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data['username']
			password = form.cleaned_data['password1']
			user = authenticate(username=username, password=password)
			login(request, user)
			messages.success(request,('Registered Successfully'))
			return redirect('home')
	else:
		form = signUpForm()
	context = {'form':form}
	return render(request,'authenticate/register.html',context)

def edit_profile(request):
	if request.method=='POST':
		form = editProfileForm(request.POST, instance=request.user)
		if form.is_valid():
			form.save()
			messages.success(request,('Update Successfully'))
			return redirect('home')
	else:
		form = editProfileForm(instance=request.user)
	context = {'form':form}
	return render(request,'authenticate/edit_profile.html',context)

def change_password(request):
	if request.method=='POST':
		form = PasswordChangeForm(data=request.POST, user=request.user)
		if form.is_valid():
			form.save()
			update_session_auth_hash(request, form.user)
			messages.success(request,('Password Update Successfully'))
			return redirect('home')
	else:
		form = PasswordChangeForm(user=request.user)
	context = {'form':form}
	return render(request,'authenticate/change_password.html',context)
