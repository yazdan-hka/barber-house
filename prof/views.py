from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.contrib import messages
from .forms import PictureForm
from main.models import Braider
from main.models import Post, PublicInfo
from  django.contrib.auth.decorators import login_required

# Create your views here.


def profile(request, user_name):
    
    braider = Braider.objects.filter(user_name=user_name).first()
    context = {'braider': braider}

    return render(request, 'profile.html', context)


def edit_profile(request):
    return render(request, 'edit-profile.html')


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


