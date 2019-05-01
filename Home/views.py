from django.http import HttpResponse


def home(request):
    return HttpResponse("This will be the Home Page!")


def about_us(request):
    return HttpResponse("This will be the about us page")


def products(request):
    return HttpResponse("This will be the products page!!")


def product_details(request, product_id):
    return HttpResponse("This will be the product details page")
