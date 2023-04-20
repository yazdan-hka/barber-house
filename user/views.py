from django.shortcuts import render, redirect
from django.urls import reverse
from  main.models import Braider
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
    ''''''
    # if request.method == 'POST':
    #     form = Registration(request.POST)
    #     if form.is_valid():
    #         cleaned_data = form.cleaned_data
    #         print(cleaned_data)
    #
    #         pass1 = cleaned_data["password1"]
    #         pass2 = cleaned_data["password2"]
    #
    #         if pass1 and pass2 and pass1 == pass1:
    #             print('passwords are the same: ', end='')
    #             print(pass1)
    #
    #         else:
    #             raise ValidationError('Error! passwords are not the same. try again.'.title())
    #
    #         return redirect('login')
    #
    #     else:
    #         cleaned_data = form.cleaned_data
    #         print(cleaned_data)
    #
    #         try:
    #             pass1 = cleaned_data["password1"]
    #             pass2 = cleaned_data["password2"]
    #             if pass2 == pass1 and pass2:
    #                 print('passwords are the same: ', end='')
    #                 print(pass1)
    #             else:
    #                 messages.error(request, 'Error! passwords are not the same. try again.'.title())
    #         except:
    #             messages.error(request, f"Week password. please try again with stronger password.".title())
    #
    #         for field_name, errors in form.errors.items():
    #             for error in errors:
    #                 messages.error(request, f"{field_name.replace('_', ' ').title()}: {error}")
    #         print(cleaned_data)
    #         return redirect('register')
    # else:
    #     form = Registration()
    #
    # context = {'form': form}

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
    return render(request, 'login.html')


def fregister(request):
    return render(request, 'registerfirst.html')


def flogin(request):
    return render(request, 'loginfirst.html')

