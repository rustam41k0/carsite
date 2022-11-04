from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST

from mycarsite.models import Cars
from .cart import Cart
from .forms import UserContactForm
from .sendemail import send


@require_POST
def cart_add(request, car_id):
    cart = Cart(request)
    car = get_object_or_404(Cars, id=car_id)
    cart.add(car=car)
    return redirect('reservations')


def cart_remove(request, car_id):
    cart = Cart(request)
    car = get_object_or_404(Cars, id=car_id)
    cart.remove(car)
    return redirect('reservations')


def cart_detail(request):
    cart = Cart(request)
    cars = []

    for car in cart:
        cars.append(car['car'].name)
    cart_length = len(cart.cart.values())

    if request.method == "GET":
        contact_form = UserContactForm()

    elif request.method == 'POST':
        contact_form = UserContactForm(request.POST)
        if contact_form.is_valid():
            name = contact_form.cleaned_data['name']
            email = contact_form.cleaned_data['email']
            chosen_cars = cars
            try:
                send(email, name, chosen_cars)
                cart.clear()
            except Exception() as ex:
                print(ex)
            return redirect('reservations')
    else:
        return HttpResponse('Неверный запрос.')

    return render(request, 'reservations.html', {'cart': cart,
                                                 'contact_form': contact_form,
                                                 'cart_length': cart_length})
