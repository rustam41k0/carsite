from django.shortcuts import render
from django.views.generic import ListView, DetailView

from cart.forms import CartAddCarForm
from mycarsite.models import *


class HomeView(ListView):
    model = Cars
    context_object_name = 'cars'
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['add_form'] = CartAddCarForm()
        return context


class PriceView(ListView):
    model = Cars
    context_object_name = 'cars'
    template_name = 'pricing.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['add_form'] = CartAddCarForm()
        return context


class CarsView(ListView):
    model = Cars
    template_name = 'car.html'
    context_object_name = 'cars'


class OneCarView(DetailView):
    model = Cars
    template_name = 'car-single.html'
    slug_url_kwarg = 'car_slug'
    context_object_name = 'car'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['cars'] = Cars.objects.all()[:3]
        return context


class BlogView(ListView):
    model = Posts
    template_name = 'blog.html'
    context_object_name = 'posts'


class SinglePostView(DetailView):
    model = Posts
    template_name = 'blog-single.html'
    slug_url_kwarg = 'blog_slug'
    context_object_name = 'post'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['tags'] = Tags.objects.all()
        context['categories'] = Category.objects.all()
        context['comments'] = Comments.objects.all()
        context['posts'] = Posts.objects.order_by('-time_create')[:3]
        return context


def contact(request):
    return render(request, 'contact.html')
