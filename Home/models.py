from django.db import models


class Administrator(models.Model):
    admin_ID = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email_address = models.EmailField(max_length=100)
    phone_number = models.IntegerField
    username = models.CharField(max_length=50)

    # to make the class more readable when outputted
    def __str__(self):
        return '%s %s %s %s %s %s' % (self.admin_ID,
                                      self.first_name,
                                      self.last_name,
                                      self.email_address,
                                      self.phone_number,
                                      self.username)


class Consumer(models.Model):
    consumer_ID = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email_address = models.EmailField(max_length=100)
    phone_number = models.IntegerField
    username = models.CharField(max_length=50)

    # to make the class more readable when outputted
    def __str__(self):
        return '%s %s %s %s %s %s' % (self.consumer_ID,
                                      self.first_name,
                                      self.last_name,
                                      self.email_address,
                                      self.phone_number,
                                      self.username)


class Product(models.Model):
    product_id = models.AutoField(primary_key=True)
    product_name = models.CharField(max_length=100)
    product_url = models.URLField(max_length=200)
    product_price = models.CharField(max_length=10, default="")
    product_description = models.CharField(max_length=300, default="")

    # to make the class more readable when outputted
    def __str__(self):
        return '%s %s %s %s %s' % (self.product_id,
                                   self.product_name,
                                   self.product_url,
                                   self.product_price,
                                   self.product_description)


class Company(models.Model):
    company_id = models.AutoField(primary_key=True)
    company_name = models.CharField(max_length=100)
    username = models.CharField(max_length=50)

    # to make the class more readable when outputted
    def __str__(self):
        return '%s %s %s' % (self.company_id,
                             self.company_name,
                             self.username)
