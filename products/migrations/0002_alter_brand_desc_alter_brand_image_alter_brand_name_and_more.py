# Generated by Django 4.2.5 on 2023-09-30 04:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='brand',
            name='desc',
            field=models.TextField(max_length=255, verbose_name='Brand description'),
        ),
        migrations.AlterField(
            model_name='brand',
            name='image',
            field=models.ImageField(upload_to='brands/', verbose_name='Brand logo'),
        ),
        migrations.AlterField(
            model_name='brand',
            name='name',
            field=models.CharField(max_length=20, verbose_name='Brand name'),
        ),
        migrations.AlterField(
            model_name='product',
            name='is_new',
            field=models.BooleanField(default=False, verbose_name='New Arrival'),
        ),
    ]