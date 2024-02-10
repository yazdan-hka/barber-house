from django.shortcuts import render, redirect, HttpResponse
from django.urls import reverse
from main.models import Braider, PublicInfo, SocialMedia, LocationInfo, BusinessInfo, Customer, Verification, CustomerVerification
from django.contrib import messages
from .forms import BraiderRegistration, BraiderLogin, CustomerRegistration, CreateNewPassword
from django.contrib.auth import authenticate, login, logout
from django.core.exceptions import ValidationError
from django.contrib.auth.hashers import make_password
import secrets
from django.db.models import Q
from django.core.mail import send_mail
from django.conf import settings
from django.template.loader import render_to_string
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import status
from .serializer import RegisterBraiderSerializer, LoginBraiderSerializer



# Create your views here.
def braider_or_customer(request):
    return render(request, 'braider-or-customer.html')

def braider_register(request):
    return render(request, 'regiater-braider.html')

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
                link = f'https://www.braidstarz.com/user/validate-email/{braider.user_name}/{token.token}/'
                print(link)

                context = {'name': cd['first_name'], 'link': link}
                html_message = render_to_string('validate-email-email-template.html', context)

                send_mail(
                    subject='Email Validation Required',
                    message=f'Hi {cd["first_name"]},\n\nThank you for signing up with our service. To complete your registration, please click on the following link to validate your email address:\n\n{link}\n\nIf you did not sign up for our service, you can safely ignore this email.\n\nThank you,\nThe BraidStarz Team',
                    from_email=settings.EMAIL_HOST_USER,
                    html_message=html_message,
                    recipient_list=[cd['email']],
                )

                messages.success(request, 'One more step to create your account'.title())
                return redirect('validate-your-email', user_name=braider.user_name)
        else:
            for field_name, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"\n{str(field_name).replace('_', ' ').title()}\n: {error}")
    else:
        form = BraiderRegistration()

    context = {'form': form}
    return render(request, 'register.html', context)

class RegisterBraiderAPIView(APIView):

    def post(self, request: Request, *args, **kwargs):
        serializer = RegisterBraiderSerializer(data=request.data)

        if serializer.is_valid():
            # Save the data to the database using the serializer's create method
            braider_instance = serializer.create(serializer.validated_data)

            braider = Braider.objects.filter(user_name=request.data['user_name']).first()
            first_name = request.data['public_info']['first_name']

            token = Verification.objects.filter(rel=braider).first()
            link = f'https://www.braidstarz.com/user/validate-email/{first_name}/{token.token}/'

            context = {'name': first_name, 'link': link}
            html_message = render_to_string('validate-email-email-template.html', context)

            send_mail(
                subject='Email Validation Required',
                message=f'Hi {first_name},\n\nThank you for signing up with our service. To complete your registration, please click on the following link to validate your email address:\n\n{link}\n\nIf you did not sign up for our service, you can safely ignore this email.\n\nThank you,\nThe BraidStarz Team',
                from_email=settings.EMAIL_HOST_USER,
                html_message=html_message,
                recipient_list=[request.data['email']],
            )

            return Response(braider_instance, {"message": "Registration successful"}, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

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
            except ValidationError as e:
                for field, errors in e.message_dict.items():
                    for error in errors:
                        messages.error(request, error)

            if customer.id:
                token = CustomerVerification.objects.filter(rel=customer).first()
                link = f'https://www.braidstarz.com/user/validate-email/{customer.user_name}/{token.token}/'
                print(link)

                context = {'name': cd['first_name'], 'link': link}
                html_message = render_to_string('validate-email-email-template.html', context)

                send_mail(
                    subject='Email Validation Required',
                    message=f'Hi {cd["first_name"]},\n\nThank you for signing up with our service. To complete your registration, please click on the following link to validate your email address:\n\n{link}\n\nIf you did not sign up for our service, you can safely ignore this email.\n\nThank you,\nThe BraidStarz Team',
                    from_email=settings.EMAIL_HOST_USER,
                    html_message=html_message,
                    recipient_list=[cd['email']])

                messages.success(request, 'One more step to create your account'.title())
                return redirect('validate-your-email', user_name=customer.user_name)
        else:
            for field_name, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"\n{str(field_name).replace('_', ' ').title()}\n: {error}")
    else:
        form = CustomerRegistration()

    context = {'form': form}
    return render(request, 'customer-register.html', context)

class LoginAPIView(APIView):
    def post(self, request):
        serializer = LoginBraiderSerializer(data=request.data)

        if serializer.is_valid():
            username = serializer.validated_data['username']
            password = serializer.validated_data['password']
            remember_me = serializer.validated_data.get('remember_me', False)

            user = authenticate(request, username=username, password=password)

            if user is not None:
                if "Customer object " in str(user):
                    try:
                        verif = CustomerVerification.objects.filter(rel=user).first()
                    except CustomerVerification.DoesNotExist:
                        verif = None

                    if verif and not verif.is_email_verified:
                        messages.error(request, 'Your email must be verified before you can log in. Please verify your email.')
                        return Response({'error': 'Email not verified'}, status=status.HTTP_400_BAD_REQUEST)
                else:
                    try:
                        verif = Verification.objects.filter(rel=user).first()
                    except Verification.DoesNotExist:
                        verif = None

                    if verif and not verif.is_email_verified:
                        messages.error(request, 'Your email must be verified before you can log in. Please verify your email.')
                        return Response({'error': 'Email not verified'}, status=status.HTTP_400_BAD_REQUEST)
                if remember_me:
                    request.session.set_expiry(60 * 60 * 24 * 7)  # 1 week in seconds

                login(request, user)

                messages.success(request, f'You are logged in dear {username}')
                return Response({'message': f'You are logged in dear {username}'})
            else:
                messages.error(request, 'Wrong username or password')
                return Response({'error': 'Wrong username or password'}, status=status.HTTP_401_UNAUTHORIZED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

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
            try:
                verif = Verification.objects.filter(rel=user).first()
            except:
                verif = CustomerVerification.objects.filter(rel=user).first()

            print(verif)

            if verif.is_email_verified == False:
                messages.error(request, 'your email must be verified for you to be able to log in. verify your email.'.title())
                return redirect('validate-your-email', user_name=user.user_name)

            if remember_me:
                request.session.set_expiry(60 * 60 * 24 * 7)  # 1 weeks = 1 weeks' seconds

            login(request, user)
            print('user is logged in')

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
        messages.success(request, f'you are logged out! goodbye..'.title())
    logout(request)
    return redirect('/')
def fregister(request):
    return render(request, 'registerfirst.html')
def flogin(request):
    return render(request, 'loginfirst.html')
def validate_your_email(request, user_name):

    try:
        user = Braider.objects.filter(user_name=user_name).first()
        verification = Verification.objects.filter(rel=user).first()
        token = secrets.token_urlsafe(32)
        verification.token = token
        verification.save()
    except:
        user = Customer.objects.filter(user_name=user_name).first()
        verification = CustomerVerification.objects.filter(rel=user).first()
        token = secrets.token_urlsafe(32)
        verification.token = token
        verification.save()

    email = user.email
    link = f'https://www.braidstarz.com/user/validate-email/{user.user_name}/{token}/'

    try:

        context = {'name': user.user_name, 'link': link}
        html_message = render_to_string('validate-email-email-template.html', context)

        send_mail(
            subject='Email Validation Required',
            message=f'Hi {user.user_name},\n\nThank you for signing up with our service. To complete your <b>registration</b>, please click on the following link to validate your email address:\n\n{link}\n\nIf you did not sign up for our service, you can safely ignore this email.\n\nThank you,\nThe BraidStarz Team',
            from_email=settings.EMAIL_HOST_USER,
            html_message=html_message,
            recipient_list=[email])

        messages.success(request, 'Email have been sent.')
    except:
        messages.error(request, 'Email could not be sent. Try again.')

    if request.method == 'POST':

        link = f'https://www.braidstarz.com/user/validate-email/{user.user_name}/{token}/'

        try:

            context = {'name': user.user_name, 'link': link}
            html_message = render_to_string('validate-email-email-template.html', context)

            send_mail(
                subject='Email Validation Required',
                message=f'Hi {user.user_name},\n\nThank you for signing up with our service. To complete your <b>registration</b>, please click on the following link to validate your email address:\n\n{link}\n\nIf you did not sign up for our service, you can safely ignore this email.\n\nThank you,\nThe BraidStarz Team',
                from_email=settings.EMAIL_HOST_USER,
                html_message=html_message,
                recipient_list=[email])
            messages.success(request, 'Email have been sent.')
        except:
            messages.error(request, 'Email could not be sent. Try again.')

        return redirect('validate-your-email', user_name=user.user_name)
    return render(request, 'validate-your-email.html')
def validate_email(request, user_name, token):

    try:
        user = Braider.objects.filter(user_name=user_name).first()
        print('try to find braider associated with this user name')
    except:
        user = Customer.objects.filter(user_name=user_name).first()
        print('try to find customer associated with this user name')

    if user:
        try:
            verific = Verification.objects.filter(rel=user).first()
            print('trying to find associated token with braider object')
        except:
            verific = CustomerVerification.objects.filter(rel=user).first()
            print('trying to find associated token with customer object')

        if verific:
            print('the token is True')
            print(f'user token: {verific.token}\n is expired: {verific.is_expired()}\n token: {token}')
            if verific.token == token and verific.is_expired() is False:
                print('token is valid')
                verific.is_email_verified = True
                verific.save()
                messages.success(request, 'Your account have been created. Log in to access your profile')
                return redirect('/user/login')
            else:
                print('token is invalid')
                messages.error(request, 'Token is invalid or expired.')
                return redirect('/')
        else:
            print('no token')
    else:
        messages.error(request, 'Token is invalid.')
        return redirect('/')


    # print(token)
    # matched_token = Verification.objects.filter(token=token).first()
    # if matched_token:
    #     pass
    # else:
    #     matched_token = CustomerVerification.objects.filter(token=token).first()
    #
    # if matched_token:
    #     if matched_token.rel.id == id and matched_token.is_expired() is False:
    #         messages.success(request, 'Your account have been created. Log in to access your profile')
    #
    #         matched_token.is_email_verified = True
    #         matched_token.save()
    #
    #         return redirect('/user/login')
    #     else:
    #         messages.error(request, 'Token is invalid or expired.')
    #         return redirect('/')
    # else:
    #     messages.error(request, 'Token is invalid.')
    #     return redirect('/')
def reset_your_password_1(request):
    if request.method == 'POST':
        query = request.POST['data']

        if (
                query == '' or
                ' ' in query or
                len(query) < 4 or
                len(query) > 260
        ):
            messages.error(request, 'Wrong username or email.')
            return redirect('reset-your-password-1')
        else:
            pass

        try:
            user = Braider.objects.filter(
                Q(user_name__icontains=query) |
                Q(email__icontains=query)
            ).first()
        except:
            user = Customer.objects.filter(
                Q(user_name__icontains=query) |
                Q(email__icontains=query)
            ).first()

        if user:
            try:
                token = Verification.objects.filter(rel=user).first()
            except:
                token = CustomerVerification.objects.filter(rel=user).first()


            link = f'https://www.braidstarz.com/user/create-new-password/{user.id}/{token.token}/'
            print(link)

            context = {'name': user.user_name, 'link': link}
            html_message = render_to_string('reset-password-email-template.html', context)

            send_mail(
                subject='Password Reset Request',
                message=f'Hi {user.user_name},\n\nWe received a request to reset your password. If you initiated this request, please click on the following link to reset your password:\n\n{link}\n\nIf you did not request a password reset, please ignore this email.\n\nThank you,\nThe BraidStarz Team',
                from_email=settings.EMAIL_HOST_USER,
                html_message=html_message,
                recipient_list=[user.email])

            return redirect('reset-your-password-2')
        else:
            messages.success(request, f'There were no account associated with {query}. Try again or make a new account.')

    return render(request, 'reset-your-password-1.html')
def reset_your_password_2(request):
    return render(request, 'reset-your-password-2.html')
def create_new_password(request, token, id):

    try:
        token_exist = Verification.objects.filter(token=token).first()
    except:
        token_exist = CustomerVerification.objects.filter(token=token).first()

    if token_exist:
        try:
            user = Braider.objects.filter(id=id).first()
        except:
            user = Customer.objects.filter(id=id).first()

        if user:
            if token_exist.rel.id == user.id:
                form = CreateNewPassword()
                context = {'form': form}
                if request.method == 'POST':
                    form = CreateNewPassword(request.POST)
                    if form.is_valid():

                        cleaned = form.clean()
                        password = cleaned.get('password')

                        user.password = password
                        user.save()

                        messages.success(request, 'Your password has been changed.')
                        return redirect('/')
                    else:
                        for field_name, errors in form.errors.items():
                            for error in errors:
                                messages.error(request, f"\n{str(field_name).replace('_', ' ').title()}\n: {error}")

            else:
                messages.error(request, 'Token is invalid or expired. Do it again.')
                return redirect('reset-your-password-1')
    else:
        messages.error(request, 'Invalid token.')
        return redirect('reset-your-password-1')

    return render(request, 'create-new-password.html', context)


# def test_email(request):
#
#     name = 'yazdan'
#     link = 'http://www.braidstarz.com/user/flogin'
#
#     context = {'first_name': cd['first_name'], 'link': link}
#     html_message = render_to_string('validate-email-email-template.html', context)
#
#     send_mail(
#         subject='Email Validation Required',
#         message=f'Hi {cd["first_name"]},\n\nThank you for signing up with our service. To complete your registration, please click on the following link to validate your email address:\n\n{link}\n\nIf you did not sign up for our service, you can safely ignore this email.\n\nThank you,\nThe BraidStarz Team',
#         html_message=html_message,
#         from_email=settings.EMAIL_HOST_USER,
#         recipient_list=[cd['email']],
#     )
#
#     print('\n\nemail is sent\n\n')
#     return HttpResponse('<h3>see if it worked.</h3>')




