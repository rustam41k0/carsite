from django.urls import path
from . import views
from .views import cart_detail

urlpatterns = [
    path('', cart_detail, name='reservations'),
    path('add/<int:car_id>/', views.cart_add, name='cart_add'),
    path('remove/<int:car_id>/', views.cart_remove, name='cart_remove'),
]