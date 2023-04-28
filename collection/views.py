from django.shortcuts import render, reverse
from django.contrib import messages
from main.models import Post
# Create your views here.

def collection(request):
    posts = Post.objects.all()
    context = {'posts': posts}
    return render(request, 'collection.html', context)


def post(request, id):
    return render(request, 'collection-1.html')
