from django.db import models
from accounts.models import Profile
from enum import Enum


class CategoryChoice(Enum):
    BOOK = 'Book'
    BIKE = 'Bike'
    MISC = 'Misc'


# Create your models here.


class Cart(models.Model):
    # owner of transactions, ond_delete to be set properly!!!
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)

    # item category
    item = models.CharField(max_length=4, choices=[(tag.name, tag.value) for tag in CategoryChoice])

    # item_id, MUST NOT DISPLAY TO USER
    item_id = models.CharField(max_length=1)

    # date added
    date_added = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return self.user.username


class Transaction(models.Model):
    # owner of transactions, ond_delete to be set properly!!!
    # NAME NOT CHANGING TO OTHER THAN USER
    # buyer = models.ForeignKey(Profile, on_delete=models.CASCADE)
    buyer = models.ForeignKey(Profile, on_delete=models.CASCADE, blank=True)

    # item category
    item = models.CharField(max_length=4, choices=[(tag.name, tag.value) for tag in CategoryChoice])

    # item_id, MUST NOT DISPLAY TO USER
    item_id = models.CharField(max_length=1)

    # date of transaction
    date_of_transaction = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return self.buyer.username


# reports of users misbehaving on site
class Report(models.Model):
    # against whom
    # reported = models.CharField(max_length=DJANGO_DEFAULT_USERNAME_LENGTH)
    # NAME NOT CHANGING TO OTHER THAN USER
    reported = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='reported_user', blank=True)

    # by whom
    # reporter = models.CharField(max_length=DJANGO_DEFAULT_USERNAME_LENGTH)
    # reporter = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='reporter')

    # reason
    reason = models.TextField(max_length=150)

    # date_of_report
    date_of_report = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    def __str__(self):
        # return self.reported + " reported by " + self.reporter
        return self.reported.username
