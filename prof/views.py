from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.contrib import messages
from .forms import PictureForm, EditProfile
from main.models import Braider
from main.models import Post, PublicInfo, SocialMedia, LocationInfo, BusinessInfo
from django.contrib.auth.decorators import login_required

# Create your views here.


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
        # 'profile_picture',
        # 'saved',
        # 'post',
        'publicinfo__first_name',
        'publicinfo__last_name',
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

    context = {'braider': braider[0]}

    return render(request, 'profile.html', context)

@login_required
def edit_profile(request):

    user_name = request.user.user_name

    braider = Braider.objects.filter(user_name=user_name)
    # \
    #     .select_related(
    #     'publicinfo',
    #     'businessinfo',
    #     'locationinfo',
    # )

    values = braider.values(
        'user_name',
        # 'profile_picture',
        # 'saved',
        # 'post',
        'publicinfo__first_name',
        'publicinfo__last_name',
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
    'user_name': dt['user_name'],
    'first_name': dt['publicinfo__first_name'],
    'last_name': dt['publicinfo__last_name'],
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
    context = {'form': form}

    if request.method == 'POST':
        form_data = EditProfile(request.POST)

        user_name = form_data['user_name'].value()
        first_name = form_data['first_name'].value()
        last_name = form_data['last_name'].value()
        city = form_data['city'].value()
        country = form_data['country'].value()
        instagram = form_data['instagram'].value()
        twitter = form_data['twitter'].value()
        facebook = form_data['facebook'].value()
        tiktok = form_data['tiktok'].value()
        youtube = form_data['youtube'].value()
        business_name = form_data['business_name'].value()
        website = form_data['website'].value()

        if dict_values['user_name'] != user_name:
            # br = Braider.objects.filter(user_name=request.user.user_name).first()
            braider[0].user_name = user_name
            braider.save()
        else:
            pass
        print(last_name)
        if dict_values['first_name'] != first_name or dict_values['last_name'] != last_name:
            print('if is fucking trigered')
            print(braider[0])
            braider[0].publicinfo.first_name = first_name
            braider[0].publicinfo.last_name = last_name
            # braider[0].publicinfo.save()
            braider[0].save()
            print('fucking new last_name', braider[0].publicinfo.last_name)
        else:
            pass

        if dict_values['city'] != city or dict_values['country'] != country:
            braider[0].locationinfo.city = city
            braider[0].locationinfo.country = country
            braider[0].locationinfo.save()
        else:
            pass

        if dict_values['instagram'] != instagram or dict_values['twitter'] != twitter or dict_values['youtube'] != youtube or dict_values['facebook'] != facebook or dict_values['tiktok'] != tiktok:
            braider[0].socialmedia.instagram = instagram
            braider[0].socialmedia.twitter = twitter
            braider[0].socialmedia.facebook = facebook
            braider[0].socialmedia.youtube = youtube
            braider[0].socialmedia.tiktok = tiktok
            braider[0].socialmedia.save()
        else:
            pass

        if dict_values['website'] != website or dict_values['business_name'] != business_name:
            braider[0].businessinfo.business_name = business_name
            braider[0].businessinfo.website = website
            braider[0].businessinfo.save()
        else:
            pass

    return render(request, 'edit-profile.html', context)


def post(request):
    return render(request, 'post.html')


def saved(request):
    return render(request, 'saved.html')


def profile_details(request):
    return render(request, 'profile-details.html')


def post_picture(request):
    context = {}
    if request.user:
        type = PublicInfo.objects.filter(rel=request.user).first().user_type
        print(type)

        if type == "b":
            if request.method == 'POST':
                form = PictureForm(request.POST, request.FILES)
                if form.is_valid():

                    post = Post()
                    if 'description' in form.cleaned_data and form.cleaned_data['description']:
                        post.description = form.cleaned_data['description']
                    post.category = form.cleaned_data['category']
                    post.image = form.cleaned_data['image']
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


