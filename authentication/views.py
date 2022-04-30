from unicodedata import name
from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import SignUpForm
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
# Create your views here.

#sign up view function


def sign_up(request):
    if request.method == "POST":
        fm = SignUpForm(request.POST)
        if fm.is_valid():
            messages.success(request,'Account Created Successfully!')
            fm.save()
    else:
     fm = SignUpForm()
    return render(request, 'signup.html',{'form':fm})



#login view function
def user_login(request):
    if not request.user.is_authenticated:
        if request.method =="POST":
            fm2 = AuthenticationForm(request =request,data = request.POST)
            if fm2.is_valid():
                uname = fm2.cleaned_data['username']
                upass = fm2.cleaned_data['password']
                user = authenticate(username = uname, password = upass)
                if user is not None:
                    login(request,user)
                    messages.success(request,"logged in succesfully !!")
                    return HttpResponseRedirect('/profile/')
        else:
            fm2 = AuthenticationForm()
        return render(request, 'userlogin.html', {'form':fm2})
    else:
        return HttpResponseRedirect('/profile/')




def profile(request):
    if request.user.is_authenticated:
        return render(request, 'profile.html', {'name': request.user})
    else:
        return HttpResponseRedirect('/login')




def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/login')
