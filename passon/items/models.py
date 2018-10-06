from django.db import models
# from django.contrib.auth.models import User
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
    # seller (Foreign Key)
    seller = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='book_seller')

    # buyer (Foreign Key)
    buyer = models.ForeignKey(Profile, default=None, on_delete=models.SET(None), related_name='book_buyer')

    # author
    author = models.CharField(max_length=200)

    # title
    title = models.CharField(max_length=200)

    # edition
    edition = models.IntegerField(blank=True, null=True)

    # branch
    branch = models.CharField(max_length=8, choices=[(tag.name, tag.value) for tag in BranchChoice])

    # sem
    sem = models.CharField(max_length=2, choices=[(tag.name, tag.value) for tag in SemChoice])

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

    def __str__(self):
        return self.title + ", " + self.author


class Bike(models.Model):
    # seller(Foreign Key)
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

    def __str__(self):
        return self.title


class Item(models.Model):
    # seller(Foreign Key)
    seller = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='item_seller')

    # buyer (Foreign Key)
    buyer = models.ForeignKey(Profile, default=None, on_delete=models.SET(None), related_name='item_buyer')

    # title
    title = models.CharField(max_length=200)

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

    def __str__(self):
        return self.title
