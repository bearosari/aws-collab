from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,get_user_model,login,logout
from .forms import UserForm, ProfileForm
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
# Create your views here.

@login_required
def home(request):
    context = {
        'title':'ColLab', 
    }
    return render(request, 'accounts/dashboard.html', context)

def classes(request):
    context = {
        'title':'Classes', 
    }
    return render(request, 'accounts/classes.html', context)

def class1(request):
    context = {
        'title':'Class1', 
    }
    return render(request, 'accounts/class1.html', context)

def class1vn(request):
    context = {
        'title':'Pointers', 
    }
    return render(request, 'accounts/class1vn.html', context)

def index(request):
    context = {
        'title' : 'index',
    }
    return render(request, 'accounts/main.html', context)

def signin(request):
    if request.method == 'POST':
        form = AuthenticationForm(data = request.POST)
        if form.is_valid():
            return redirect('home')
    else:
        form = AuthenticationForm()
    context = {
        'title': 'signin',
        'form': form,
    }
    return render(request, 'accounts/signin.html', context)

def signup(request):
    if request.method == "POST":
        user_form = UserForm(request.POST)
        profile_form = ProfileForm(request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()

            profile = profile_form.save(commit = False)
            profile.user = user
            profile.save()
            return redirect('signin')
    else:
        user_form = UserForm()
        profile_form = ProfileForm()
    context = {
        'title': 'signup',
        'form' : user_form,
        'profile_form' : profile_form,
    }
    return render(request, 'accounts/signup.html', context)

def aboutus(request):
    context = {
        'title':'aboutus'
    }
    return render(request, 'accounts/aboutus2.html', context)

def matlab(request):
    context = {
        'title':'Matlab', 
    }
    return render(request, 'accounts/matlab.html', context)

def prog_ide(request):
    context = {
        'title':'Programming', 
    }
    return render(request, 'accounts/prog_ide.html', context)