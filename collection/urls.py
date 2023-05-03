from django.urls import path
from . import views

urlpatterns = [
	path('collection/', views.collection, name='collection'),
	path('collection-picture/<int:id>/', views.collection_picture, name='collection-picture'),
]
