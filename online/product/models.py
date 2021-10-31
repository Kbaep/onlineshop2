from django.db import models
from account.models import UserProfile


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Produser(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(max_length=500)
    amount = models.IntegerField()
    price = models.FloatField()
    thumbnail = models.ImageField(upload_to='./product', default='./product/Null.png'
                                  )
    # ImageField устанавливаем Pillow, чтобы можно было загружать картинки
    id_category = models.ForeignKey(Category, on_delete=models.CASCADE)
    id_produser = models.ForeignKey(Produser, on_delete=models.CASCADE)


class Basket(models.Model):
    id_customer = models.OneToOneField(UserProfile, on_delete=models.CASCADE)


class Status(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.name}'


class Order(models.Model):
    id_status = models.ForeignKey(Status, on_delete=models.CASCADE, null=True, blank=True)
    id_customer = models.OneToOneField(UserProfile, on_delete=models.CASCADE)
    total = models.FloatField()

    # def __str__(self):
    #     return f'{self.id_customer.name}'


class Orderline(models.Model):
    id_product = models.OneToOneField(Product, on_delete=models.CASCADE)
    id_basket = models.ForeignKey(Basket, on_delete=models.CASCADE, null=True, blank=True)
    id_order = models.ForeignKey(Order, on_delete=models.CASCADE, null=True, blank=True)
    numbers = models.IntegerField()
    price = models.FloatField()

    # def __str__(self):
    #     return f'{self.id_order}'
