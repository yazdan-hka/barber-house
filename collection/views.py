from django.shortcuts import render
from django.contrib import messages
# Create your views here.

def collection(request):

    messages.success(request, "Profile details updated.")
    return render(request, 'collection.html')


def collection_1(request):
    return render(request, 'collection-1.html')
