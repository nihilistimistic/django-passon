from django.conf.urls import url
from . import views

app_name = 'transactions'

urlpatterns = [
    url(r'cart/', views.cart, name="cart"),
    url(r'transactions/', views.transactions_view, name="transactions"),
    url(r'report/', views.report, name="report"),
]
