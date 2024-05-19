from django.urls import path
from shop.views import index, detail, checkout,confimation
from . import views

urlpatterns = [
    path('', index, name='home'),
    path('<int:myid>', detail, name="detail"),
    path('checkout', checkout, name="checkout"),
    path('confirmation', confimation, name="confirmation" ),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),
]