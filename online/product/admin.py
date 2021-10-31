from django.contrib import admin
from product.models import Category, Produser, Product, Basket, Status, Order, Orderline

# Register your models here.
admin.site.register(Category)
admin.site.register(Produser)
admin.site.register(Basket)
admin.site.register(Status)
admin.site.register(Order)
admin.site.register(Orderline)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'amount', 'price', 'thumbnail', 'id_category', 'id_produser', 'id')
