from django.urls import path
from user import views

urlpatterns = [
	path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('fregister/', views.fregister, name='fregister'),
    path('flogin/', views.flogin, name='flogin'),
]
