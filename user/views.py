from django.shortcuts import render, redirect
# from django.urls import reverse
from main.models import Braider, PublicInfo, SocialMedia, LocationInfo, BusinessInfo
from django.contrib import messages
from .forms import BraiderRegistration, BraiderLogin
from django.contrib.auth import authenticate, login, logout
from django.core.exceptions import ValidationError
from django.contrib.auth.hashers import make_password


# Create your views here.

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
                try:
                    braider.delete()
                except:
                    print('braider was not delete. ')
                errors = e.message_dict
                for error in errors:
                    messages.warning(request, error)
                    print('error 1 is trigerred.')
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
                    braider.delete()
                    errors = e.messages
                    for error in errors:
                        messages.warning(request, error)
                        print('error 2 is trigerred.')

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
                        errors = e.messages
                        for e in errors:
                            messages.warning(request, f'{e}')
                            print('error 3 is trigerred.')

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
                            print('validation is made')
                            errors = e.messages
                            for error in errors:
                                messages.warning(request, error)
                                print('error 4 is trigerred.')
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
                                braider.delete()
                                print('validation is made')
                                errors = e.messages
                                for error in errors:
                                    messages.warning(request, error)
                                    print('error 4 is trigerred.')

            if saved:
                messages.success(request, 'your account have been created. wellcome to braidstarz! log in to access your profile'.title())
                return redirect('login')
        else:
            for field_name, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"\n{str(field_name).replace('_', ' ').title()}\n: {error}")
    else:
        form = BraiderRegistration()

    context = {'form': form}
    return render(request, 'register.html', context)
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




