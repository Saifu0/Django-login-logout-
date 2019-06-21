from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm

def index(request):
    return render(request,'app/index.html',{})

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request,f"Your account has been created. You can Now login!")
            return redirect('index')

    else:
        form = UserRegisterForm()

    return render(request,'registration/register.html',{'form':form})

