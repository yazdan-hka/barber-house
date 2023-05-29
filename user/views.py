from django.shortcuts import render, redirect
from django.urls import reverse
from main.models import Braider, PublicInfo, SocialMedia, LocationInfo, BusinessInfo, Customer, Verification
from django.contrib import messages
from .forms import BraiderRegistration, BraiderLogin, CustomerRegistration
from django.contrib.auth import authenticate, login, logout
from django.core.exceptions import ValidationError
from django.contrib.auth.hashers import make_password
import secrets
from django.core.mail import send_mail
from django.conf import settings


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
                    print(braider.id)
                    print('braider was not delete. ')
            if saved:
                saved = False
                pub = PublicInfo(
                    first_name=cd['first_name'],
                    last_name=cd['last_name'],
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
                token = Verification.objects.filter(rel=braider).first()
                link = f'http://127.0.0.1:8000/user/validate-email/{braider.id}/{token.token}/'
                print(link)

                # send_mail(
                #     subject='Email Validation Required',
                #     message=f'Hi {cd["first_name"]},\n\nThank you for signing up with our service. To complete your registration, please click on the following link to validate your email address:\n\n{link}\n\nIf you did not sign up for our service, you can safely ignore this email.\n\nThank you,\nThe BraidStarz Team',
                #     from_email=settings.EMAIL_HOST_USER,
                #     recipient_list=[cd['email']])

                messages.success(request, 'One more step to create your account'.title())
                return redirect('validate-your-email', pk=braider.pk)
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
            verif = Verification.objects.filter(rel=user).first()

            if verif.is_email_verified == False:
                messages.error(request, 'your email must be verified for you to be able to log in. verify your email.'.title())
                return redirect('validate-your-email', pk=user.id)

            login(request, user)
            print('user is logged in')
            
            if remember_me:
                request.session.set_expiry(60 * 60 * 24 * 7)  # 1 weeks = 1 weeks' seconds
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
def validate_your_email(request, pk):

    braider = Braider.objects.filter(id=pk).first()
    token = secrets.token_urlsafe(32)
    verification = Verification.objects.filter(rel=braider).first()
    verification.token = token
    verification.save()

    if request.method == 'POST':
        email = braider.email
        token = Verification.objects.filter(rel=braider).first()
        link = f'http://127.0.0.1:8000/user/validate-email/{braider.id}/{token.token}/'

        print(link)

        # try:
        #     send_mail(
        #         subject='Email Validation Required',
        #         message=f'Hi {braider.user_name},\n\nThank you for signing up with our service. To complete your registration, please click on the following link to validate your email address:\n\n{link}\n\nIf you did not sign up for our service, you can safely ignore this email.\n\nThank you,\nThe BraidStarz Team',
        #         from_email=settings.EMAIL_HOST_USER,
        #         recipient_list=[email])
        #     messages.success(request, 'Email have been sent.')
        # except:
        #     messages.error(request, 'Email could not be sent. Try again.')
        # return redirect('validate-your-email', pk=braider.id)

    return render(request, 'validate-your-email.html')
def validate_email(request, token, id):

    matched_token = Verification.objects.filter(token=token).first()

    if matched_token:
        if matched_token.rel.id == id and matched_token.is_expired() is False:
            messages.success(request, 'Your account have been created. Log in to access your profile')

            matched_token.is_email_verified = True
            matched_token.save()

            return redirect('/user/login')
        else:
            messages.error(request, 'Token is invalid or expired.')
            return redirect('/')
    else:
        messages.error(request, 'Token is invalid.')
        return redirect('/')





