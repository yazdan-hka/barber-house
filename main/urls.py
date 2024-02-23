from django.urls import path
from . import views

urlpatterns = [
	path('', views.index, name='index'),
	path('about/', views.about, name='about'),
	path('privacy-and-policy/', views.privacy, name='privacy'),
    path('search/', views.SearchBraidersAPIView.as_view(), name='braider-search'),
]
