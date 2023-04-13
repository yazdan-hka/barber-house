from django.shortcuts import render

# Create your views here.


def profile(request):
    return render(request, 'profile.html')


def post(request):
    return render(request, 'post.html')


def saved(request):
    return render(request, 'saved.html')


def profile_details(request):
    return render(request, 'profile-details.html')


def post_details(request):
    return render(request, 'post-details.html')

