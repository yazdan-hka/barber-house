from django.shortcuts import render, redirect
from .models import Braider
from django.urls import reverse
from django.db.models import Q
from django.contrib import messages
from .forms import BraiderFinder

# Create your views here.

def index(request):
    if request.method == 'POST':
        form = BraiderFinder(request.POST)

        if form.is_valid():
            cform = form.cleaned_data
            search = cform['search']
            query = search.lower()
            braiders = Braider.objects.filter(
                    Q(country__icontains=query) |
                    Q(city__icontains=query) |
                    Q(first_name__icontains=query) |
                    Q(last_name__icontains=query) |
                    Q(user_name__icontains=query)
                )
            if braiders:
                messages.success(request, f'Wow! {len(braiders)} Braiders find you.'.title())
                context = {'form': form, 'braiders': braiders}
            else:
                print('no result is found')
                messages.warning(request, f'<b>{query}</b>: No braider is found. search something better.'.title())
                return redirect('index')
    else:
        form = BraiderFinder()
        context = {'form': form}

    return render(request, 'index.html', context)

def about(request):
    return render(request, 'about.html')
