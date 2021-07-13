from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse 
from django.contrib.auth.models import User 
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
# Create your views here.


def index(request):
    print(request.user.username)
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('login'))
    return render(request, 'account/profile.html')


def login_page(request):
    if request.method ==  'POST':
        username = request.POST['username']
        password = request.POST['password']
        print(username, password)
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'Successfully login')
            return HttpResponseRedirect(reverse('index'))
        else:
            messages.warning(request, 'Invalide login credential')
            return render(request, 'account/user_login.html')

    return render(request, 'account/user_login.html')

def logout_page(request):
    logout(request)
    messages.success(request, 'Successfully logout')
    return HttpResponseRedirect(reverse('index'))

        