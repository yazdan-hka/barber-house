from django.shortcuts import render, redirect
# from django.urls import reverse
from main.models import Braider, PublicInfo, SocialMedia, LocationInfo, BusinessInfo, Customer
from django.contrib import messages
from .forms import BraiderRegistration, BraiderLogin, CustomerRegistration
from django.contrib.auth import authenticate, login, logout
from django.core.exceptions import ValidationError
from django.contrib.auth.hashers import make_password


# Create your views here.
def braider_or_customer(request):
    return render(request, 'braider-or-customer.html')
def register_page(request):

    if request.method == 'POST':
        form = BraiderRegistration(request.POST)
        if form.is_valid():

            cd = form.cleaned_data

            braider = Braider(
                user_name=cd['user_name'],
                email=cd['email'],
                password=make_password(cd['password']),
                phone_number=cd['phone_number'],
            )

            saved = False

            try:
                braider.full_clean()
                braider.save()
                if braider.id:
                    saved = True

            except ValidationError as e:
                print('it may be 37')
                for field, errors in e.message_dict.items():
                    for error in errors:
                        messages.error(request, error)
                try:
                    braider.delete()
                except:
                    print('braider was not delete. ')
            if saved:
                saved = False
                pub = PublicInfo(
                    first_name=cd['first_name'],
                    last_name=cd['last_name'],
                    user_type=cd['user_type'],
                    rel=braider
                )
                try:
                    pub.full_clean()
                    pub.save()
                    if pub.id:
                        saved = True
                except ValidationError as e:
                    print('it may be 62')

                    braider.delete()
                    for field, errors in e.message_dict.items():
                        for error in errors:
                            form.add_error(field, error)

                if saved:
                    saved = False
                    loc = LocationInfo(
                        country=cd['country'],
                        city=cd['city'],
                        rel=braider
                    )
                    try:
                        loc.full_clean()
                        loc.save()
                        if loc.id:
                            saved = True
                    except ValidationError as e:
                        braider.delete()
                        print('it may be 83')

                        for field, errors in e.message_dict.items():
                            for error in errors:
                                form.add_error(field, error)

                    if saved:
                        saved = False
                        realins = cd['insta_id']
                        if realins == '':
                            realins = None
                        soc = SocialMedia(
                            instagram=realins,
                            rel=braider
                        )
                        try:
                            soc.full_clean()
                            soc.save()
                            if soc.id:
                                saved = True

                        except ValidationError as e:
                            braider.delete()
                            print('it may be 106')

                            print('validation is made')
                            for field, errors in e.message_dict.items():
                                for error in errors:
                                    form.add_error(field, error)
                        if saved:
                            saved = False
                            bus = BusinessInfo(
                                rel=braider,
                                website=cd['website']
                            )
                            try:
                                bus.full_clean()
                                bus.save()
                                if bus.id:
                                    saved = True
                            except ValidationError as e:
                                print('it may be 124')

                                braider.delete()
                                print('validation is made')
                                for field, errors in e.message_dict.items():
                                    for error in errors:
                                        form.add_error(field, error)

            if saved:

                send_mail(
                    subject='Email Validation Required',
                    message=f'Hi {cd["first_name"]},\n\nThank you for signing up with our service. To complete your registration, please click on the following link to validate your email address:\n\nhttps://www.braidstarz.art/af4wtesra3r4weaa34rae3wdwf4aeh3a4ewr/\n\nIf you did not sign up for our service, you can safely ignore this email.\n\nThank you,\nThe BraidStarz Team',
                    from_email=settings.EMAIL_HOST_USER,
                    recipient_list=[cd['email']])

                messages.success(request, 'One more step to create your account'.title())
                return redirect('validate-your-email', cd['email'])
        else:
            for field_name, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"\n{str(field_name).replace('_', ' ').title()}\n: {error}")
    else:
        form = BraiderRegistration()

    context = {'form': form}
    return render(request, 'register.html', context)
def customer_register(request):

    if request.method == 'POST':
        form = CustomerRegistration(request.POST)
        if form.is_valid():
            cd = form.cleaned_data

            customer = Customer(
                first_name=cd['first_name'],
                last_name=cd['last_name'],
                user_name=cd['user_name'],
                email=cd['email'],
                password=make_password(cd['password']),
            )

            try:
                customer.full_clean()
                customer.save()
                messages.success(request, "your account have been created!".title())
                return redirect('/')
            except ValidationError as e:
                for field, errors in e.message_dict.items():
                    for error in errors:
                        messages.error(request, error)
        else:
            for field_name, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"\n{str(field_name).replace('_', ' ').title()}\n: {error}")
    else:
        form = CustomerRegistration()

    context = {'form': form}
    return render(request, 'customer-register.html', context)
def login_page(request):
    form = BraiderLogin()

    if request.method == 'POST':
        form = BraiderLogin(request.POST)

        username = form['username'].value()
        password = form['password'].value()
        remember_me = form['remember_me'].value()

        print(f'\n\n\n{username, password, remember_me}')

        user = authenticate(request, username=username, password=password)
        print(user, 'user is authenticated')
        if user is not None:
            login(request, user)
            print('user is logged in')
            
            if remember_me:
                request.session.set_expiry(60 * 60 * 24 * 14)  # 2 weeks = 2 weeks' seconds
            messages.success(request, f'You are logged in dear {username}'.title())
            return redirect('/')
        else:
            messages.error(request, 'Wrong username or password')
    context = {'form': form}
    return render(request, 'login.html', context)
def logout_page(request):
    try:
        messages.success(request, f'you are logged out! comeback soon {request.user.first_name}'.title())
    except:
        messages.success(request, f'you are logged out! goodbye..'.title(), )
    logout(request)
    return redirect('/')
def fregister(request):
    return render(request, 'registerfirst.html')
def flogin(request):
    return render(request, 'loginfirst.html')

def validate_your_email(request, email):
    context = {'email': email}
    return render(request, 'validate-your-email', context)




