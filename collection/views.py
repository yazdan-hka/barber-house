from django.shortcuts import render
from django.contrib import messages
from main.models import Post
# Create your views here.

def collection(request):
    posts = Post.objects.all()
    print(posts)
    for i in posts:
        print(i.image)
    context = {'posts': posts}
    return render(request, 'collection.html', context)


def collection_1(request):
    return render(request, 'collection-1.html')
