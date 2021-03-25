from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=100)
<<<<<<< HEAD
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
=======
    stock_count = models.IntegerField(help_text="How many items are currently in stock.")
    price = models.DecimalField(max_digits=6, decimal_places=2)
    description = models.TextField(default="", blank=True)
    sku = models.CharField(verbose_name="Stock Keeping Unit", max_length=20, unique=True)

    def __str__(self):
        return self.name


class ProductImage(models.Model):
    image = models.ImageField()
    product = models.ForeignKey('Product', on_delete=models.CASCADE)

    def __str__(self):
        return str(self.image)


class Category(models.Model):
    name = models.CharField(max_length=100)
    products = models.ManyToManyField('Product')

>>>>>>> fa9bec0 (fifth commit)
    def __str__(self):
        return self.name
