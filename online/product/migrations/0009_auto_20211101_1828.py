# Generated by Django 3.2.8 on 2021-11-01 15:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_auto_20211003_0816'),
        ('product', '0008_auto_20211101_1819'),
    ]

    operations = [
        migrations.CreateModel(
            name='Basket',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_customer', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='account.userprofile')),
            ],
        ),
        migrations.CreateModel(
            name='ProductOrder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numbers', models.IntegerField()),
                ('price', models.FloatField()),
                ('id_order', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='product.order')),
                ('id_product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.product')),
            ],
        ),
        migrations.CreateModel(
            name='ProductBasket',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numbers', models.IntegerField()),
                ('price', models.FloatField()),
                ('id_basket', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='product.basket')),
                ('id_product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.product')),
            ],
        ),
        migrations.AddField(
            model_name='basket',
            name='product',
            field=models.ManyToManyField(through='product.ProductBasket', to='product.Product'),
        ),
    ]