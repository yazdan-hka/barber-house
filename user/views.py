from django.shortcuts import render, redirect
from django.urls import reverse
from main.models import Braider
from django.contrib import messages
from .forms import BraiderRegistration, BraiderLogin
from django.contrib.auth import authenticate, login, logout
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

    if request.user.is_authenticated and isinstance(request.user, Braider):
        # user is logged in and is an instance of MyModel
        return redirect('profile')
        # , {'user': request.user}
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        remember_me = request.POST.get('remember_me', False)

        user = authenticate(request, username=username, password=password)
        print(user)
        if user is not None:
            login(request, user)
            # if remember_me:
            #     request.session.set_expiry(0)  # 2 weeks = 2 weeks' seconds
            return redirect('/')
        else:
            messages.error(request, 'Wrong username or password')

    # form = BraiderLogin()
    # context = {'form': form}
    return render(request, 'login.html')
def logout_page(request):
    messages.success(request, f'you are logged out! goodbye{request.user.first_name}'.title(), )
    logout(request)
    return redirect('/')
def fregister(request):
    return render(request, 'registerfirst.html')
def flogin(request):
    return render(request, 'loginfirst.html')




