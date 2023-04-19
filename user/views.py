from django.shortcuts import render, redirect
from django.urls import reverse
from main.models import Braider
from django.contrib import messages
from .forms import Registration

# Create your views here.


def register(request):

    # if request.method == 'POST':
    #
    #     firstname = request.POST['firstname']
    #     lastname = request.POST['lastname']
    #     username = request.POST['username']
    #     usertype = request.POST['usertype']
    #     email = request.POST['email']
    #     password = request.POST['password']
    #     country = request.POST['country']
    #     countrycode = request.POST['countryCode']
    #     phonenumber = request.POST['phonenumber']
    #
    #     phonenumber = '+' + countrycode + phonenumber
    #
    #     print(phonenumber)
    #
    #     print(f'\n\ndear {firstname}, we are Gla'
    #           f'd that you joined Braidstarz!! w'
    #           f'e konw that you are from {country}, '
    #           f'and your email is {email}.\n\n')
    #
    #     braider = Braider(first_name=firstname,
    #                       last_name=lastname,
    #                       user_name=username,
    #                       user_type=usertype,
    #                       # insta_id=instaid,
    #                       email=email,
    #                       password=password,
    #                       phone_number=phonenumber,
    #                       country=country,
    #                       # city=city,
    #                       )
    #
    #     braider.full_clean()
    #     braider.save()
    #
    #     print('\n\nbraider object have been saved\n\n')
    #
    #     messages.add_message(request, messages.INFO, "Hello world.")
    #
    #     return redirect(reverse("register"))

    form = Registration()

    context = {'form': form}

    return render(request, 'register.html', context)


def login(request):
    return render(request, 'login.html')


def fregister(request):
    return render(request, 'registerfirst.html')


def flogin(request):
    return render(request, 'loginfirst.html')

