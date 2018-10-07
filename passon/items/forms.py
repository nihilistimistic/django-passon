from django import forms
from . import models
import sys


class SellBookForm(forms.ModelForm):
    author = forms.CharField(max_length=200, help_text='Author of this book')
    title = forms.CharField(max_length=200, help_text='Title of this book')
    edition = forms.IntegerField(max_value=sys.maxsize, help_text='Edition of this book')
    is_engg = forms.BooleanField(help_text='Is this book related to Engineering?')
    branch = forms.CharField(max_length=8, help_text='Branch you think this book belongs to')
    sem = forms.CharField(max_length=2, help_text='Which students have to study this book?')
    description = forms.CharField(widget=forms.widgets.Textarea, max_length=200, help_text='Description of this book')
    quality = forms.CharField(max_length=3, help_text='Quality of this book')
    price = forms.IntegerField(max_value=sys.maxsize, help_text='Price you think would be fair for this book')

    class Meta:
        model = models.Book
        fields = ('author', 'title', 'edition', 'is_engg', 'branch', 'sem', 'description', 'quality', 'price')


class SellBikeForm(forms.ModelForm):
    title = forms.CharField(max_length=200, help_text='Brand Name of this cycle ?')
    # color ???
    description = forms.CharField(widget=forms.widgets.Textarea, max_length=200, help_text='Description of this cycle')
    quality = forms.CharField(max_length=3, help_text='Quality of this cycle')
    price = forms.IntegerField(max_value=sys.maxsize, help_text='Price you think would be fair for this cycle')

    class Meta:
        model = models.Bike
        fields = ('title', 'description', 'quality', 'price')


class SellItemForm(forms.ModelForm):
    title = forms.CharField(max_length=200, help_text='What is this item')
    description = forms.CharField(widget=forms.widgets.Textarea, max_length=200, help_text='Description of this item')
    quality = forms.CharField(max_length=3, help_text='Quality of this item')
    price = forms.IntegerField(max_value=sys.maxsize, help_text='Price you think would be fair for this item')

    class Meta:
        model = models.Item
        fields = ('title', 'description', 'quality', 'price')