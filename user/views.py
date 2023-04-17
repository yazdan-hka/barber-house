from django.shortcuts import render, redirect
from django.urls import reverse
from main.models import Braider
from django.contrib import messages



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




        braider = Braider(first_name=firstname,
                          last_name=lastname,
                          user_name=username,
                          user_type=usertype,
                          # insta_id=instaid,
                          email=email,
                          password=password,
                          phone_number=phonenumber,
                          country=country,
                          # city=city,
                          )

        braider.save()
        print('\n\nbraider object have been saved\n\n')

        messages.add_message(request, messages.INFO, "Hello world.")

        messages.debug(request, "%s SQL statements were executed." % email)
        messages.info(request, "Three credits remain in your account.")
        messages.success(request, "Profile details updated.")
        messages.warning(request, "Your account expires in three days.")
        messages.error(request, "Document deleted.")

        return redirect(reverse("register"))

    return render(request, 'register.html')


def login(request):
    return render(request, 'login.html')


def fregister(request):
    return render(request, 'registerfirst.html')


def flogin(request):
    return render(request, 'loginfirst.html')

