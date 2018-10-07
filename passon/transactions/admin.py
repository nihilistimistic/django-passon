from django.contrib import admin
from .models import Cart, Transaction, Report

# Register your models here.
admin.site.register(Cart)
admin.site.register(Transaction)
admin.site.register(Report)
