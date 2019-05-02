from django.http import HttpResponse
from django.views import generic
from django.shortcuts import render
from home.models import Product


def home(request):
    return render(request, "home.html")


def about_us(request):
    return render(request, "about_us.html")


def products(request):
    return render(request, "products.html",  {'products': Product.objects.all()})


def product_details(request):
    return render(request, "product_detail.html", {'products': Product.objects.all()})
