from django.urls import path
from . import views

urlpatterns = [
    path('profile/', views.profile, name='profile'),
    path('post/', views.post, name='post'),
    path('saved/', views.saved, name='saved'),
    path('profile-details/', views.profile_details, name='profile-details'),
    path('post-details/', views.post_details, name='post-details'),
]

