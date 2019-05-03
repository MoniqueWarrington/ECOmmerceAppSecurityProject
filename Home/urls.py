from django.urls import path

from home import views


urlpatterns = [
    path('', views.home, name='Home Page'),
    path('about_us/', views.about_us, name='About Us'),
    path('products/', views.products, name='Products'),
    # Path for individual product detail page, done via product_id primary key
    path('product_detail/<int:product_id>',
         views.product_detail, name='Product Details'),
]
