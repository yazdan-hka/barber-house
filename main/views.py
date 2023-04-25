from django.shortcuts import render, redirect
from .models import Braider, LocationInfo
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
            # braiders = Braider.objects.filter(
            #         Q(locationinfo__country__icontains=query) |
            #         Q(locationinfo__city__icontains=query) |
            #         Q(publicinfo__first_name__icontains=query) |
            #         Q(publicinfo__last_name__icontains=query) |
            #         Q(user_name__icontains=query)
            #     )

            # braiders = Braider.objects.select_related(
            #     'locationinfo', 'businessinfo', 'publicinfo').values(
            #                         'user_name',
            #                         'locationinfo__country',
            #                         'locationinfo__city',
            #                         'businessinfo__website',
            #                         'publicinfo__first_name',
            #                         'publicinfo__last_name'
            #                         )

            braiders = Braider.objects.filter(
                Q(user_name__icontains=query) |
                Q(publicinfo__first_name__icontains=query) |
                Q(publicinfo__last_name__icontains=query) |
                Q(locationinfo__country__icontains=query) |
                Q(locationinfo__city__icontains=query)
            ).prefetch_related('publicinfo_set', 'locationinfo_set', 'businessinfo_set')
            print('braiders are queried')

            braider_info = []

            if braiders:
                print('braiders are found')
                for braider in braiders:
                    print('starting iteration braiders')
                    location_info = braider.locationinfo_set.first()
                    business_info = braider.businessinfo_set.first()
                    public_info = braider.publicinfo_set.first()
                    try:
                        print('tryin to save the braider to list')
                        print(public_info.user_type)
                        if public_info.user_type == 'b':
                            print('braider is braider, saving it.')
                            braider_info.append({
                                'user_name': braider.user_name,
                                'country': location_info.country,
                                'city': location_info.city,
                                'website': business_info.website,
                                'name': public_info.first_name + " " + public_info.last_name,
                            })
                        else:
                            pass
                    except:
                        print('tryin to save the braider to list but in except')
                        if public_info.user_type == 'b':
                            print('braider is braider, saving it.')
                            braider_info.append({
                                'user_name': braider.user_name,
                                'country': location_info.country,
                                'city': location_info.city,
                                'name': public_info.first_name + " " + public_info.last_name,
                            })
                        else:
                            pass

                messages.success(request, f'Wow! {len(braider_info)} Braiders find you.'.title())
                context = {'form': form, 'braiders': braider_info}
            else:
                print('no result is found')
                messages.warning(request, f'{query}: No braider is found. search something better.'.title())
                return redirect('index')
    else:
        form = BraiderFinder()
        context = {'form': form}

    return render(request, 'index.html', context)

def about(request):
    return render(request, 'about.html')
