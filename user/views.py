from django.shortcuts import render, redirect
from django.urls import reverse
from main.models import Braider
from django.contrib import messages
from .forms import Registration

from django.contrib.auth import authenticate, login

# Create your views here.

def register(request):

    if request.method == 'POST':
        form = Registration(request.POST)
        if form.is_valid():

            cd = form.cleaned_data

            braider = Braider(
                first_name=cd['first_name'],
                last_name=cd['last_name'],
                user_name=cd['user_name'],
                user_type=cd['user_type'],
                insta_id=cd['insta_id'],
                email=cd['email'],
                password=cd['password'],
                phone_number=cd['phone_number'],
                country=cd['country'],
                city=cd['city'],
            )

            braider.save()

            messages.success(request, 'you account  have been created. wellcome to braidstarz!'.title())
            return redirect('login')

        else:
            print(form.cleaned_data)
            for field_name, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"\n{str(field_name).replace('_', ' ').title()}\n: {error}")

    else:
        form = Registration()

    context = {'form': form}
    return render(request, 'register.html', context)


def login(request):
    if request.method == 'POST':
        user_name = request.POST['user_name']
        password = request.POST['password']
        Braider = authenticate(request, user_name=user_name, password=password)
        if Braider is not None:
            login(request, user)
            return redirect('home')
        else:
            # handle invalid login
            pass
    else:
        return render(request, 'login.html')
    return render(request, 'login.html')


def fregister(request):
    return render(request, 'registerfirst.html')


def flogin(request):
    return render(request, 'loginfirst.html')

