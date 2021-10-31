from django.shortcuts import render
from django.views import View
from product.models import Product


class IndexView(View):
    def get(self, request):
        products = Product.objects.all()
        return render(request, 'lending/index.html', {'product': products})
