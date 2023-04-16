from django.shortcuts import render, redirect
from django.urls import reverse

# Create your views here.


def register(request):

    if request.method == 'POST':

        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        username = request.POST['username']
        usertype = request.POST['usertype']
        email = request.POST['email']
        password = request.POST['password']
        country = request.POST['country']
        countrycode = request.POST['countryCode']
        phonenumber = request.POST['phonenumber']

        print(f'\n\ndear {firstname}, we are Glad that you joined Braidstarz!! we konw that you are from {country}, '
              f'and your email is {email}.\n\n')

        return redirect(reverse("user:login"))

    return render(request, 'register.html')


def login(request):
    return render(request, 'login.html')


def fregister(request):
    return render(request, 'registerfirst.html')


def flogin(request):
    return render(request, 'loginfirst.html')

