from django.shortcuts import render, redirect
from django.views import View
from product.models import Product, Basket
from account.services.account import get_user
# Create your views here.
app_name = "product"


class BasketView(View):
    def get(self, request):
        return render(request, 'product/index.html')


class BuyView(View):
    def post(self, request):
        id_product = request.POST['id_product']
        product = Product.objects.get(id=id_product)
        basket = Basket.objects.get(id_customer=get_user(request))

        return redirect("lending:index")
