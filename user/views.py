from django.shortcuts import render,redirect
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from .forms import UserRegisterForm

# Create your views here.

def login(request):
	if request.user.is_authenticated:
		return redirect('main')
	if request.method == "POST" :
		username = request.POST["username"]
		password = request.POST["password"]

		user = authenticate(username = username,password = password)

		if user is not None:
			auth_login(request,user)
			return redirect('main')
		else:
			err_msg = "Invalid username or password"
			return render(request,'user/login.html',{'err_msg':err_msg})
	return render(request,'user/login.html')


def register(request):
	if request.user.is_authenticated:
		return redirect('main')
	if request.method =="POST":
		form = UserRegisterForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('main')
		else:
			error_message = "Error : User/Email Taken or Passwords not matched"
			return render(request,'user/register.html',{'error_message':error_message})
	form = UserRegisterForm()
	return render(request,'user/register.html',{'form':form})

def logout(request):
	auth_logout(request)
	return redirect('main')