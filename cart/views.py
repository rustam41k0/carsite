from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from django.views.generic import ListView

from mycarsite.models import Cars
from .cart import Cart
from .forms import CartAddCarForm


@require_POST
def cart_add(request, car_id):
    cart = Cart(request)
    product = get_object_or_404(Cars, id=car_id)
    form = CartAddCarForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(product=product,
                 quantity=cd['quantity'],
                 update_quantity=cd['update'])
    return redirect('reservations')


def cart_remove(request, car_id):
    cart = Cart(request)
    product = get_object_or_404(Cars, id=car_id)
    cart.remove(product)
    return redirect('reservations')


def cart_detail(request):
    cart = Cart(request)
    for item in cart:
        item['add_form'] = CartAddCarForm(initial={'update': True})
    return render(request, 'reservations', {'cart': cart})
