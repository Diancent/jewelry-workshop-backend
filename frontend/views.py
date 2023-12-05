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
def createArtisanPage(request):
    return render(request, 'artisan/create_artisan.html')
def getArtisanPage(request):
    return render(request, 'artisan/get_artisan.html')
def putArtisanPage(request):
    return render(request, 'artisan/update_artisan.html')
def deleteArtisanPage(request):
    return render(request, 'artisan/delete_artisan.html')

def materials_page(request):
    return render(request, 'materials.html')
def createMaterialPage(request):
    return render(request, 'material/create_material.html')
def getMaterialPage(request):
    return render(request, 'material/get_material.html')
def putMaterialPage(request):
    return render(request, 'material/update_material.html')
def deleteMaterialPage(request):
    return render(request, 'material/delete_material.html')

def products_page(request):
    return render(request, 'products.html')
def createProductPage(request):
    return render(request, 'product/create_product.html')
def getProductPage(request):
    return render(request, 'product/get_product.html')
def putProductPage(request):
    return render(request, 'product/update_product.html')
def deleteProductPage(request):
    return render(request, 'product/delete_product.html')
