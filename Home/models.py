from django.db import models


class Administrator(models.Model):
    admin_ID = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email_address = models.EmailField(max_length=100)
    phone_number = models.IntegerField(max_length=25)
    username = models.CharField(max_length=50)


class Consumer(models.Model):
    consumer_ID = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email_address = models.EmailField(max_length=100)
    phone_number = models.IntegerField(max_length=25)
    username = models.CharField(max_length=50)


class Product(models.Model):
    product_id = models.AutoField(primary_key=True)
    product_name = models.CharField(max_length=100)
    product_url = models.URLField(max_length=200)


class Company(models.Model):
    company_id = models.AutoField(primary_key=True)
    company_name = models.CharField(max_length=100)
    username = models.CharField(max_length=50)
