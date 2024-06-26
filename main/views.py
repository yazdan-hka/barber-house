from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.pagination import PageNumberPagination
from rest_framework import status
from .serializers import SearchBraiderSerializer, Search
from django.shortcuts import render, redirect
from .models import Braider, Post
from django.urls import reverse
from django.db.models import Q
from django.contrib import messages
from .forms import BraiderFinder, MessageForm
# from django.conf import settings

# Create your views here.

class SearchBraidersAPIView(APIView):
    def get(self, request: Request):
        serializer = Search(data=request.data)

        if serializer.is_valid():
            keyword = request.data.get('text')
            braiders = Braider.objects.filter(
                    Q(user_name__icontains=keyword) |
                    Q(publicinfo__first_name__icontains=keyword) |
                    Q(publicinfo__last_name__icontains=keyword) |
                    Q(locationinfo__country__icontains=keyword) |
                    Q(locationinfo__city__icontains=keyword) |
                    Q(socialmedia__instagram__icontains=keyword) |
                    Q(businessinfo__name__icontains=keyword) 
                )
            
            count = len(braiders)
            results = SearchBraiderSerializer(braiders, many=True)

            if count > 0:

                resp = {
                    'status': status.HTTP_200_OK, 
                    'data': results.data, 
                    'messages': {
                            'success' : f"{count} braiders are right here for you!".title(),
                            'warning' : None,
                            'error' : None,
                            }
                    }

                return Response(resp, status=status.HTTP_200_OK)
            else:

                resp = {
                    'status': status.HTTP_200_OK, 
                    'data': results.data, 
                    'messages': {
                            'success' : None,
                            'warning' : "Search something better".title(),
                            'error' : None,
                            }
                    }

                return Response(resp, status=status.HTTP_200_OK)

def index(request):

    posts = Post.objects.all()

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
            )
            braider_info = []

            if braiders:
                for braider in braiders:
                    try:
                        b = braider.locationinfo.country
                    except:
                        break

                    try:
                        braider_info.append({
                            'user_name': braider.user_name,
                            'country': braider.locationinfo.country,
                            'city': braider.locationinfo.city,
                            'profile_picture': braider.publicinfo.profile_picture,
                            'website': braider.businessinfo.website,
                            'name': braider.publicinfo.first_name + " " + braider.publicinfo.last_name,
                            'url': reverse('profile', kwargs={'user_name': braider.user_name})
                        })
                    except:
                        braider_info.append({
                            'user_name': braider.user_name,
                            'country': braider.locationinfo.country,
                            'city': braider.locationinfo.city,
                            'profile_picture': braider.publicinfo.profile_picture,
                            'name': braider.publicinfo.first_name + " " + braider.publicinfo.last_name,
                            'url': reverse('profile', kwargs={'user_name': braider.user_name})
                        })

                messages.success(request, f'Wow! {len(braider_info)} Braiders find you.'.title())
                context = {'form': form, 'braiders': braider_info, 'posts': posts}
            else:
                messages.warning(request, f'{query}: No braider is found. search something better.'.title())
                return redirect('index')
    else:
        form = BraiderFinder()
        context = {'form': form, 'posts': posts}

    return render(request, 'index.html', context)

def about(request):
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your message have been sent. we will get back to you as soon as possible.'.title())
            return redirect('index')
    else:
        form = MessageForm()

    return render(request, 'about.html', {'form': form})

def privacy(request):
    return render(request, 'privacy.html')



