from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import Registerform




def register(request):
    if request.method=='POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            username=form.cleaned_data.get('username')
            messages.success(request,f"Welcome {username} ,your account is created")
            return redirect('login')
    else:
        form = Registerform()
        return render(request,'users/register.html',{'form':form})

@login_required
def profilepage(request):
    return render(request,'users/profile.html')


def login(request):
    if request.method=="POST":
        form.save()
        return redirect('index')
   