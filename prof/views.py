from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import PictureForm
from main.models import Post
# Create your views here.


def profile(request):
    return render(request, 'profile.html')


def post(request):
    return render(request, 'post.html')


def saved(request):
    return render(request, 'saved.html')


def profile_details(request):
    return render(request, 'profile-details.html')


def post_picture(request):
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
    return render(request, 'post-picture.html', {'form': form})


