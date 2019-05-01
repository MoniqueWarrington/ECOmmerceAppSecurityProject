from django.http import HttpResponse
from django.views import generic
from django.shortcuts import render


def home(request):
    return render(request, "home.html")


def about_us(request):
    return HttpResponse("This will be the about us page")


def products(request):
    return HttpResponse("This will be the products page!!")


def product_details(request):
    return render(request, "product_detail.html")
