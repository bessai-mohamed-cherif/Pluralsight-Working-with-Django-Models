from django.contrib import admin

from .models import Product,ProductImage,Categorie

admin.site.register(Product)
admin.site.register(ProductImage)
admin.site.register(Categorie)