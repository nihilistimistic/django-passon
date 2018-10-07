from django.conf.urls import url
from . import views

app_name = 'items'

urlpatterns = [
    url(r'books/', views.books_list, name="books_list"),
    url(r'bikes/', views.bikes_list, name="bikes_list"),
    url(r'misc/', views.items_list, name="items_list"),
    url(r'sell_book_form/', views.sell_book_form, name="sell_book_form"),
    url(r'sell_bike_form/', views.sell_bike_form, name="sell_bike_form"),
    url(r'sell_item_form/', views.sell_item_form, name="sell_item_form"),
]
