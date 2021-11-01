from django.shortcuts import render, redirect
from django.views import View
from product.models import Product, Basket, ProductOrder, ProductBasket, Order
from account.services.account import get_user

# Create your views here.
app_name = "product"


class BasketView(View):
    def get(self, request):
        basket = Basket.objects.get(id_customer=get_user(request))
        product = ProductBasket.objects.filter(id_basket=basket)
        return render(request, 'product/index.html', {'products': product})


class BuyView(View):
    def post(self, request):
        id_product = request.POST['id_product']
        product = Product.objects.get(id=id_product)
        basket = Basket.objects.get(id_customer=get_user(request))
        if ProductBasket.objects.filter(id_product=product, id_basket=basket):
            product_basket = ProductBasket.objects.get(id_product=product, id_basket=basket)
            ProductBasket.objects.filter(id=product_basket.id).update(numbers=product_basket.numbers + 1)
        else:
            ProductBasket(id_product=product, id_basket=basket, numbers=1, price=product.price).save()
        return redirect("lending:index")


class DeleteProductBasketView(View):
    def post(self, request):
        id_product = request.POST['id_product']
        product = Product.objects.get(id=id_product)
        basket = Basket.objects.get(id_customer=get_user(request))
        product_basket = ProductBasket.objects.get(id_product=product, id_basket=basket)
        if product_basket.numbers > 1:
            ProductBasket.objects.filter(id=product_basket.id).update(numbers=product_basket.numbers - 1)
        else:
            ProductBasket.objects.filter(id_product=product, id_basket=basket).delete()
        return redirect("product:basket")
