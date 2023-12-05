# frontend/views.py

from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def customers_page(request):
    return render(request, 'customers.html')
def createCustomerPage(request):
    return render(request, 'customer/create_customer.html')
def getCustomerPage(request):
    return render(request, 'customer/get_customer.html')
def putCustomerPage(request):
    return render(request, 'customer/update_customer.html')
def deleteCustomerPage(request):
    return render(request, 'customer/delete_customer.html')

def artisans_page(request):
    return render(request, 'artisans.html')

def materials_page(request):
    return render(request, 'materials.html')

def products_page(request):
    return render(request, 'products.html')
