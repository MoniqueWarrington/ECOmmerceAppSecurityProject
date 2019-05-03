from django.http import HttpResponse, Http404
from django.views import generic
from django.shortcuts import get_object_or_404, render
from home.models import Product


def home(request):
    return render(request, "home.html")


def about_us(request):
    return render(request, "about_us.html")


def products(request):
    return render(request, "products.html", {'products': Product.objects.all()})


def product_detail(request, product_id):
    try:
        products = Product.objects.get(product_id=product_id)
    except Product.DoesNotExist:
        raise Http404('Product not found')
    return render(request, "product_detail.html", {'products': products})
