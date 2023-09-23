from django.shortcuts import render,redirect

# Create your views here.

# from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import RegisterForm
from django.contrib.auth.decorators import login_required

def register(request):
    if request.method =='POST':
        form=RegisterForm(request.POST)
        
        if form.is_valid():
            form.save()
            username=form.cleaned_data.get('username')
            print(username)
            messages.success(request,f'welcome {username},your account is created')
            return redirect('login')
    else:
        form=RegisterForm()
        print('hi')
    return render(request,'users/register.html',{'form':form})

@login_required
def profile(request):
    return render(request,'users/profile.html')