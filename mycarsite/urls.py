from django.urls import path

from mycarsite.views import *

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('pricing/', PriceView.as_view(), name='pricing'),
    # path('reservations/', ReservationsView.as_view(), name='reservations'),
    path('car/', CarsView.as_view(), name='car'),
    path('blog/', BlogView.as_view(), name='blog'),
    path('blog_single/<slug:blog_slug>', SinglePostView.as_view(), name='blog_single'),
    path('contact/', contact, name='contact'),
    path('car_single/<slug:car_slug>/', OneCarView.as_view(), name='car_single'),
]
