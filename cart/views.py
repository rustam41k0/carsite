from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from django.views.generic import ListView, DetailView

from sendemail import send_email
from mycarsite.models import Cars
from .cart import Cart
from .forms import CartAddCarForm


@require_POST
def cart_add(request, car_id):
    cart = Cart(request)
    car = get_object_or_404(Cars, id=car_id)
    print(car)
    # form = CartAddCarForm(request.POST)
    # if form.is_valid():
    #     cd = form.cleaned_data
    cart.add(car=car)  # update_quantity=cd['update']
    return redirect('reservations')


def cart_remove(request, car_id):
    cart = Cart(request)
    car = get_object_or_404(Cars, id=car_id)
    cart.remove(car)
    return redirect('reservations')


def cart_detail(request):
    cart = Cart(request)
    send_mail = send_email()
    return render(request, 'reservations.html', {'cart': cart, 'send_email': send_mail})


