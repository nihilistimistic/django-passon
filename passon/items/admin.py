from django.contrib import admin
from .models import Book, Bike, Item

# Register your models here.

admin.site.register(Book)
admin.site.register(Bike)
admin.site.register(Item)
