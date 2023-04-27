from django.shortcuts import render, redirect
from .forms import PictureForm
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
            print('form seems to be valid')
            print(form)
            return redirect('home')
        else:
            return redirect('post-picture')
    else:
        form = PictureForm()
    return render(request, 'post-picture.html', {'form': form})


