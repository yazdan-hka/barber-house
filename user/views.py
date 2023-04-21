from django.shortcuts import render, redirect
from django.urls import reverse
from main.models import Braider
from django.contrib import messages
from .forms import BraiderRegistration, BraiderLogin
from django.contrib.auth import authenticate, login
from django.contrib.auth.hashers import check_password, make_password


# Create your views here.

def register_page(request):

    if request.method == 'POST':
        form = BraiderRegistration(request.POST)
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
        form = BraiderRegistration()

    context = {'form': form}
    return render(request, 'register.html', context)


def login_page(request):
    if request.method == 'POST':

        form = BraiderLogin(request.POST)
        if form.is_valid():

            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            remember_me = form.cleaned_data.get('remember_me')

            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                if remember_me:
                    request.session.set_expiry(1209600)  # 2 weeks
                messages.success(request, 'you are logged in.'.title())
                return redirect('/')
            else:
                messages.error(request, 'invalid username or password'.title())
                return redirect(reverse('login'))
        else:
            print('form is not valid')
    else:
        form = BraiderLogin()

    context = {'form': form}
    return render(request, 'login.html', context)


def fregister(request):
    return render(request, 'registerfirst.html')


def flogin(request):
    return render(request, 'loginfirst.html')

