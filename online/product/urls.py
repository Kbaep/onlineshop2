from django.urls import path
from . import views

app_name = "product"
urlpatterns = [
    path('', views.BasketView.as_view(), name='basket'),
    path('buy/', views.BuyView.as_view(), name='buy'),
    path('delete_product/', views.DeleteProductBasketView.as_view(), name='delete_product'),
    path('order/complete/', views.CompleteOrderView.as_view(), name='order_complete'),
    path('order/list/', views.OrderView.as_view(), name='order_list'),
    path('order/detail/<int:id>', views.OrderDetailView.as_view(), name='order_detail'),
]
