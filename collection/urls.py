from django.urls import path
from . import views

urlpatterns = [
	path('collection/', views.collection, name='collection'),
	path('collection-picture/', views.collection_picture, name='post'),
]
