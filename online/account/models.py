from django.db import models

# Create your models here.
from django.contrib.auth import get_user_model

User = get_user_model()


class TypeUserProfile(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.name}: {self.id}'


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    surname = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    id_type_user_profile = models.ForeignKey(TypeUserProfile, on_delete=models.CASCADE)
    country = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    street = models.CharField(max_length=50)
    zip_code = models.IntegerField()

    class Meta:
        db_table = "customer"

    def __str__(self):
        return self.surname + " " + self.name