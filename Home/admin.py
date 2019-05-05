from django.contrib import admin
from .models import Company, Product, Consumer, Administrator, Review

admin.site.register(Company)
admin.site.register(Product)
admin.site.register(Consumer)
admin.site.register(Administrator)
admin.site.register(Review)
