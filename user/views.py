from django.shortcuts import render, redirect
# from django.urls import reverse
from main.models import Braider, PublicInfo, SocialMedia, LocationInfo
from django.contrib import messages
from .forms import BraiderRegistration # BraiderLogin
from django.contrib.auth import authenticate, login, logout
from django.core.exceptions import ValidationError
# from django.contrib.auth.hashers import check_password, make_password


# Create your views here.

def register_page(request):

    if request.method == 'POST':
        form = BraiderRegistration(request.POST)
        if form.is_valid():

            cd = form.cleaned_data

            braider = Braider(
                user_name=cd['user_name'],
                email=cd['email'],
                password=cd['password'],
                phone_number=cd['phone_number'],
            )
            saved = False

            try:
                braider.full_clean()
                braider.save()
                if braider.id:
                    saved = True
            except ValidationError as e:
                errors = e.message_dict
                for e in errors:
                    messages.warning(request, f'{e}')


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
                    errors = e.message_dict
                    braider.delete()
                    for e in errors:
                        messages.warning(request, f'{e}')

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
                        errors = e.messages
                        braider.delete()
                        for e in errors:
                            messages.warning(request, f'{e}')
                    if saved:
                        soc = SocialMedia(
                            insta=cd['insta_id'],
                            rel=braider
                        )
                        try:
                            soc.full_clean()
                            soc.save()
                            if soc.id:
                                saved = True
                        except ValidationError as e:
                            errors = e.messages
                            braider.delete()
                            for e in errors:
                                messages.warning(request, f'{e}')
            if saved:
                messages.success(request, 'you account have been created. wellcome to braidstarz!'.title())
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
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        remember_me = request.POST.get('remember_me', False)

        user = authenticate(request, username=username, password=password)
        print(user)
        if user is not None:
            login(request, user)
            if remember_me:
                request.session.set_expiry(60 * 60 * 24 * 14)  # 2 weeks = 2 weeks' seconds
            return redirect('/')
        else:
            messages.error(request, 'Wrong username or password')

    # form = BraiderLogin()
    # context = {'form': form}
    return render(request, 'login.html')
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




