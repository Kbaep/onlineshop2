# Generated by Django 3.2.8 on 2021-11-01 15:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0007_auto_20211024_0939'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderline',
            name='id_basket',
        ),
        migrations.RemoveField(
            model_name='orderline',
            name='id_order',
        ),
        migrations.RemoveField(
            model_name='orderline',
            name='id_product',
        ),
        migrations.DeleteModel(
            name='Basket',
        ),
        migrations.DeleteModel(
            name='Orderline',
        ),
    ]