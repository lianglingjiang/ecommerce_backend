# Generated by Django 4.2.5 on 2023-09-30 03:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='Modified at')),
            ],
            options={
                'verbose_name': 'Shopping Cart',
            },
        ),
        migrations.CreateModel(
            name='CartEntry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField(default=1)),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='Modified at')),
                ('cart', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cart.cart')),
                ('product', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='products.product')),
            ],
            options={
                'verbose_name': 'Cart Entry',
                'verbose_name_plural': 'Cart Entries',
            },
        ),
    ]
