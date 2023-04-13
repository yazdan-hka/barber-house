from django.shortcuts import render

# Create your views here.

def collection(request):
    return render(request, 'collection.html')


def collection_1(request):
    return render(request, 'collection-1.html')
