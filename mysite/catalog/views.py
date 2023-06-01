from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Item, Order, OrderItem

class HomeView(ListView):
    model = Item
    template_name = 'home.html'

def home(request):
    return render(request, 'home.htlm')

def product(request):
    return render(request, 'product.html')

def checkout(request):
    return render(request, 'checkout.html')