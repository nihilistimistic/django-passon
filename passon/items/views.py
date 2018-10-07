from django.shortcuts import render
from . import forms

# Create your views here.


def books_list(request):
    return render(request, 'items/books_list.html')


def bikes_list(request):
    return render(request, 'items/bikes_list.html')


def items_list(request):
    return render(request, 'items/items_list.html')


def sell_book_form(request):
    form = forms.SellBookForm()
    return render(request, 'items/sell_book_form.html', {'form': form})


def sell_bike_form(request):
    form = forms.SellBikeForm()
    return render(request, 'items/sell_bike_form.html', {'form': form})


def sell_item_form(request):
    form = forms.SellItemForm()
    return render(request, 'items/sell_item_form.html', {'form': form})