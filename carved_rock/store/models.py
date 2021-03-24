from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=100)
    stock_count = models.IntegerField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    description = models.TextField(default="")
    sku = models.CharField(max_length=20, verbose_name="stock keeping unit", unique=True)
    def __str__(self):
        return self.name

class ProductImage(models.Model):
    image = models.ImageField()
    product = models.ForeignKey('Product', on_delete=models.CASCADE)
    def __str__(self):
        return self.image

class Categorie(models.Model):
    name = models.CharField(max_length=100)
    product = models.ManyToManyField('Product')
    def __str__(self):
        return self.name
