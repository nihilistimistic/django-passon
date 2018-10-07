from django.shortcuts import render

# Create your views here.


def cart(request):
    return render(request, 'transactions/cart.html')


def transactions_view(request):
    return render(request, 'transactions/transactions.html')


def report(request):
    return render(request, 'transactions/report.html')
