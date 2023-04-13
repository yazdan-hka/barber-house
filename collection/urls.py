from django.urls import path
from . import views

urlpatterns = [
	path('collection/', views.collection, name='collection'),
	path('collection-1/', views.collection_1, name='collection-1'),
]
