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
    path('artisans/create/page', views.createArtisanPage, name='createArtisanPage'),
    path('artisans/get/page', views.getArtisanPage, name='getArtisanPage'),
    path('artisans/put/page', views.putArtisanPage, name='putArtisanPage'),
    path('artisans/delete/page', views.deleteArtisanPage, name='deleteArtisanPage'),

    path('materials/', views.materials_page, name='materials'),
    path('materials/create/page', views.createMaterialPage, name='createMaterialPage'),
    path('materials/get/page', views.getMaterialPage, name='getMaterialPage'),
    path('materials/put/page', views.putMaterialPage, name='putMaterialPage'),
    path('materials/delete/page', views.deleteMaterialPage, name='deleteMaterialPage'),

    path('products/', views.products_page, name='products'),
    path('products/create/page', views.createProductPage, name='createProductPage'),
    path('products/get/page', views.getProductPage, name='getProductPage'),
    path('products/put/page', views.putProductPage, name='putProductPage'),
    path('products/delete/page', views.deleteProductPage, name='deleteProductPage'),
]
