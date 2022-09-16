from django.urls import path

from mycarsite.views import ReservationsView
from . import views

urlpatterns = [
    path('', ReservationsView.as_view(), name='reservations'),
    path('add/<int:car_id>/', views.cart_add, name='cart_add'),
    path('remove/<int:car_id>/', views.cart_remove, name='cart_remove'),
]
