from django.shortcuts import render
from products.models import Product


def home(request):
    products = Product.objects.active()[:6]
    return render(request, 'home/home.html',{'products':products})
