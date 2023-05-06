from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout #, register
from django.contrib import messages
from django.http import HttpResponse

# Create your views here.
def home(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        #authenticate
        user = authenticate(request, username=username, password= password)
        if user is not None:
            login(request, user)
            messages.success(request, 'You have been logged in')
            return redirect('home')
        else:
            messages.success(request,'There was an error in logging in please try again....')
            return redirect('home')
    else:
        return render(request, 'home.html', {})


def logout_user(request):
    logout(request)
    messages.success(request, 'You have been logged out')
    return redirect('home')

def register_user(request):

    return render(request, 'register.html', {})
    