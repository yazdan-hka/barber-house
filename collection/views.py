from django.shortcuts import render, reverse
from django.contrib import messages
from main.models import Post
# Create your views here.

def collection(request):
    posts = Post.objects.all()

    for post in posts:
        print(post.braider.publicinfo.profile_picture)

    context = {'posts': posts}
    return render(request, 'collection.html', context)


def collection_picture(request, id):

    post = Post.objects.get(id=id)

    context = {'post': post}

    return render(request, 'collection-picture.html', context)
