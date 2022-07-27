from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User, auth
from django.contrib import messages
from .models import Profile

from core.models import Profile
# from urllib3 import HTTPResponse


def index(request):
    return render(request, 'index.html')

def signup(request):
    
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']
            
        if password == password2:
            # check for existing fields
            if User.objects.filter(email=email).exists(): 
                messages.info(request, 'Email already exists.')
                return redirect('signup')
            elif User.objects.filter(username=username).exists():
                messages.info(request, 'Username taken.')
                return redirect('signup')
            else:
                user = User.objects.create_user(username = username, email = email, password = password)
                user.save()
                
                #log user in and redirect to settings page
                
                #create profile object for new user
                user_model = User.objects.get(username=username)
                new_profile = Profile.objects.create(user=user_model, id_user=user_model.id)
                new_profile.save()
                return redirect('signup')
        else:
            messages.info(request, 'Password does not match.')
            return redirect('signup')
                    
    else:
        return render(request, 'signup.html')
    
def signin(request):
    return render(request, 'signin.html')