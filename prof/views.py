from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.pagination import PageNumberPagination
from rest_framework import status
from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.contrib import messages
from django.core.exceptions import ValidationError
from .forms import PictureForm, EditProfile
from .serializers import BraiderProfileSerializer
from main.models import Braider
from main.models import Post, PublicInfo, SocialMedia, LocationInfo, BusinessInfo
from django.contrib.auth.decorators import login_required
from PIL import Image
from io import BytesIO
from django.core.files.uploadedfile import InMemoryUploadedFile

# Create your views here.

class BraiderProfileAPIView(APIView):
    def get(self, request: Request, user_name):
        try:
            braider = Braider.objects.get(user_name=user_name)
            serializer = BraiderProfileSerializer(braider)

            resp = {
                'status': status.HTTP_200_OK,
                'data': serializer.data, 
                'messages': {
                        'success' : None,
                        'warning' : None,
                        'error' : None,
                        }
                }

            return Response(resp, status=status.HTTP_200_OK)
        except Braider.DoesNotExist:

            resp = {
                'status': status.HTTP_404_NOT_FOUND,
                'data': None, 
                'messages': {
                        'success' : None,
                        'warning' : None,
                        'error' : 'Braider Not Found',
                        }
                }

            return Response(resp, status=status.HTTP_404_NOT_FOUND)

def crop_to_square(image):
    img = Image.open(image)
    width, height = img.size
    if width > height:
        extra = (width - height) / 2
        img = img.crop((extra, 0, width - extra, height))
    else:
        extra = (height - width) / 2
        img = img.crop((0, extra, width, height - extra))
    img = img.resize((900, 900))
    buffer = BytesIO()
    img.save(buffer, format='JPEG')
    image_file = InMemoryUploadedFile(buffer, None, 'temp.jpg', 'image/jpeg', buffer.getbuffer().nbytes, None)
    return image_file

def profile(request, user_name):

    braider = Braider.objects.filter(user_name=user_name)

    #.select_related(
        # 'locationinfo', 'businessinfo', 'publicinfo')
    #.values(
    #                         'locationinfo__country',
    #                         'locationinfo__city',
    #                         'businessinfo',
    #                         'publicinfo__first_name',
    # )

    braider = braider.values(
        'user_name',
        'publicinfo__profile_picture',
        # 'saved',
        # 'post',
        'publicinfo__first_name',
        'publicinfo__last_name',
        'publicinfo__biography',
        'locationinfo__city',
        'locationinfo__country',
        'phone_number',
        'show_phone',
        'email',
        'posts__image',
        'socialmedia__instagram',
        'socialmedia__twitter',
        'socialmedia__facebook',
        'socialmedia__tiktok',
        'socialmedia__youtube',
        'businessinfo__name',
        'businessinfo__website',
        # 'businessinfo__location'
        )

    context = {'braider': braider[0]}

    return render(request, 'profile.html', context)
@login_required
def edit_profile(request):
    user_name = request.user.user_name
    braider = Braider.objects.filter(user_name=user_name)

    values = braider.values(
        'user_name',
        'publicinfo__profile_picture',
        # 'saved',
        # 'post',
        'publicinfo__first_name',
        'publicinfo__last_name',
        'publicinfo__biography',
        'locationinfo__city',
        'locationinfo__country',
        'phone_number',
        'show_phone',
        'email',
        'socialmedia__instagram',
        'socialmedia__twitter',
        'socialmedia__facebook',
        'socialmedia__tiktok',
        'socialmedia__youtube',
        'businessinfo__name',
        'businessinfo__website',
        # 'businessinfo__location'
    )

    dt = values[0]

    dict_values = {
    'profile_picture': dt['publicinfo__profile_picture'],
    'user_name': dt['user_name'],
    'first_name': dt['publicinfo__first_name'],
    'last_name': dt['publicinfo__last_name'],
    'biography': dt['publicinfo__biography'],
    'city': dt['locationinfo__city'],
    'country': dt['locationinfo__country'],
    # '': dt['phone_number'],
    # '': dt['show_phone'],
    # '': dt['email'],
    'instagram': dt['socialmedia__instagram'],
    'twitter': dt['socialmedia__twitter'],
    'facebook': dt['socialmedia__facebook'],
    'tiktok': dt['socialmedia__tiktok'],
    'youtube': dt['socialmedia__youtube'],
    'business_name': dt['businessinfo__name'],
    'website': dt['businessinfo__website'],
    }

    form = EditProfile(initial=dict_values)
    context = {'form': form, 'pp': dt['publicinfo__profile_picture']}

    if request.method == 'POST':
        form_data = EditProfile(request.POST, request.FILES)
        if form_data.is_valid():
            user_name = form_data['user_name'].value()
            try:
                profile_picture = request.FILES['profile_picture']
            except:
                profile_picture = dt['publicinfo__profile_picture']

            first_name = form_data['first_name'].value()
            last_name = form_data['last_name'].value()
            biography = form_data['biography'].value()
            city = form_data['city'].value()
            country = form_data['country'].value()
            instagram = form_data['instagram'].value()
            twitter = form_data['twitter'].value()
            facebook = form_data['facebook'].value()
            tiktok = form_data['tiktok'].value()
            youtube = form_data['youtube'].value()
            business_name = form_data['business_name'].value()
            website = form_data['website'].value()



            if instagram == '':
                instagram = None

            if facebook == '':
                facebook = None

            if twitter == '':
                twitter = None

            if youtube == '':
                youtube = None

            if tiktok == '':
                tiktok = None

            if biography == '':
                biography = None

            braider = Braider.objects.get(user_name=dt['user_name'])
            print('\n', type(braider), '\n')

            print(user_name)
            if dict_values['user_name'] != user_name:
                if Braider.objects.filter(user_name=user_name).first():
                    messages.error(request, 'Your Username was not changed because it was already taken by another user.')
                else:
                    braider.user_name = user_name
                    braider.save()
            else:
                pass

            if dict_values['biography'] != biography or dict_values['first_name'] != first_name or dict_values['last_name'] != last_name or dict_values['profile_picture'] != profile_picture:
                print('pub info is fucking changed.')
                try:
                    braider.publicinfo.first_name = first_name
                    braider.publicinfo.last_name = last_name
                    braider.publicinfo.biography = biography
                    if braider.publicinfo.profile_picture != profile_picture:
                        braider.publicinfo.profile_picture.delete()
                        picture = crop_to_square(profile_picture)
                    else:
                        picture = profile_picture
                    print(picture)
                    braider.publicinfo.profile_picture = picture
                    braider.publicinfo.save()
                except ValidationError as e:
                    for field, errors in e.message_dict.items():
                        for error in errors:
                            form.add_error(field, error)
            else:
                pass

            if dict_values['city'] != city or dict_values['country'] != country:
                print('location info has been changed')
                braider.locationinfo.city = city
                braider.locationinfo.country = country
                braider.locationinfo.save()
            else:
                pass

            if dict_values['instagram'] != instagram or dict_values['twitter'] != twitter or dict_values['youtube'] != youtube or dict_values['facebook'] != facebook or dict_values['tiktok'] != tiktok:
                print('social info is changed')
                braider.socialmedia.instagram = instagram
                braider.socialmedia.twitter = twitter
                braider.socialmedia.facebook = facebook
                braider.socialmedia.youtube = youtube
                braider.socialmedia.tiktok = tiktok
                braider.socialmedia.save()
            else:
                pass

            old_business_name = dict_values['business_name']

            if old_business_name is None:
                old_business_name = ''

            if dict_values['website'] != website or old_business_name != business_name:
                print('business info is changed so i will print the old bussiness name and the new one for fun:\n')
                print(f'old is <{old_business_name}>')
                print(f'new is <{business_name}>')

                braider.businessinfo.name = business_name
                braider.businessinfo.website = website
                braider.businessinfo.save()
            else:
                pass
            messages.success(request, 'Your profile now is more compelete :)')
            return redirect('profile', user_name=braider.user_name)
        else:
            for field_name, errors in form_data.errors.items():
                for error in errors:
                    messages.error(request, f"\n{str(field_name).replace('_', ' ').title()}\n: {error}")
        return redirect('edit-profile')

    return render(request, 'edit-profile.html', context)
def posts(request, user_name):
    braider = Braider.objects.filter(user_name=user_name).first()
    posts = Post.objects.filter(braider=braider)
    un = braider.user_name

    context = {'posts': posts, 'pp': braider.publicinfo.profile_picture, 'un': un}

    return render(request, 'post.html', context)
def saved(request):
    return render(request, 'saved.html')
def profile_details(request):
    return render(request, 'profile-details.html')
def post_picture(request):
    context = {}
    if request.user:
        if 'braider' in str(request.user):
            if request.method == 'POST':
                form = PictureForm(request.POST, request.FILES)
                if form.is_valid():

                    post = Post()
                    if 'description' in form.cleaned_data and form.cleaned_data['description']:
                        post.description = form.cleaned_data['description']
                    post.category = form.cleaned_data['category']
                    post.image = crop_to_square(form.cleaned_data['image'])
                    post.braider = request.user
                    post.save()

                    return redirect('index')
                else:
                    for field_name, errors in form.errors.items():
                        for error in errors:
                            messages.warning(request, f"\n{str(field_name).replace('_', ' ').title()}\n: {error}")
                    return redirect('post-picture')
            else:
                form = PictureForm()
                context = {'form': form}
        else:
            messages.warning(request, 'sorry you cannot post media'.title())
            return redirect('index')
    else:
        messages.warning(request, 'You must be logged in!')
        return redirect('login')
    return render(request, 'post-picture.html', context)


