from django.urls import path
from user import views

urlpatterns = [
    path('braider-or-customer/', views.braider_or_customer, name='braider-or-customer'),
    path('fregister/', views.fregister, name='fregister'),
    path('flogin/', views.flogin, name='flogin'),
    path('register/', views.register_page, name='register'),
    path('customer-register/', views.customer_register, name='customer-register'),
    path('login/', views.login_page, name='login'),
    path('logout/', views.logout_page, name='logout'),
    path('validate-your-email/', views.validate_your_email, name='validate-your-email')
]
