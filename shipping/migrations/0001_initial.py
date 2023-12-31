# Generated by Django 4.2.5 on 2023-10-02 05:27

from django.db import migrations, models
import django.db.models.deletion
import django_countries.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', django_countries.fields.CountryField(max_length=2)),
                ('name', models.CharField(max_length=127)),
            ],
            options={
                'verbose_name_plural': 'countries',
            },
        ),
        migrations.CreateModel(
            name='DeliveryCompany',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=20, unique=True, verbose_name='Delivery Company Name')),
                ('email', models.EmailField(max_length=254)),
                ('number', models.CharField(db_index=True, max_length=63)),
                ('type', models.PositiveSmallIntegerField(choices=[(1, 'Fixed'), (2, 'Cell'), (3, 'Fax')])),
            ],
        ),
        migrations.CreateModel(
            name='TrackingInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tracking_num', models.CharField(max_length=30, unique=True, verbose_name='Tracking Number')),
                ('delivery_company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shipping.deliverycompany')),
            ],
        ),
        migrations.CreateModel(
            name='State',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('short_name', models.CharField(max_length=127)),
                ('long_name', models.CharField(max_length=254)),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shipping.country')),
            ],
        ),
        migrations.CreateModel(
            name='ShippingContact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('primary', models.BooleanField(default=False)),
                ('first_name', models.CharField(blank=True, max_length=30, null=True, verbose_name='First Name')),
                ('middle_name', models.CharField(blank=True, max_length=30, null=True, verbose_name='Middle Name')),
                ('last_name', models.CharField(blank=True, max_length=30, null=True, verbose_name='Last Name')),
                ('line1', models.CharField(max_length=255)),
                ('line2', models.CharField(blank=True, max_length=255, null=True)),
                ('line3', models.CharField(blank=True, max_length=255, null=True)),
                ('city', models.CharField(max_length=255)),
                ('zip', models.CharField(blank=True, max_length=31)),
                ('number', models.CharField(db_index=True, max_length=63)),
                ('type', models.PositiveSmallIntegerField(choices=[(1, 'Fixed'), (2, 'Cell'), (3, 'Fax')])),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='Modified at')),
                ('state', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='shipping.state')),
            ],
        ),
    ]
