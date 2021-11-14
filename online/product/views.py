from django.shortcuts import render, redirect
from django.views import View
from product.models import Product, Basket, ProductOrder, ProductBasket, Order, Status
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


class CompleteOrderView(View):
    def get(self, request):
        basket = Basket.objects.get(id_customer=get_user(request))
        product_baskets = ProductBasket.objects.filter(id_basket=basket)
        status = Status.objects.get(name="Сортировка")
        total = 0
        profile = get_user(request)
        order = Order.objects.create(id_status=status, total=total, id_customer=profile)
        # order = Order(id_status=status, total=total, id_customer=get_user(request)).save()
        for product_basket in product_baskets:
            ProductOrder(id_product=product_basket.id_product, id_order=order, numbers=product_basket.numbers,
                         price=product_basket.price).save()
            total += product_basket.price * product_basket.numbers
            ProductBasket.objects.filter(id_product=product_basket.id_product, id_basket=basket).delete()
        Order.objects.filter(id=order.id).update(total=total)
        return redirect("product:order_list")


class OrderView(View):
    def get(self, request):
        orders = Order.objects.filter(id_customer=get_user(request))
        return render(request, 'product/Orderlist.html', {'orders': orders})

class OrderDetailView(View):
    def get(self,request,id):
        order = Order.objects.get(id=id)
        products = ProductOrder.objects.filter(id_order=order)
        return render(request, 'product/Orderdetail.html', {'products': products})