from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponse
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
# Create your views here.

def IndexPage(request):
    return render(request,'index.html')

@login_required(login_url='login')
def HomePage(request):
    return render(request,'home.html')

def SignupPage(request):
    if request.method=='POST':
        uname=request.POST.get('username')
        email=request.POST.get('email')
        pass1=request.POST.get('password1')
        pass2=request.POST.get('password2')

        if pass1!=pass2:
            messages.warning(request,"Password and Confirm Password is not Same")
            return redirect('signup')
        else:
            my_user=User.objects.create_user(uname,email,pass1)
            my_user.save()
            return redirect('login')

    return render(request,'signup.html')

def LoginPage(request):
    if request.method=='POST':
        username=request.POST.get('username')
        pass1=request.POST.get('pass')
        user=authenticate(request,username=username,password=pass1)
        if user is not None:
            login(request,user)
            return redirect('rules')
        else:
            messages.warning(request,"Username or Password is Incorrect")
            
    return render(request,'login.html')
def Logout(request):
    logout(request)
    return redirect('login')
def success(request):
    logout(request)
    return render(request,'success.html')
def lose(request):
    logout(request)
    return render(request,'lose.html')
def rules(request):
    return render(request,'rules.html')
