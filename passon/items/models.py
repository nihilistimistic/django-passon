from django.db import models
from accounts.models import Profile
from enum import Enum

# Profile se link h, User se kro
# Create your models here.


class BranchChoice(Enum):
    CSIT = 'Computer Science/Information Technology'
    ECE = 'Electronics and Communication Engineering'
    EE = 'Electrical Engineering'
    CIV = 'Civil Engineering'
    BIOT = 'Biotechnology'
    CHEM = 'Chemical Engineering'
    MECHPROD = 'Mechanical/Production Engineering'


class SemChoice(Enum):
    S1 = '1st'
    S2 = '2nd'
    S3 = '3rd'
    S4 = '4th'
    S5 = '5th'
    S6 = '6th'
    S7 = '7th'
    S8 = '8th'


class QualityChoice(Enum):
    NEW = 'New'
    GU = 'Gently Used'
    MU = 'Moderately Used'
    RU = 'Rigorously Used'

# ADD TAGS FOR SEARCH


class Book(models.Model):
    # seller (Foreign Key), ond_delete to be set properly!!!
    seller = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='book_seller')

    # buyer (Foreign Key)
    buyer = models.ForeignKey(Profile, default=None, on_delete=models.SET(None), related_name='book_buyer')

    # author
    author = models.CharField(max_length=200)

    # title
    title = models.CharField(max_length=200)

    # edition
    edition = models.IntegerField(blank=True, null=True)

    # is_engg ? Then:
    is_engg = models.BooleanField()

    # branch
    branch = models.CharField(max_length=8, choices=[(tag.name, tag.value) for tag in BranchChoice], blank=True)

    # sem
    sem = models.CharField(max_length=2, choices=[(tag.name, tag.value) for tag in SemChoice], blank=True)

    # description
    description = models.TextField(max_length=1000)

    # quality
    quality = models.CharField(max_length=3, choices=[(tag.name, tag.value) for tag in QualityChoice])

    # price
    price = models.IntegerField()

    # is_sold
    is_sold = models.BooleanField()

    # is_delivered
    is_delivered = models.BooleanField()

    # post date
    post_date = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    # IMAGE FIELD
    # image = models.ImageField(default='default.png', blank=True)

    def __str__(self):
        return self.title + ", " + self.author


class Bike(models.Model):
    # seller(Foreign Key), ond_delete to be set properly!!!
    seller = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='bike_seller')

    # buyer (Foreign Key)
    buyer = models.ForeignKey(Profile, default=None, on_delete=models.SET(None), related_name='bike_buyer')

    # title
    title = models.CharField(max_length=200)

    # colour

    # can use image processing to identify coloured cycles

    # description
    description = models.TextField(max_length=1000)

    # quality
    quality = models.CharField(max_length=3, choices=[(tag.name, tag.value) for tag in QualityChoice])

    # price
    price = models.IntegerField()

    # is_sold
    is_sold = models.BooleanField()

    # is_delivered
    is_delivered = models.BooleanField()

    # post date
    post_date = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    # IMAGE FIELD
    # image = models.ImageField(default='default.png', blank=True)

    def __str__(self):
        return self.title


class Item(models.Model):
    # seller(Foreign Key), ond_delete to be set properly!!!
    seller = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='Item_seller')

    # buyer (Foreign Key)
    buyer = models.ForeignKey(Profile, default=None, on_delete=models.SET(None), related_name='item_buyer')

    # title
    title = models.CharField(max_length=200)

    # description
    description = models.TextField(max_length=500)

    # quality
    quality = models.CharField(max_length=3, choices=[(tag.name, tag.value) for tag in QualityChoice])

    # price
    price = models.IntegerField()

    # is_sold
    is_sold = models.BooleanField()

    # is_delivered
    is_delivered = models.BooleanField()

    # post date
    post_date = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    # IMAGE FIELD
    # image = models.ImageField(default='default.png', blank=True)

    def __str__(self):
        return self.title
