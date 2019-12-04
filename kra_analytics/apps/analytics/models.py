# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


#--------------


class TaxPayer(models.Model):
    tax_pin = models.CharField(max_length=100, primary_key=True)
    date_enrolled = models.DateTimeField(null=False)

    tax_compliant = models.BooleanField(default=False)
    last_date_of_filling = models.DateTimeField(null=True)

    def __str__(self):
        return self.tax_pin


#-------------------


class Supplier(models.Model):
    name = models.CharField(max_length=50)
    tax_profile = models.ForeignKey('TaxPayer', related_name='product_suppliers')

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=50)
    manufacturer = models.ForeignKey('Manufacturer')

    def __str__(self):
        return self.name

class Customer(models.Model):
    name = models.CharField(max_length=50)
    tax_profile = models.ForeignKey('TaxPayer', related_name='product_customers')

    def __str__(self):
        return self.name

class Transaction(models.Model):
    retailer = models.ForeignKey('Retailer', related_name='retail_transactions')
    customer = models.ForeignKey('Customer', related_name='customer_transactions')
    product = models.ForeignKey('Product', related_name='product_transactions')

    amount_received = models.DecimalField(max_digits=18, decimal_places=2)

    transaction_total = models.DecimalField(max_digits=18, decimal_places=2)
    vat_total = models.DecimalField(max_digits=18, decimal_places=2)

    date_of_transaction = models.DateTimeField(null=False)
    date_of_delivery = models.DateTimeField(null=False)

    @property
    def transaction_total(self):
        return (self.transaction_total + self.vat_total)

    def __str__(self):
        return str(self.id)


#-------------------


class Manufacturer(models.Model):
    name = models.CharField(max_length=50)
    tax_profile = models.ForeignKey('TaxPayer', related_name='product_manufactures')

    def __str__(self):
        return self.name

class Retailer(models.Model):
    name = models.CharField(max_length=50)
    tax_profile = models.ForeignKey('TaxPayer', related_name='product_retailers')

    supplier = models.ForeignKey('Supplier', null=True)

    def __str__(self):
        return self.name
