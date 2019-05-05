from django.http import HttpResponse, Http404
from django.views import generic
from django.shortcuts import get_object_or_404, render
from home.models import Product, Review
from home.forms import ConsumerReviewForm


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

    context = {'products': products}

    if request.user.is_authenticated:
        form = ConsumerReviewForm
        context['form'] = form
        if request.method == 'POST':
            review = Review()
            form = ConsumerReviewForm(request.POST)
            if form.is_valid():
                # form.cleaned_data['review_text']
                review.review_text = form.cleaned_data['review_text']
                review.product_ID = product_id
                review.user_id = request.user.id
                review.save()

    return render(request, "product_detail.html", context)
