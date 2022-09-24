from decimal import Decimal
from django.conf import settings
from mycarsite.models import Cars


class Cart(object):

    def __init__(self, request):
        # Инициализация корзины
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            # сохраняем ПУСТУЮ корзину в сессии
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart

    def __iter__(self):
        # Перебираем товары в корзине и получаем товары из базы данных.
        cars_ids = self.cart.keys()
        # получаем товары и добавляем их в корзину
        cars = Cars.objects.filter(id__in=cars_ids)

        cart = self.cart.copy()
        for car in cars:
            cart[str(car.id)]['car'] = car
        for item in cart.values():
            yield item

    # def __len__(self):
    #     return len(self.cart.values())

    def add(self, car):
        car_id = str(car.id)
        if car_id not in self.cart:
            self.cart[car_id] = {}
        self.save()

    def save(self):
        # сохраняем товар
        self.session.modified = True

    def remove(self, car):
        # Удаляем товар
        car_id = str(car.id)
        if car_id in self.cart:
            del self.cart[car_id]
            self.save()

    def get_total_price(self):
        # получаем общую стоимость
        return sum(Decimal(item['price']) for item in self.cart.values())

    def clear(self):
        # очищаем корзину в сессии
        del self.session[settings.CART_SESSION_ID]
        self.save()
