from django.urls import path
from . import views

urlpatterns = [
	path('nft/', views.nft, name='nft'),

]
