from django.urls import path
from shop.views import index, detail, checkout, confimation, custom_logout, register
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', index, name='home'),
    path('<int:myid>', detail, name="detail"),
    path('checkout', checkout, name="checkout"),
    path('confirmation', confimation, name="confirmation" ),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),
    path('login/', auth_views.LoginView.as_view(template_name='shop/login.html'), name='login'),
    path('logout/', custom_logout, name='logout'),
     path('register/', views.register, name='register'),
]