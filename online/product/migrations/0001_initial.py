# Generated by Django 3.2.7 on 2021-10-03 05:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Produser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField(max_length=500)),
                ('amount', models.IntegerField()),
                ('price', models.FloatField()),
                ('thumbnail', models.ImageField(upload_to='')),
                ('id_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.category')),
                ('id_produser', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.produser')),
            ],
        ),
    ]