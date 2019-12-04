# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2019-12-03 10:16
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Manufacturer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('manufacturer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='analytics.Manufacturer')),
            ],
        ),
        migrations.CreateModel(
            name='Retailer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Supplier',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='TaxPayer',
            fields=[
                ('tax_pin', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('date_enrolled', models.DateTimeField()),
                ('tax_compliant', models.BooleanField(default=False)),
                ('last_date_of_filling', models.DateTimeField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount_received', models.DecimalField(decimal_places=2, max_digits=18)),
                ('vat_total', models.DecimalField(decimal_places=2, max_digits=18)),
                ('date_of_transaction', models.DateTimeField()),
                ('date_of_delivery', models.DateTimeField()),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='customer_transactions', to='analytics.Customer')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product_transactions', to='analytics.Product')),
                ('retailer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='retail_transactions', to='analytics.Retailer')),
            ],
        ),
        migrations.AddField(
            model_name='supplier',
            name='tax_profile',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product_suppliers', to='analytics.TaxPayer'),
        ),
        migrations.AddField(
            model_name='retailer',
            name='tax_profile',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product_retailers', to='analytics.TaxPayer'),
        ),
        migrations.AddField(
            model_name='manufacturer',
            name='tax_profile',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product_manufactures', to='analytics.TaxPayer'),
        ),
        migrations.AddField(
            model_name='customer',
            name='tax_profile',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product_customers', to='analytics.TaxPayer'),
        ),
    ]
