from django.urls import path
from user import views

urlpatterns = [
    path('braider-or-customer/', views.braider_or_customer, name='braider-or-customer'),
    path('fregister/', views.fregister, name='fregister'),
    path('flogin/', views.flogin, name='flogin'),
    # path('register/', views.register_page, name='register'),
    path('api/register/', views.RegisterBraiderAPIView.as_view(), name='braider-register'),
    path('customer-register/', views.customer_register, name='customer-register'),
    path('login/', views.login_page, name='login'),
    path('logout/', views.logout_page, name='logout'),
    path('validate-your-email/<str:user_name>/', views.validate_your_email, name='validate-your-email'),
    path('validate-email/<str:user_name>/<str:token>/', views.validate_email, name='validate-email'),
    path('reset-your-password-1/', views.reset_your_password_1, name='reset-your-password-1'),
    path('reset-your-password-2/', views.reset_your_password_2, name='reset-your-password-2'),
    path('create-new-password/<str:id>/<str:token>/', views.create_new_password, name='create-new-password'),
    # path('test-email/', views.test_email, name='test-email'),

]
