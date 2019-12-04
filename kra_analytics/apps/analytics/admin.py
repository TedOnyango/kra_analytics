# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import Customer, TaxPayer, Supplier, Transaction, Product, Retailer, Manufacturer

admin.site.register(TaxPayer)
admin.site.register(Supplier)
admin.site.register(Customer)
admin.site.register(Transaction)
admin.site.register(Product)
admin.site.register(Retailer)
admin.site.register(Manufacturer)
