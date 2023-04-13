from django.shortcuts import render

# Create your views here.


def register(request):
    return render(request, 'register.html')


def login(request):
    return render(request, 'login.html')


def fregister(request):
    return render(request, 'registerfirst.html')


def flogin(request):
    return render(request, 'loginfirst.html')

