from django.shortcuts import render, redirect
from .models import Braider
from django.urls import reverse
from django.db.models import Q
from django.contrib import messages

# Create your views here.

def index(request):
    context = {}
    if request.method == 'POST':

        search = request.POST['search']
        query = search.lower()

        print(f'\n search is: {query} \n')

        braiders = Braider.objects.filter(
                Q(country__icontains=query) |
                Q(city__icontains=query) |
                Q(first_name__icontains=query) |
                Q(last_name__icontains=query) |
                Q(user_name__icontains=query)
            )

        print('query is done\n')

        if braiders:
            messages.success(request, f'Wow! {len(braiders)} Braiders find you.'.title())
            context = {'braiders': braiders}
        else:
            print('no result is found')
            messages.warning(request, f'<b>{query}</b>: No braider is found. search something better.'.title())
            return redirect('index')

    return render(request, 'index.html', context)

def about(request):
    return render(request, 'about.html')
