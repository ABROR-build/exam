from django.db import models
from app_accounts.models import Accounts


class Categories(models.Model):
    category_name = models.CharField(max_length=300)

    class Meta:
        db_table = 'Categories'

    def __str__(self):
        return self.category_name


class Products(models.Model):
    seller = models.ForeignKey(Accounts, on_delete=models.CASCADE)
    category = models.ForeignKey(Categories, on_delete=models.CASCADE)
    name = models.CharField(max_length=500)
    description = models.CharField(max_length=1000)
    price = models.FloatField()
    image = models.ImageField(upload_to='product_images/')

    class Meta:
        db_table = 'Products'

    def __str__(self):
        return self.name


class Comments(models.Model):
    account = models.ForeignKey(Accounts, on_delete=models.CASCADE)
    product = models.ForeignKey(Products, on_delete=models.CASCADE)
    comment = models.CharField(max_length=1000)
