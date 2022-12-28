from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
#from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import User

# Create your views here.

def index(request):
    return render(request, 'index.html')
    
def home(request):
    if request.method == "POST":
        if request.POST['status'] == "signup":
            email = request.POST['email']
            password = request.POST['password']
            repeat_password = request.POST['repeat_password']
            if password == repeat_password:
                if User.objects.filter(email=email).exists():
                    messages.info(request, 'Email already used')
                    return redirect('/authapp/')
                else:
                    user = User.objects.create(email=email, password=password)
                    user.save()
                    return render(request, 'home.html', {"email":email})
            elif password != repeat_password:
                messages.info(request, 'Your passwords do not match')
                return redirect('/authapp/')
        elif request.POST['status'] == "login":
            email = request.POST['email']
            password = request.POST['password']
            user = auth.authenticate(request, email=email, password=password)
            if user is not None:
                auth.login(request, user)
                return render(request, 'home.html', {"email":email})
            else:
                messages.info(request, 'Invalid credentials')
                return redirect('/authapp/')
    elif request.method != "POST":
        return redirect('/authapp/')
    
def logout(request):
    auth.logout(request)
    return redirect('/authapp/')