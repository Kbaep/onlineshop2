from django.urls import path
from . import views
app_name = "product"
urlpatterns = [
    path('', views.BasketView.as_view(), name='basket'),
    path('buy/', views.BuyView.as_view(), name='buy'),
]