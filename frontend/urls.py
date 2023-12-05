# frontend/urls.py

from django.urls import path

from . import views
from .views import customers_page, artisans_page, materials_page, products_page

urlpatterns = [
    path('', views.index, name='index'),
    path('customers/', views.customers_page, name='customers'),
    path('customers/create/page', views.createCustomerPage, name='createCustomerPage'),
    path('customers/get/page', views.getCustomerPage, name='getCustomerPage'),
    path('customers/put/page', views.putCustomerPage, name='putCustomerPage'),
    path('customers/delete/page', views.deleteCustomerPage, name='deleteCustomerPage'),
    path('artisans/', views.artisans_page, name='artisans'),
    path('materials/', views.materials_page, name='materials'),
    path('products/', views.products_page, name='products'),
    # path('customers', customers, name='getAllCustomers'),
    # path('artisans', views.artisans_page, name='getAllArtisans'),
    # path('materials', views.materials_page, name='getAllMaterials'),
    # path('products', views.products_page, name='getAllProducts'),
    # Додайте інші шляхи за потреби
]
