from django.urls import path
from . import views

urlpatterns = [
	path('collection/', views.collection, name='collection'),
	path('post/<int:id>/', views.post, name='post'),
]
